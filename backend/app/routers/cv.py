#app/routers/cv.py
# This module handles the CRUD operations for CVs (Curriculum Vitae) in the application.
from fastapi import APIRouter, Depends, HTTPException, status
from bson import ObjectId
from app.database import db
from app.schemas import CVCreate, CVUpdate
from app.dependencies import get_current_user
from datetime import datetime
from fastapi.responses import Response
from docxtpl import DocxTemplate
from io import BytesIO
from fastapi import Query
import os

TEMPLATE_DIR = "templates"

router = APIRouter()
cvs_collection = db["cvs"]

def cv_serializer(cv):
    cv["id"] = str(cv["_id"])
    del cv["_id"]
    return cv

@router.get("/cvs")
def get_user_cvs(user=Depends(get_current_user)):
    cvs = list(cvs_collection.find({"user_email": user["email"]}))
    return [cv_serializer(cv) for cv in cvs]

@router.post("/cvs", status_code=201)
def create_cv(cv: CVCreate, user=Depends(get_current_user)):
    new_cv = {
        "title": cv.title,
        "category": cv.category,  # ← aggiunto qui
        "data": cv.data.dict(),  # ← converti Pydantic model in dict
        "user_email": user["email"],
        "created_at": datetime.utcnow()
    }
    result = cvs_collection.insert_one(new_cv)
    new_cv["_id"] = result.inserted_id
    return cv_serializer(new_cv)

@router.get("/cvs/{cv_id}")
def get_cv(cv_id: str, user=Depends(get_current_user)):
    cv = cvs_collection.find_one({"_id": ObjectId(cv_id), "user_email": user["email"]})
    if not cv:
        raise HTTPException(status_code=404, detail="CV not found")
    return cv_serializer(cv)

@router.put("/cvs/{cv_id}")
def update_cv(cv_id: str, updated: CVUpdate, user=Depends(get_current_user)):
    try:
        result = cvs_collection.update_one(
            {"_id": ObjectId(cv_id), "user_email": user["email"]},
            {"$set": {
                "title": updated.title,
                "category": updated.category,  # ← aggiunto qui
                "data": updated.data.dict()  # ← anche qui
            }}
        )
        if result.matched_count == 0:
            raise HTTPException(status_code=404, detail="CV not found or not owned")
        return {"msg": "CV updated"}
    except Exception as e:
        print(f"Errore durante update_cv: {e}")
        raise HTTPException(status_code=500, detail="Errore interno durante aggiornamento CV")

@router.delete("/cvs/{cv_id}")
def delete_cv(cv_id: str, user=Depends(get_current_user)):
    result = cvs_collection.delete_one({"_id": ObjectId(cv_id), "user_email": user["email"]})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="CV not found or not owned")
    return {"msg": "CV deleted"}


@router.get("/cvs/{cv_id}/export/word")
def export_cv_word(
    cv_id: str,
    user=Depends(get_current_user),
    template: str = Query(default="cv_template.docx")  # 👈 parametro template
):
    cv = cvs_collection.find_one({"_id": ObjectId(cv_id), "user_email": user["email"]})
    if not cv:
        raise HTTPException(status_code=404, detail="CV non trovato")

    template_path = f"templates/{template}"
    try:
        tpl = DocxTemplate(template_path)
    except Exception:
        raise HTTPException(status_code=400, detail="Template non valido o mancante")

    tpl.render(cv)

    output = BytesIO()
    tpl.save(output)
    output.seek(0)

    return Response(
        content=output.read(),
        media_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        headers={"Content-Disposition": f'attachment; filename="{cv["title"]}.docx"'}
    )

@router.get("/templates")
def list_templates():
    try:
        files = os.listdir(TEMPLATE_DIR)
        docx_files = [f for f in files if f.endswith(".docx")]
        return {"templates": docx_files}
    except FileNotFoundError:
        raise HTTPException(status_code=500, detail="Cartella template non trovata")