<template>
  <section class="bg-white dark:bg-gray-900">
    <div class="py-8 px-4 mx-auto max-w-4xl lg:py-16">
      <h2 class="mb-4 text-xl font-bold text-gray-900 dark:text-white">Modifica CV</h2>

      <form @submit.prevent="modificaCv">
        <div class="grid gap-4 sm:grid-cols-2 sm:gap-6">

           <!-- Titolo -->
          <div class="sm:col-span-2">
           <h3 class="font-semibold text-gray-900 dark:text-white mb-4">Titolo</h3>
            <input v-model="title" type="text" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white" placeholder="Titolo del CV" required />
          </div>

          <!-- Categoria -->
          <div class="sm:col-span-2">
          <h3 class="font-semibold text-gray-900 dark:text-white mb-4">Categoria</h3>
            <select v-model="category" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:text-white">
              <option value="" disabled>Seleziona una categoria</option>
              <option value="Studente">Studente</option>
              <option value="Professionista">Professionista</option>
              <option value="IT">Informatica</option>
              <option value="Marketing">Marketing</option>
              <option value="Altro">Altro</option>
            </select>
          </div>

          <!-- Informazioni personali -->
<div class="sm:col-span-2">
   <!-- Divider opzionale -->
  <div class="w-full flex items-center my-8">
    <hr class="flex-grow border-t border-gray-300 dark:border-gray-700" />
    <span class="mx-4 whitespace-nowrap text-gray-900 dark:text-white font-medium bg-white dark:bg-gray-900 px-2">
      Informazioni personali
    </span>
    <hr class="flex-grow border-t border-gray-300 dark:border-gray-700" />
  </div>

  <div class="grid gap-4 sm:grid-cols-2 mt-2">
    <input v-model="data.personal_info.full_name" placeholder="Nome e Cognome" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:text-white" required />
    <input v-model="data.personal_info.phone" placeholder="Telefono" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:text-white" required />
    <input v-model="data.personal_info.email" placeholder="Email di contatto" type="email" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:text-white" required />
    <input v-model="data.personal_info.birth_date" placeholder="Data di nascita (es. 1990-01-01)" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:text-white" />
    <input v-model="data.personal_info.address" placeholder="Indirizzo (opzionale)" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:text-white" />
    <input v-model="data.personal_info.website" placeholder="Sito web personale (opzionale)" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:text-white" />
    <!-- Nazionalità -->
<select v-model="data.personal_info.nationality" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:text-white">
  <option disabled value="">Seleziona nazionalità</option>
  <option>Italiana</option>
  <option>Francese</option>
  <option>Tedesca</option>
  <option>Spagnola</option>
  <option>Altra</option>
</select>

<!-- Sesso -->
<select v-model="data.personal_info.gender" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:text-white">
  <option disabled value="">Seleziona sesso</option>
  <option>Maschio</option>
  <option>Femmina</option>
  <option>Altro</option>
  <option>Preferisco non specificare</option>
</select>

  </div>
















</div>

<!-- Profili social -->
<div class="sm:col-span-2">
 <!-- Divider opzionale -->
  <div class="w-full flex items-center my-8">
    <hr class="flex-grow border-t border-gray-300 dark:border-gray-700" />
    <span class="mx-4 whitespace-nowrap text-gray-900 dark:text-white font-medium bg-white dark:bg-gray-900 px-2">
      Social
    </span>
    <hr class="flex-grow border-t border-gray-300 dark:border-gray-700" />
  </div>

  <div
    v-for="(profile, i) in data.personal_info.social_profiles"
    :key="i"
    class="mt-2 grid grid-cols-2 gap-2 relative"
  >
    <input
      v-model="profile.platform"
      placeholder="Nome piattaforma (es. LinkedIn)"
     class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:text-white"
    />
    <input
      v-model="profile.url"
      placeholder="URL del profilo (es. https://linkedin.com/in/...)"
     class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:text-white"
    />
    <!-- <button
      type="button"
      @click="removeSocial(i)"
      class="absolute top-0 right-0 text-red-500 text-sm"
    >
      ✖
    </button> -->
  </div>

  <!-- Pulsanti azione -->
  <div class="flex items-center gap-2 mt-4">
    <button
      @click="addSocial"
      type="button"
      class="px-3 py-2 text-xs font-medium text-center inline-flex items-center text-white bg-blue-700 rounded-lg hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"
    >
      <svg class="w-[16px] h-[16px] text-white mr-2" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
        <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 12h14m-7 7V5"/>
      </svg>
      Aggiungi
    </button>

    <button
      v-if="data.personal_info.social_profiles.length"
      @click="removeSocial(data.personal_info.social_profiles.length - 1)"
      type="button"
      class="px-3 py-2 text-xs font-medium text-center inline-flex items-center text-white bg-red-600 rounded-lg hover:bg-red-700 focus:ring-4 focus:outline-none focus:ring-red-300 dark:bg-red-500 dark:hover:bg-red-600 dark:focus:ring-red-800"
    >
      <svg class="w-[16px] h-[16px] text-white mr-2" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
        <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/>
      </svg>
      Rimuovi ultimo
    </button>
  </div>
