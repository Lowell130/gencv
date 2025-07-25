<template>
  <form @submit.prevent="submitForm">
    <!-- 👇 lo stesso markup Flowbite che hai usato, con v-model su dati locali -->
    <!-- Esempio per il titolo -->
    <div class="sm:col-span-2 mb-4">
      <label class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Titolo</label>
      <input v-model="title" type="text" class="form-input w-full" required />
    </div>

    <!-- Riepilogo -->
          <div class="sm:col-span-2">
            <label class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Riepilogo</label>
            <textarea v-model="data.summary" rows="4" placeholder="Breve descrizione" class="block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white"></textarea>
          </div>

          <!-- Esperienze -->
          <div class="sm:col-span-2">
            <h3 class="font-semibold text-gray-900 dark:text-white">Esperienze</h3>
            <div v-for="(exp, i) in data.experiences" :key="i" class="grid gap-4 mt-2 sm:grid-cols-2">
              <input v-model="exp.role" placeholder="Ruolo" class="p-2 border rounded dark:bg-gray-700 dark:text-white" />
              <input v-model="exp.company" placeholder="Azienda" class="p-2 border rounded dark:bg-gray-700 dark:text-white" />
              <input v-model="exp.start_date" placeholder="Data inizio (YYYY-MM)" class="p-2 border rounded dark:bg-gray-700 dark:text-white" />
              <input v-model="exp.end_date" placeholder="Data fine" class="p-2 border rounded dark:bg-gray-700 dark:text-white" />
              <textarea v-model="exp.description" placeholder="Descrizione" class="sm:col-span-2 p-2 border rounded dark:bg-gray-700 dark:text-white" />
            </div>
            <button type="button" @click="addExperience" class="mt-2 text-sm text-blue-600">➕ Aggiungi esperienza</button>
          </div>

          <!-- Educazione -->
          <div class="sm:col-span-2">
            <h3 class="font-semibold text-gray-900 dark:text-white">Educazione</h3>
            <div v-for="(edu, i) in data.education" :key="i" class="grid gap-4 mt-2 sm:grid-cols-2">
              <input v-model="edu.degree" placeholder="Titolo di studio" class="p-2 border rounded dark:bg-gray-700 dark:text-white" />
              <input v-model="edu.institution" placeholder="Istituto" class="p-2 border rounded dark:bg-gray-700 dark:text-white" />
              <input v-model="edu.year" placeholder="Anno" class="sm:col-span-2 p-2 border rounded dark:bg-gray-700 dark:text-white" />
            </div>
            <button type="button" @click="addEducation" class="mt-2 text-sm text-blue-600">➕ Aggiungi educazione</button>
          </div>

          <!-- Competenze -->
          <div class="sm:col-span-2">
            <h3 class="font-semibold text-gray-900 dark:text-white">Competenze</h3>
            <div v-for="(skill, i) in data.skills" :key="i" class="grid gap-4 mt-2 sm:grid-cols-2">
              <input v-model="skill.name" placeholder="Competenza" class="p-2 border rounded dark:bg-gray-700 dark:text-white" />
              <input v-model="skill.level" placeholder="Livello (es. Intermedio)" class="p-2 border rounded dark:bg-gray-700 dark:text-white" />
            </div>
            <button type="button" @click="addSkill" class="mt-2 text-sm text-blue-600">➕ Aggiungi competenza</button>
          </div>

          <!-- Lingue -->
          <div class="sm:col-span-2">
            <h3 class="font-semibold text-gray-900 dark:text-white">Lingue</h3>
            <div v-for="(lang, i) in data.languages" :key="i" class="mt-2">
              <input v-model="data.languages[i]" placeholder="Lingua" class="p-2 border rounded w-full dark:bg-gray-700 dark:text-white" />
            </div>
            <button type="button" @click="addLanguage" class="mt-2 text-sm text-blue-600">➕ Aggiungi lingua</button>
          </div>
        

   


    <button type="submit" class="btn btn-primary mt-4">
      {{ mode === 'edit' ? 'Salva modifiche' : 'Crea CV' }}
    </button>

    <p v-if="error" class="text-red-600 mt-2">{{ error }}</p>
    <p v-if="success" class="text-green-600 mt-2">{{ success }}</p>
  </form>
</template>

<script setup>
defineProps({
  mode: { type: String, default: 'create' }, // 'create' | 'edit'
  initialData: { type: Object, default: () => ({}) }
})
defineEmits(['submit']) // genitore riceve l'evento

const title = ref(initialData.title || '')
const data = reactive({
  summary: initialData.data?.summary || '',
  experiences: initialData.data?.experiences || [],
  education: initialData.data?.education || [],
  skills: initialData.data?.skills || [],
  languages: initialData.data?.languages || []
})

const error = ref('')
const success = ref('')

function submitForm() {
  if (!title.value) return error.value = 'Il titolo è obbligatorio'

  const cv = {
    title: title.value,
    data: toRaw(data)
  }

  error.value = ''
  success.value = ''
  emit('submit', cv)
}
</script>
