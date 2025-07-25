<template>
  <section class="bg-white dark:bg-gray-900 min-h-screen py-12">
    <div class="max-w-3xl mx-auto px-4">
      <h1 class="text-3xl font-bold mb-6 text-gray-900 dark:text-white">Anteprima CV</h1>

      <div v-if="cv">
        <div class="mb-6">
          <h2 class="text-xl font-semibold text-primary-700 dark:text-primary-400">{{ cv.title }}</h2>
          <p class="text-gray-600 dark:text-gray-300 italic">Categoria: {{ cv.category || '—' }}</p>
        </div>

        <div class="mb-6">
          <h3 class="font-semibold text-lg text-gray-800 dark:text-white">Informazioni personali</h3>
          <ul class="space-y-1 text-gray-700 dark:text-gray-300">
            <li><strong>Nome:</strong> {{ cv.data.personal_info.full_name }}</li>
            <li><strong>Email:</strong> {{ cv.data.personal_info.email }}</li>
            <li><strong>Telefono:</strong> {{ cv.data.personal_info.phone }}</li>
            <li v-if="cv.data.personal_info.birth_date"><strong>Data di nascita:</strong> {{ cv.data.personal_info.birth_date }}</li>
            <li v-if="cv.data.personal_info.address"><strong>Indirizzo:</strong> {{ cv.data.personal_info.address }}</li>
<li>
  <strong>Sito web: </strong>
  <template v-if="cv.data.personal_info.website">
    <a :href="cv.data.personal_info.website" target="_blank" class="text-blue-600 hover:underline">
      {{ cv.data.personal_info.website }}
    </a>
  </template>
  <template v-else>
    <span class="text-gray-500">N/A</span>
  </template>
</li>          </ul>

          <div v-if="cv.data.personal_info.social_profiles?.length" class="mt-4">
            <h4 class="font-medium text-gray-800 dark:text-white mb-1">Profili social:</h4>
            <ul class="list-disc ml-6 space-y-1">
              <li v-for="(profile, i) in cv.data.personal_info.social_profiles" :key="i">
                <strong>{{ profile.platform }}:</strong> <a :href="profile.url" target="_blank" class="text-blue-600 hover:underline">{{ profile.url }}</a>
              </li>
            </ul>
          </div>
        </div>

        <div v-if="cv.data.profile" class="mb-6">
          <h3 class="font-semibold text-lg text-gray-800 dark:text-white">Profilo personale</h3>
          <p class="text-gray-700 dark:text-gray-300">{{ cv.data.profile }}</p>
        </div>

        <div v-if="cv.data.objectives" class="mb-6">
          <h3 class="font-semibold text-lg text-gray-800 dark:text-white">Obiettivi</h3>
          <p class="text-gray-700 dark:text-gray-300">{{ cv.data.objectives }}</p>
        </div>

        <div v-if="cv.data.summary" class="mb-6">
          <h3 class="font-semibold text-lg text-gray-800 dark:text-white">Riepilogo</h3>
          <p class="text-gray-700 dark:text-gray-300">{{ cv.data.summary }}</p>
        </div>

        <div v-if="cv.data.experiences.length" class="mb-6">
          <h3 class="font-semibold text-lg text-gray-800 dark:text-white mb-4">Esperienze</h3>
          <ol class="relative border-s border-gray-200 dark:border-gray-700">                   
            <li
              v-for="(exp, i) in cv.data.experiences"
              :key="i"
              class="mb-10 ms-4"
            >
              <div class="absolute w-3 h-3 bg-gray-200 rounded-full mt-1.5 -start-1.5 border border-white dark:border-gray-900 dark:bg-gray-700"></div>
              <time class="mb-1 text-sm font-normal leading-none text-gray-400 dark:text-gray-500">
                {{ exp.start_date }} - {{ exp.end_date || 'In corso' }}
              </time>
              <h3 class="text-lg font-semibold text-gray-900 dark:text-white">
                {{ exp.role }} - {{ exp.company }} {{ exp.client ? `(${exp.client})` : '' }}
              </h3>
              <p class="mb-2 text-base font-normal text-gray-500 dark:text-gray-400">
                {{ exp.description }}
              </p>
              <p v-if="exp.tools" class="text-sm text-gray-600 dark:text-gray-400 mb-4">
  <strong>Strumenti:</strong> {{ exp.tools }}