</div>

          <!-- Riepilogo -->
          <div class="sm:col-span-2">
          <!-- Divider opzionale -->
  <div class="w-full flex items-center my-8">
    <hr class="flex-grow border-t border-gray-300 dark:border-gray-700" />
    <span class="mx-4 whitespace-nowrap text-gray-900 dark:text-white font-medium bg-white dark:bg-gray-900 px-2">
      Riepilogo
    </span>
    <hr class="flex-grow border-t border-gray-300 dark:border-gray-700" />
  </div>
            <textarea v-model="data.summary" rows="4" placeholder="Breve descrizione" class="block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white"></textarea>
          </div>












      
    <!-- Esperienze -->
<div class="sm:col-span-2">
<!-- Divider opzionale -->
  <div class="w-full flex items-center my-8">
    <hr class="flex-grow border-t border-gray-300 dark:border-gray-700" />
    <span class="mx-4 whitespace-nowrap text-gray-900 dark:text-white font-medium bg-white dark:bg-gray-900 px-2">
      Esperienze
    </span>
    <hr class="flex-grow border-t border-gray-300 dark:border-gray-700" />
  </div>

  

  <draggable v-model="data.experiences" item-key="id" handle=".drag-handle">
  <!-- Divider tra i blocchi esperienza (dal secondo in poi) -->
     <template #item="{ element: exp, index: i }">
      <div class="grid gap-4 mt-8 sm:grid-cols-2 relative border border-dashed border-gray-300 p-4 rounded-lg bg-gray-100 dark:bg-gray-800">

      <!-- Handle per trascinare -->
      <div class="absolute -right-7 top-2 drag-handle cursor-move text-gray-500 dark:text-gray-300">
     <svg class="w-6 h-6 text-gray-800 dark:text-white" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24">
  <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 20V10m0 10-3-3m3 3 3-3m5-13v10m0-10 3 3m-3-3-3 3"/>
</svg>


      </div>
  <!-- <template v-if="i > 0">
    <div class="sm:col-span-2 my-6">
      <hr class="border-t border-gray-300 dark:border-gray-600" />
    </div>
  </template> -->

    <input v-model="exp.role" placeholder="Ruolo" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:text-white" />
   
    <input v-model="exp.company" placeholder="Azienda" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:text-white" />
    <input v-model="exp.client" placeholder="Cliente" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:text-white" />
    <input v-model="exp.start_date" placeholder="Data inizio (YYYY-MM)" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:text-white" />
    <div class="flex items-center gap-4">
  <!-- Campo end_date -->
  <input
    v-if="!exp.current"
    v-model="exp.end_date"
    placeholder="Data fine (YYYY-MM)"
    class="flex-1 bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:text-white"
  />

  <!-- Switch "In corso" -->
  <label class="inline-flex items-center cursor-pointer mt-2">
    <input type="checkbox" v-model="exp.current" class="sr-only peer" />
    <div class="relative w-11 h-6 bg-gray-200 peer-focus:outline-none peer-focus:ring-4 peer-focus:ring-blue-300 dark:peer-focus:ring-blue-800 rounded-full peer dark:bg-gray-700 peer-checked:after:translate-x-full rtl:peer-checked:after:-translate-x-full after:content-[''] after:absolute after:top-[2px] after:start-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all dark:border-gray-600 peer-checked:bg-blue-600 dark:peer-checked:bg-blue-600"></div>
    <span class="ms-3 text-sm font-medium text-gray-900 dark:text-gray-300">In corso</span>
  </label>
</div>

    <textarea v-model="exp.description" placeholder="Descrizione" class="sm:col-span-2 bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:text-white" />
    <input
  v-model="exp.tools"
  placeholder="Strumenti utilizzati (es. Jira, Active Directory)"
  class="sm:col-span-2 bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:text-white"
/>

<!-- Separatore opzionale -->
<div class="sm:col-span-2 flex justify-center my-2">
  <div class="w-full text-center p-4 text-sm text-yellow-800 rounded-lg bg-yellow-50 dark:bg-gray-800 dark:text-yellow-300" role="alert">
    <span class="font-medium">INFO:</span> I dati <strong>contrattuali</strong> sono facoltativi, ma se inseriti saranno visibili anche nel CV finale.
  </div>
</div>



    <input v-model="exp.contract" placeholder="Contratto"  class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:text-white" />
    <input v-model="exp.level" placeholder="Livello contratto"  class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:text-white" />
    <input v-model="exp.ral" placeholder="RAL"  class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:text-white" />

    <!-- <button type="button" @click="removeExperience(i)" class="absolute top-0 right-0 text-red-500 text-sm">✖</button> -->
</div>
     </template>
     
  </draggable>



  <!-- Pulsanti azione -->
  <div class="flex items-center gap-2 mt-4">
    
    <button
      type="button"
      @click="addExperience"
      class="px-3 py-2 text-xs font-medium text-center inline-flex items-center text-white bg-blue-700 rounded-lg hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"
    >
      <svg class="w-[16px] h-[16px] text-white mr-2" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
        <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 12h14m-7 7V5"/>
      </svg>
      Aggiungi esperienza
    </button>
    <button
      v-if="data.experiences.length"
      type="button"
      @click="removeExperience(data.experiences.length - 1)"
      class="px-3 py-2 text-xs font-medium text-center inline-flex items-center text-white bg-red-600 rounded-lg hover:bg-red-700 focus:ring-4 focus:outline-none focus:ring-red-300 dark:bg-red-500 dark:hover:bg-red-600 dark:focus:ring-red-800"
    >
      <svg class="w-[16px] h-[16px] text-white mr-2" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
        <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/>
      </svg>
      Rimuovi ultima
    </button>



  </div>
</div>



         
<!-- Educazione -->
<div class="sm:col-span-2">
  <!-- Divider -->
  <div class="w-full flex items-center my-8">
    <hr class="flex-grow border-t border-gray-300 dark:border-gray-700" />
    <span class="mx-4 whitespace-nowrap text-gray-900 dark:text-white font-medium bg-white dark:bg-gray-900 px-2">
      Educazione
    </span>
    <hr class="flex-grow border-t border-gray-300 dark:border-gray-700" />
  </div>

  <draggable v-model="data.education" item-key="id" handle=".drag-handle">
    <template #item="{ element: edu, index: i }">
      <div class="grid gap-4 mt-8 sm:grid-cols-2 relative border border-dashed border-gray-300 p-4 rounded-lg bg-gray-100 dark:bg-gray-800">
        
        <!-- Drag handle -->
        <div class="absolute -right-7 top-2 drag-handle cursor-move text-gray-500 dark:text-gray-300">
          <svg class="w-6 h-6 text-gray-800 dark:text-white" aria-hidden="true" xmlns="http://www.w3.org/2000/svg"
            width="24" height="24" fill="none" viewBox="0 0 24 24">
            <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
              d="M8 20V10m0 10-3-3m3 3 3-3m5-13v10m0-10 3 3m-3-3-3 3" />
          </svg>
        </div>

        <input v-model="edu.degree" placeholder="Titolo di studio"
          class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:text-white" />

        <input v-model="edu.institution" placeholder="Istituto"
          class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:text-white" />

        <input v-model="edu.year" placeholder="Anno o intervallo (es: 2020-2023)"
          class="sm:col-span-2 bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:text-white" />

        <div class="sm:col-span-2 flex items-center">
          <input type="checkbox" v-model="edu.ongoing" :id="'ongoing-edu-' + i"
            class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 dark:bg-gray-700 dark:border-gray-600" />
          <label :for="'ongoing-edu-' + i" class="ml-2 text-sm text-gray-900 dark:text-white">
            In corso
          </label>
        </div>
      </div>
    </template>
  </draggable>

  <!-- Pulsanti azione -->
  <div class="flex items-center gap-2 mt-4">
    <button type="button" @click="addEducation"
      class="px-3 py-2 text-xs font-medium text-center inline-flex items-center text-white bg-blue-700 rounded-lg hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">
      <svg class="w-[16px] h-[16px] text-white mr-2" xmlns="http://www.w3.org/2000/svg" fill="none"
        viewBox="0 0 24 24">
        <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
          d="M5 12h14m-7 7V5" />
      </svg>
      Aggiungi educazione
    </button>

    <button v-if="data.education.length" type="button" @click="removeEducation(data.education.length - 1)"
      class="px-3 py-2 text-xs font-medium text-center inline-flex items-center text-white bg-red-600 rounded-lg hover:bg-red-700 focus:ring-4 focus:outline-none focus:ring-red-300 dark:bg-red-500 dark:hover:bg-red-600 dark:focus:ring-red-800">
      <svg class="w-[16px] h-[16px] text-white mr-2" xmlns="http://www.w3.org/2000/svg" fill="none"
        viewBox="0 0 24 24">
        <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
          d="M6 18L18 6M6 6l12 12" />
      </svg>
      Rimuovi ultima
    </button>
  </div>