</p>

              <div v-if="exp.contract || exp.level || exp.ral" class="text-sm text-gray-600 dark:text-gray-400 space-y-1">
                <p v-if="exp.contract"><strong>Contratto:</strong> {{ exp.contract }}</p>
                <p v-if="exp.level"><strong>Livello:</strong> {{ exp.level }}</p>
                <p v-if="exp.ral"><strong>RAL:</strong> {{ exp.ral }}</p>
              </div>
            </li>
          </ol>
        </div>

       <div v-if="cv.data.education.length" class="mb-6">
  <h3 class="font-semibold text-lg text-gray-800 dark:text-white">Educazione</h3>
  <ul class="space-y-1 text-gray-700 dark:text-gray-300">
    <li v-for="(edu, i) in cv.data.education" :key="i">
      {{ edu.degree }} - {{ edu.institution }}
      <span v-if="edu.ongoing"> (In corso)</span>
      <span v-else> ({{ edu.year }})</span>
    </li>
  </ul>
</div>

      <div v-if="cv.data.skills.length" class="mb-6">
  <h3 class="font-semibold text-lg text-gray-800 dark:text-white mb-2">Competenze</h3>
  <div class="flex flex-wrap gap-2">
    <span
      v-for="(skill, i) in cv.data.skills"
      :key="i"
      :class="badgeClassByLevel(skill.level)"
      class="text-xs font-medium px-2.5 py-0.5 rounded-sm"
    >
      {{ skill.name }}<span v-if="skill.level"> ({{ skill.level }})</span>
    </span>
  </div>
</div>


        <div v-if="cv.data.soft_skills?.length" class="mb-6">
          <h3 class="font-semibold text-lg text-gray-800 dark:text-white">Soft Skills</h3>
          <ul class="space-y-1 text-gray-700 dark:text-gray-300">
            <li v-for="(skill, i) in cv.data.soft_skills" :key="i">{{ skill }}</li>
          </ul>
        </div>

        <div v-if="cv.data.languages.length" class="mb-6">
          <h3 class="font-semibold text-lg text-gray-800 dark:text-white">Lingue</h3>
          <ul class="space-y-1 text-gray-700 dark:text-gray-300">
            <li v-for="(lang, i) in cv.data.languages" :key="i">
              {{ lang.language }}<span v-if="lang.level">{{ lang.name }} ({{ lang.level }})</span>
            </li>
          </ul>
        </div>

        <div v-if="cv.data.projects?.length" class="mb-6">
          <h3 class="font-semibold text-lg text-gray-800 dark:text-white">Progetti</h3>
          <ul class="space-y-2 text-gray-700 dark:text-gray-300">
            <li v-for="(proj, i) in cv.data.projects" :key="i">
              <strong>{{ proj.title }}</strong>
              <span v-if="proj.link"> - <a :href="proj.link" target="_blank" class="text-blue-600 hover:underline">Vedi</a></span><br>
              <span class="text-sm">{{ proj.description }}</span>
            </li>
          </ul>
        </div>

        <div v-if="cv.data.certifications?.length" class="mb-6">
          <h3 class="font-semibold text-lg text-gray-800 dark:text-white">Certificazioni</h3>
          <ul class="space-y-1 text-gray-700 dark:text-gray-300">
            <li v-for="(cert, i) in cv.data.certifications" :key="i">
              {{ cert.name }}<span v-if="cert.issuer"> - {{ cert.issuer }}</span><span v-if="cert.year"> ({{ cert.year }})</span>
            </li>
          </ul>
        </div>
      </div>

      <p v-else class="text-gray-600 dark:text-gray-300">Caricamento in corso...</p>
    </div>
  </section>
</template>

<script setup>
const route = useRoute()
const { token } = useAuth()
const cv = ref(null)

onMounted(async () => {
  try {
    const data = await $fetch(`http://localhost:8000/cvs/${route.params.id}`, {
      headers: { Authorization: `Bearer ${token.value}` }
    })
    cv.value = data
  } catch (err) {
    console.error('Errore nel caricamento della preview:', err)
  }
})


const badgeClassByLevel = (level) => {
  const normalized = level?.toLowerCase()

  if (normalized?.includes('base') || normalized?.includes('principiante')) {
    return 'bg-red-100 text-red-800 dark:bg-red-900 dark:text-red-300'
  }
  if (normalized?.includes('intermedio') || normalized?.includes('medio')) {
    return 'bg-yellow-100 text-yellow-800 dark:bg-yellow-900 dark:text-yellow-300'
  }
  if (normalized?.includes('avanzato') || normalized?.includes('esperto') || normalized?.includes('senior')) {
    return 'bg-green-100 text-green-800 dark:bg-green-900 dark:text-green-300'
  }

  // Default style if level is not recognized
  return 'bg-gray-100 text-gray-800 dark:bg-gray-700 dark:text-gray-300'
}

</script>