</div>





















          <!-- Competenze -->
<!-- Competenze -->
<div class="sm:col-span-2">
  <!-- Divider -->
  <div class="w-full flex items-center my-8">
    <hr class="flex-grow border-t border-gray-300 dark:border-gray-700" />
    <span class="mx-4 whitespace-nowrap text-gray-900 dark:text-white font-medium bg-white dark:bg-gray-900 px-2">
      Competenze
    </span>
    <hr class="flex-grow border-t border-gray-300 dark:border-gray-700" />
  </div>

  <div v-for="(skill, i) in data.skills" :key="i" class="grid gap-4 mt-2 sm:grid-cols-2 relative">
    <input
      v-model="skill.name"
      placeholder="Competenza"
      class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:text-white"
    />
    <select
      v-model="skill.level"
      class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:text-white"
    >
      <option value="" disabled selected>Livello</option>
      <option value="Base">Base</option>
      <option value="Intermedio">Intermedio</option>
      <option value="Avanzato">Avanzato</option>
      <option value="Esperto">Esperto</option>
      <option value="Specialistico">Specialistico</option>
    </select>

    <!-- <button
      type="button"
      @click="removeSkill(i)"
      class="absolute top-0 right-0 text-red-500 text-sm"
    >✖</button> -->
  </div>

  <!-- Pulsanti azione -->
  <div class="flex items-center gap-2 mt-4">
    <button
      type="button"
      @click="addSkill"
      class="px-3 py-2 text-xs font-medium text-center inline-flex items-center text-white bg-blue-700 rounded-lg hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"
    >
      <svg class="w-[16px] h-[16px] text-white mr-2" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
        <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 12h14m-7 7V5"/>
      </svg>
      Aggiungi competenza
    </button>

    <button
      v-if="data.skills.length"
      type="button"
      @click="removeSkill(data.skills.length - 1)"
      class="px-3 py-2 text-xs font-medium text-center inline-flex items-center text-white bg-red-600 rounded-lg hover:bg-red-700 focus:ring-4 focus:outline-none focus:ring-red-300 dark:bg-red-500 dark:hover:bg-red-600 dark:focus:ring-red-800"
    >
      <svg class="w-[16px] h-[16px] text-white mr-2" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
        <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/>
      </svg>
      Rimuovi ultima
    </button>
  </div>
</div>

















<!-- Lingue -->
<div class="sm:col-span-2">
  <!-- Divider -->
  <div class="relative flex items-center my-8">
    <hr class="flex-grow border-t border-gray-300 dark:border-gray-700" />
    <span class="absolute left-1/2 transform -translate-x-1/2 px-3 bg-white dark:bg-gray-900 text-gray-900 dark:text-white font-medium">
      Lingue
    </span>
  </div>

  <div v-for="(lang, i) in data.languages" :key="i" class="grid gap-4 mt-2 sm:grid-cols-2 relative">
    <input
      v-model="lang.name"
      placeholder="Lingua (es. Inglese)"
      class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:text-white"
    />
    <select
      v-model="lang.level"
      class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:text-white"
    >
     <option value="" disabled selected>Livello</option>
      <option value="Base">Base</option>
      <option value="Intermedio">Intermedio</option>
      <option value="Avanzato">Avanzato</option>
      <option value="Fluente">Fluente</option>
      <option value="Madrelingua">Madrelingua</option>
    </select>
  </div>

  <!-- Pulsanti azione -->
  <div class="flex items-center gap-2 mt-4">
  <button
      type="button"
      @click="addLanguage"
      class="px-3 py-2 text-xs font-medium text-center inline-flex items-center text-white bg-blue-700 rounded-lg hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"
    >
      <svg class="w-[16px] h-[16px] text-white mr-2" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
        <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 12h14m-7 7V5"/>
      </svg>
      Aggiungi lingua
    </button>

    <button
      v-if="data.languages.length"
      type="button"
      @click="removeLanguage(data.languages.length - 1)"
      class="px-3 py-2 text-xs font-medium text-center inline-flex items-center text-white bg-red-600 rounded-lg hover:bg-red-700 focus:ring-4 focus:outline-none focus:ring-red-300 dark:bg-red-500 dark:hover:bg-red-600 dark:focus:ring-red-800"
    >
      <svg class="w-[16px] h-[16px] text-white mr-2" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
        <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/>
      </svg>
      Rimuovi ultima
    </button>
  </div>
</div>




<!-- Profilo personale -->
<div class="sm:col-span-2">
<!-- Divider opzionale -->
  <div class="w-full flex items-center my-8">
    <hr class="flex-grow border-t border-gray-300 dark:border-gray-700" />
    <span class="mx-4 whitespace-nowrap text-gray-900 dark:text-white font-medium bg-white dark:bg-gray-900 px-2">
      Profilo personale
    </span>
    <hr class="flex-grow border-t border-gray-300 dark:border-gray-700" />
  </div>
  <textarea v-model="data.profile" rows="4" placeholder="Parla di te..." class="block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 dark:bg-gray-700 dark:border-gray-600 dark:text-white"></textarea>
</div>


<!-- Obiettivi -->
<div class="sm:col-span-2">
  <!-- Divider opzionale -->
  <div class="w-full flex items-center my-8">
    <hr class="flex-grow border-t border-gray-300 dark:border-gray-700" />
    <span class="mx-4 whitespace-nowrap text-gray-900 dark:text-white font-medium bg-white dark:bg-gray-900 px-2">
      Obiettivi
    </span>
    <hr class="flex-grow border-t border-gray-300 dark:border-gray-700" />
  </div>
  <textarea v-model="data.objectives" rows="3" placeholder="Dove vuoi arrivare?" class="block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 dark:bg-gray-700 dark:border-gray-600 dark:text-white"></textarea>
</div>


<!-- Soft Skills -->
<div class="sm:col-span-2">
  <!-- Divider opzionale -->
  <div class="w-full flex items-center my-8">
    <hr class="flex-grow border-t border-gray-300 dark:border-gray-700" />
    <span class="mx-4 whitespace-nowrap text-gray-900 dark:text-white font-medium bg-white dark:bg-gray-900 px-2">
      Soft Skills
    </span>
    <hr class="flex-grow border-t border-gray-300 dark:border-gray-700" />
  </div>

  <!-- Lista Soft Skills -->
  <div v-for="(soft, i) in data.soft_skills" :key="i" class="mt-2 relative">
    <input
      v-model="data.soft_skills[i]"
      placeholder="Es. Comunicazione"
      class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:text-white"
    />
    <!-- <button
      type="button"
      @click="removeSoftSkill(i)"
      class="absolute top-0 right-2 text-red-500 text-sm"
    >✖</button> -->
  </div>

  <!-- Pulsanti azione -->
  <div class="flex items-center gap-2 mt-4">
    <button
      type="button"
      @click="addSoftSkill"
      class="px-3 py-2 text-xs font-medium text-center inline-flex items-center text-white bg-blue-700 rounded-lg hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"
    >
      <svg class="w-[16px] h-[16px] text-white mr-2" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
        <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 12h14m-7 7V5" />
      </svg>
      Aggiungi
    </button>

    <button
      v-if="data.soft_skills.length"
      type="button"
      @click="removeSoftSkill(data.soft_skills.length - 1)"
      class="px-3 py-2 text-xs font-medium text-center inline-flex items-center text-white bg-red-600 rounded-lg hover:bg-red-700 focus:ring-4 focus:outline-none focus:ring-red-300 dark:bg-red-500 dark:hover:bg-red-600 dark:focus:ring-red-800"
    >
      <svg class="w-[16px] h-[16px] text-white mr-2" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
        <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
      </svg>
      Rimuovi ultima
    </button>
  </div>
</div>




<!-- Progetti -->
<div class="sm:col-span-2">
  <!-- Divider opzionale -->
  <div class="w-full flex items-center my-8">
    <hr class="flex-grow border-t border-gray-300 dark:border-gray-700" />
    <span class="mx-4 whitespace-nowrap text-gray-900 dark:text-white font-medium bg-white dark:bg-gray-900 px-2">
      Progetti
    </span>
    <hr class="flex-grow border-t border-gray-300 dark:border-gray-700" />
  </div>

  <!-- Lista progetti -->
  <div
    v-for="(proj, i) in data.projects"
    :key="i"
    class="grid gap-4 mt-2 sm:grid-cols-2 relative"
  >
    <template v-if="i > 0">
    <div class="sm:col-span-2 my-6">
      <hr class="border-t border-gray-300 dark:border-gray-600" />
    </div>
  </template>
    <input v-model="proj.title" placeholder="Titolo progetto" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:text-white" />
    <input v-model="proj.link" placeholder="Link (opzionale)" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:text-white" />
    <textarea v-model="proj.description" placeholder="Descrizione" class="sm:col-span-2 bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:text-white"></textarea>
    <!-- <button type="button" @click="removeProject(i)" class="absolute top-0 right-0 text-red-500 text-sm">✖</button> -->
  </div>

  <!-- Pulsanti azione -->
  <div class="flex items-center gap-2 mt-4">
    <button
      type="button"
      @click="addProject"
      class="px-3 py-2 text-xs font-medium text-center inline-flex items-center text-white bg-blue-700 rounded-lg hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"
    >
      <svg class="w-[16px] h-[16px] text-white mr-2" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
        <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 12h14m-7 7V5" />
      </svg>
      Aggiungi
    </button>

    <button
      v-if="data.projects.length"
      type="button"
      @click="removeProject(data.projects.length - 1)"
      class="px-3 py-2 text-xs font-medium text-center inline-flex items-center text-white bg-red-600 rounded-lg hover:bg-red-700 focus:ring-4 focus:outline-none focus:ring-red-300 dark:bg-red-500 dark:hover:bg-red-600 dark:focus:ring-red-800"
    >
      <svg class="w-[16px] h-[16px] text-white mr-2" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
        <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
      </svg>
      Rimuovi ultimo
    </button>
  </div>
</div>



<!-- Certificazioni -->
<div class="sm:col-span-2">
  <!-- Divider opzionale -->
  <div class="w-full flex items-center my-8">
    <hr class="flex-grow border-t border-gray-300 dark:border-gray-700" />
    <span class="mx-4 whitespace-nowrap text-gray-900 dark:text-white font-medium bg-white dark:bg-gray-900 px-2">
      Certificazioni
    </span>
    <hr class="flex-grow border-t border-gray-300 dark:border-gray-700" />
  </div>

  <!-- Lista certificazioni -->
  <div v-for="(cert, i) in data.certifications" :key="i" class="grid gap-4 mt-2 sm:grid-cols-3 relative">
    <input v-model="cert.name" placeholder="Certificazione" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:text-white" />
    <input v-model="cert.issuer" placeholder="Ente" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:text-white" />
    <input v-model="cert.year" placeholder="Anno" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:text-white" />

  </div>

  <!-- Pulsanti azione -->
  <div class="flex items-center gap-2 mt-4">
    <button
      type="button"
      @click="addCertification"
      class="px-3 py-2 text-xs font-medium text-center inline-flex items-center text-white bg-blue-700 rounded-lg hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"
    >
      <svg class="w-[16px] h-[16px] text-white mr-2" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
        <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 12h14m-7 7V5" />
      </svg>
      Aggiungi
    </button>

    <button
      v-if="data.certifications.length"
      type="button"
      @click="removeCertification(data.certifications.length - 1)"
      class="px-3 py-2 text-xs font-medium text-center inline-flex items-center text-white bg-red-600 rounded-lg hover:bg-red-700 focus:ring-4 focus:outline-none focus:ring-red-300 dark:bg-red-500 dark:hover:bg-red-600 dark:focus:ring-red-800"
    >
      <svg class="w-[16px] h-[16px] text-white mr-2" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
        <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
      </svg>
      Rimuovi ultima
    </button>
  </div>
</div>













        </div>

        <p v-if="error" class="mt-4 text-red-600">{{ error }}</p>
        <p v-if="success" class="mt-4 text-green-600">{{ success }}</p>
    <div class="flex justify-center">
      <button type="submit" class="inline-flex items-center px-5 py-2.5 mt-6 text-sm font-medium text-white bg-primary-700 rounded-lg hover:bg-primary-800 focus:ring-4 focus:ring-primary-200 dark:focus:ring-primary-900">
        Salva modifiche
      </button>
    </div>
      </form>
    </div>
  </section>
</template>

<script setup>
import draggable from 'vuedraggable'
definePageMeta({ middleware: 'auth' })
import { toRaw } from 'vue'

const route = useRoute()
const router = useRouter()
const { token } = useAuth()
const id = route.params.id

const title = ref('')
const data = reactive({
  profile: '',
  summary: '',
  objectives: '',
  experiences: [],
  education: [],
  skills: [],
  soft_skills: [],
  projects: [],
  certifications: [],
  languages: [],
  personal_info: {
    full_name: '',
    phone: '',
    email: '',
    birth_date: '',
    address: '',
    website: '',
    social_profiles: []
  }
})

const error = ref('')
const success = ref('')
const category = ref('')

onMounted(async () => {
  try {
    const cv = await $fetch(`http://localhost:8000/cvs/${id}`, {
      headers: { Authorization: `Bearer ${token.value}` }
    })
    title.value = cv.title
    category.value = cv.category || ''
    Object.assign(data, cv.data)
    data.experiences.forEach(exp => {
  exp.current = !exp.end_date // usa `current` come nel v-model
})
  } catch {
    error.value = 'Errore nel caricamento del CV'
  }
})

function addSocial() {
  data.personal_info.social_profiles.push({ platform: '', url: '' })
}
function removeSocial(index) {
  data.personal_info.social_profiles.splice(index, 1)
}
function addSoftSkill() {
  data.soft_skills.push('')
}
function removeSoftSkill(index) {
  data.soft_skills.splice(index, 1)
}
function addProject() {
  data.projects.push({ title: '', description: '', link: '' })
}
function removeProject(index) {
  data.projects.splice(index, 1)
}
function addCertification() {
  data.certifications.push({ name: '', issuer: '', year: '' })
}
function removeCertification(index) {
  data.certifications.splice(index, 1)
}


function addExperience() {
  data.experiences.push({ 
     id: Date.now(),  // 👈 ID univoco per il drag&drop
    role: '',
    company: '',
    start_date: '',
    end_date: '', 
    description: '', 
    in_progress: false, 
    contract: '', 
    level: '', 
    ral: '',
    tools: '', // 👈 aggiunto
  })
}

function removeExperience(index) {
  data.experiences.splice(index, 1)
}
function addEducation() {
  data.education.push({
    degree: '',
    institution: '',
    year: '',
    ongoing: false   // 👈 nuovo campo
  })
}

function removeEducation(index) {
  data.education.splice(index, 1)
}
function addSkill() {
  data.skills.push({ name: '', level: '' })
}
function removeSkill(index) {
  data.skills.splice(index, 1)
}
function addLanguage() {
  data.languages.push({ name: '', level: '' })
}
function removeLanguage(index) {
  data.languages.splice(index, 1)
}

async function modificaCv() {
  try {
    const sanitizedData = toRaw(data)
  sanitizedData.experiences = sanitizedData.experiences.map(exp => {
  if (exp.current) exp.end_date = null
  delete exp.current
  return exp
})

    await $fetch(`http://localhost:8000/cvs/${id}`, {
      method: 'PUT',
      headers: { Authorization: `Bearer ${token.value}` },
      body: {
        title: title.value,
        category: category.value,
        data: sanitizedData
      }
    })
    success.value = 'CV aggiornato con successo!'
    setTimeout(() => router.push('/dashboard'), 1000)
  } catch (err) {
    error.value = 'Errore durante l\'aggiornamento'
    console.error('Errore PUT:', err)
  }
}
</script>
