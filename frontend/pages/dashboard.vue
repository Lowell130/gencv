<template>
<section class="bg-gray-50 dark:bg-gray-900 py-3 sm:py-5">
  <div class="px-4 mx-auto max-w-screen-2xl lg:px-12">
      <div class="relative overflow-hidden bg-white shadow-md dark:bg-gray-800 sm:rounded-lg">
          <div class="flex flex-col px-4 py-3 space-y-3 lg:flex-row lg:items-center lg:justify-between lg:space-y-0 lg:space-x-4">
              <!-- <div class="flex items-center flex-1 space-x-4">
                  <h5>
                      <span class="text-gray-500">All Products:</span>
                      <span class="dark:text-white">123456</span>
                  </h5>
                  <h5>
                      <span class="text-gray-500">Total sales:</span>
                      <span class="dark:text-white">$88.4k</span>
                  </h5>
              </div> -->
              <div class="flex flex-col flex-shrink-0 space-y-3 md:flex-row md:items-center lg:justify-end md:space-y-0 md:space-x-3">
                  <!-- <button @click="goToNewCv" type="button" class="flex items-center justify-center px-4 py-2 text-sm font-medium text-white rounded-lg bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:ring-primary-300 dark:bg-primary-600 dark:hover:bg-primary-700 focus:outline-none dark:focus:ring-primary-800">
                      <svg class="h-4 w-4 mr-2" fill="currentColor" viewbox="0 0 20 20" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
                          <path clip-rule="evenodd" fill-rule="evenodd" d="M10 3a1 1 0 011 1v5h5a1 1 0 110 2h-5v5a1 1 0 11-2 0v-5H4a1 1 0 110-2h5V4a1 1 0 011-1z" />
                      </svg>
                     NUOVO CV
                  </button> -->
                  <button @click="goToNewCv"  type="button" class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center inline-flex items-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">
  NUOVO CV
<svg class="rtl:rotate-180 w-3.5 h-3.5 ms-2" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 14 10">
<path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M1 5h12m0 0L9 1m4 4L9 9"/>
</svg>
</button>
                  <!-- <button @click="exportSelected('word')" :disabled="!selectedCVs.length" type="button" class="flex items-center justify-center flex-shrink-0 px-3 py-2 text-sm font-medium text-gray-900 bg-white border border-gray-200 rounded-lg focus:outline-none hover:bg-gray-100 hover:text-primary-700 focus:z-10 focus:ring-4 focus:ring-gray-200 dark:focus:ring-gray-700 dark:bg-gray-800 dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700">
                      <svg class="w-4 h-4 mr-2" xmlns="http://www.w3.org/2000/svg" aria-hidden="true" fill="none" viewbox="0 0 24 24" stroke-width="1.5" stroke="currentColor">
                          <path stroke-linecap="round" stroke-linejoin="round" d="M16.023 9.348h4.992v-.001M2.985 19.644v-4.992m0 0h4.992m-4.993 0l3.181 3.183a8.25 8.25 0 0013.803-3.7M4.031 9.865a8.25 8.25 0 0113.803-3.7l3.181 3.182m0-4.991v4.99" />
                      </svg>
                      Export Word
                  </button>
                  <button @click="exportSelected('pdf')" :disabled="!selectedCVs.length" type="button" class="flex items-center justify-center flex-shrink-0 px-3 py-2 text-sm font-medium text-gray-900 bg-white border border-gray-200 rounded-lg focus:outline-none hover:bg-gray-100 hover:text-primary-700 focus:z-10 focus:ring-4 focus:ring-gray-200 dark:focus:ring-gray-700 dark:bg-gray-800 dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700">
                      <svg class="w-4 h-4 mr-2" xmlns="http://www.w3.org/2000/svg" fill="none" viewbox="0 0 24 24" stroke-width="2" stroke="currentColor" aria-hidden="true">
                          <path stroke-linecap="round" stroke-linejoin="round" d="M3 16.5v2.25A2.25 2.25 0 005.25 21h13.5A2.25 2.25 0 0021 18.75V16.5m-13.5-9L12 3m0 0l4.5 4.5M12 3v13.5" />
                      </svg>
                      Export PDF
                  </button> -->
                  <button
  @click="deleteSelected"
  :disabled="!selectedCVs.length"
  type="button"
  class="uppercase flex items-center justify-center flex-shrink-0 px-3 py-2 text-sm font-medium text-white bg-red-600 border border-red-700 rounded-lg focus:outline-none hover:bg-red-700 focus:z-10 focus:ring-4 focus:ring-red-300 dark:focus:ring-red-700 dark:bg-red-800 dark:border-red-700 dark:hover:bg-red-700"
>
  <svg class="w-4 h-4 mr-2" fill="none" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24">
    <path stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12" />
  </svg>
  Elimina CV
</button> 
              </div>
          </div>
          <div class="overflow-x-auto">
              <table class="w-full text-sm text-left text-gray-500 dark:text-gray-400">
                  <thead class="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400">
                      <tr>
                          <th scope="col" class="p-4">
                              <div class="flex items-center">
                                  <input id="checkbox-all" @change="toggleSelectAll($event)" :checked="areAllSelected" type="checkbox" class="w-4 h-4 bg-gray-100 border-gray-300 rounded text-primary-600 focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600">
                                  <label for="checkbox-all" class="sr-only">checkbox</label>
                              </div>
                          </th>
                          <th scope="col" class="px-4 py-3">Nome CV</th>
                          <th scope="col" class="px-4 py-3">Categoria</th>
                          <!-- <th scope="col" class="px-4 py-3">Stock</th> -->
                          <!-- <th scope="col" class="px-4 py-3">Sales/Day</th>
                          <th scope="col" class="px-4 py-3">Sales/Month</th>
                          <th scope="col" class="px-4 py-3">Rating</th>
                          <th scope="col" class="px-4 py-3">Sales</th> -->
            <th scope="col" class="px-4 py-3 text-center">Azioni</th>


                          <th scope="col" class="px-4 py-3">Creato</th>
                      </tr>
                  </thead>
                  <tbody>
<tr v-if="cvs.length === 0">
  <td colspan="9" class="text-center py-4 text-gray-600 dark:text-gray-300">
    Non sono presenti CV,
    <NuxtLink to="/cv/new" class="text-blue-600 hover:underline">crea il primo</NuxtLink>.
  </td>
</tr>

                      <tr v-for="cv in cvs" :key="cv.id"
                       class="border-b dark:border-gray-600 hover:bg-gray-100 dark:hover:bg-gray-700">
                          <td class="w-4 px-4 py-3">
                              <div class="flex items-center">
                                  <input :value="cv.id" v-model="selectedCVs" id="checkbox-table-search-1" type="checkbox" onclick="event.stopPropagation()" class="w-4 h-4 bg-gray-100 border-gray-300 rounded text-primary-600 focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600">
                                  <label for="checkbox-table-search-1" class="sr-only">checkbox</label>
                              </div>
                          </td>
          <th scope="row" class="px-4 py-3 font-medium text-gray-900 whitespace-nowrap dark:text-white">{{ cv.title }}</th>
                          <td class="px-4 py-2">

<span class="bg-primary-100 text-primary-800 text-xs font-medium px-2 py-0.5 rounded dark:bg-primary-900 dark:text-primary-300">
  {{ cv.category || '—' }}
</span>

                          </td>
                          <!-- <td class="px-4 py-2 font-medium text-gray-900 whitespace-nowrap dark:text-white">
                              <div class="flex items-center">
                                  <div class="inline-block w-4 h-4 mr-2 bg-red-700 rounded-full"></div>
                                  95
                              </div>
                          </td> -->
                          <!-- <td class="px-4 py-2 font-medium text-gray-900 whitespace-nowrap dark:text-white">-</td>
                          <td class="px-4 py-2 font-medium text-gray-900 whitespace-nowrap dark:text-white">-</td>
                          <td class="px-4 py-2 font-medium text-gray-900 whitespace-nowrap dark:text-white">
                              <div class="flex items-center">
                                  <svg aria-hidden="true" class="w-5 h-5 text-yellow-400" fill="currentColor" viewbox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                                      <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z" />
                                  </svg>
                                  <svg aria-hidden="true" class="w-5 h-5 text-yellow-400" fill="currentColor" viewbox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                                      <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z" />
                                  </svg>
                                  <svg aria-hidden="true" class="w-5 h-5 text-yellow-400" fill="currentColor" viewbox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                                      <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z" />
                                  </svg>
                                  <svg aria-hidden="true" class="w-5 h-5 text-yellow-400" fill="currentColor" viewbox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                                      <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z" />
                                  </svg>
                                  <svg aria-hidden="true" class="w-5 h-5 text-yellow-400" fill="currentColor" viewbox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                                      <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z" />
                                  </svg>
                                  <span class="ml-1 text-gray-500 dark:text-gray-400">-</span>
                              </div>
                          </td>
                          <td class="px-4 py-2 font-medium text-gray-900 whitespace-nowrap dark:text-white">
                              <div class="flex items-center">
                                  <svg xmlns="http://www.w3.org/2000/svg" viewbox="0 0 24 24" fill="currentColor" class="w-5 h-5 mr-2 text-gray-400" aria-hidden="true">
                                      <path d="M2.25 2.25a.75.75 0 000 1.5h1.386c.17 0 .318.114.362.278l2.558 9.592a3.752 3.752 0 00-2.806 3.63c0 .414.336.75.75.75h15.75a.75.75 0 000-1.5H5.378A2.25 2.25 0 017.5 15h11.218a.75.75 0 00.674-.421 60.358 60.358 0 002.96-7.228.75.75 0 00-.525-.965A60.864 60.864 0 005.68 4.509l-.232-.867A1.875 1.875 0 003.636 2.25H2.25zM3.75 20.25a1.5 1.5 0 113 0 1.5 1.5 0 01-3 0zM16.5 20.25a1.5 1.5 0 113 0 1.5 1.5 0 01-3 0z" />
                                  </svg>
                                  1.6M
                              </div>
                          </td> -->
  <td class="px-4 py-2 flex items-center justify-center space-x-2 text-gray-600 dark:text-gray-300">
  <!-- Anteprima -->
  <button @click="goToPreview(cv.id)" title="Anteprima">
    <svg class="w-5 h-5 hover:text-blue-600" fill="none" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24">
      <path stroke-linecap="round" stroke-linejoin="round" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
      <path stroke-linecap="round" stroke-linejoin="round" d="M2.458 12C3.732 7.943 7.523 5 12 5s8.268 2.943 9.542 7c-1.274 4.057-5.064 7-9.542 7s-8.268-2.943-9.542-7z" />
    </svg>
  </button>

  <!-- Modifica -->
  <NuxtLink :to="`/cv/${cv.id}`" title="Modifica">
    <svg class="w-5 h-5 hover:text-green-600" fill="none" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24">
      <path stroke-linecap="round" stroke-linejoin="round" d="M16.862 3.487a2.25 2.25 0 113.182 3.182L7.5 19.5 3 21l1.5-4.5 12.362-13.013z" />
    </svg>
  </NuxtLink>

  <!-- PDF -->
  <!-- <button @click="exportSingle(cv.id, 'pdf')" title="Esporta PDF">
    <svg class="w-5 h-5 hover:text-red-500" fill="none" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24">
      <path stroke-linecap="round" stroke-linejoin="round" d="M12 4v16m8-8H4" />
    </svg>
  </button> -->

 <select v-model="selectedTemplate" class="text-sm rounded border border-gray-300 p-1 dark:bg-gray-800 dark:text-white">
  <option v-for="template in availableTemplates" :key="template" :value="template">
    {{ template.replace('.docx', '').replace('_', ' ').toUpperCase() }}
  </option>
</select>



<button @click="downloadWord(cv.id, selectedTemplate)" title="Esporta Word">
  <svg class="w-5 h-5 hover:text-indigo-500" fill="none" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
  <path stroke-linecap="round" stroke-linejoin="round" d="M4 16v2a2 2 0 002 2h12a2 2 0 002-2v-2" />
  <path stroke-linecap="round" stroke-linejoin="round" d="M12 4v12m0 0l-4-4m4 4l4-4" />
</svg>

</button>

  <!-- Elimina -->
  <button @click="deleteSingle(cv.id)" title="Elimina">
    <svg class="w-5 h-5 hover:text-red-700" fill="none" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24">
      <path stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12" />
    </svg>
  </button>
</td>

                          <td class="px-4 py-2 font-medium text-gray-900 whitespace-nowrap dark:text-white">
  {{ formatDate(cv.created_at) }}
</td>

                      </tr>
                 
                  </tbody>
              </table>
          </div>
          <nav class="flex flex-col items-start justify-between p-4 space-y-3 md:flex-row md:items-center md:space-y-0" aria-label="Table navigation">
              <span class="text-sm font-normal text-gray-500 dark:text-gray-400">
                  Showing
                  <span class="font-semibold text-gray-900 dark:text-white">1-10</span>
                  of
                  <span class="font-semibold text-gray-900 dark:text-white">1000</span>
              </span>
              <ul class="inline-flex items-stretch -space-x-px">
                  <li>
                      <a href="#" class="flex items-center justify-center h-full py-1.5 px-3 ml-0 text-gray-500 bg-white rounded-l-lg border border-gray-300 hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white">
                          <span class="sr-only">Previous</span>
                          <svg class="w-5 h-5" aria-hidden="true" fill="currentColor" viewbox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                              <path fill-rule="evenodd" d="M12.707 5.293a1 1 0 010 1.414L9.414 10l3.293 3.293a1 1 0 01-1.414 1.414l-4-4a1 1 0 010-1.414l4-4a1 1 0 011.414 0z" clip-rule="evenodd" />
                          </svg>
                      </a>
                  </li>
                  <li>
                      <a href="#" class="flex items-center justify-center px-3 py-2 text-sm leading-tight text-gray-500 bg-white border border-gray-300 hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white">1</a>
                  </li>
                  <li>
                      <a href="#" class="flex items-center justify-center px-3 py-2 text-sm leading-tight text-gray-500 bg-white border border-gray-300 hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white">2</a>
                  </li>
                  <li>
                      <a href="#" aria-current="page" class="z-10 flex items-center justify-center px-3 py-2 text-sm leading-tight border text-primary-600 bg-primary-50 border-primary-300 hover:bg-primary-100 hover:text-primary-700 dark:border-gray-700 dark:bg-gray-700 dark:text-white">3</a>
                  </li>
                  <li>
                      <a href="#" class="flex items-center justify-center px-3 py-2 text-sm leading-tight text-gray-500 bg-white border border-gray-300 hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white">...</a>
                  </li>
                  <li>
                      <a href="#" class="flex items-center justify-center px-3 py-2 text-sm leading-tight text-gray-500 bg-white border border-gray-300 hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white">100</a>
                  </li>
                  <li>
                      <a href="#" class="flex items-center justify-center h-full py-1.5 px-3 leading-tight text-gray-500 bg-white rounded-r-lg border border-gray-300 hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white">
                          <span class="sr-only">Next</span>
                          <svg class="w-5 h-5" aria-hidden="true" fill="currentColor" viewbox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                              <path fill-rule="evenodd" d="M7.293 14.707a1 1 0 010-1.414L10.586 10 7.293 6.707a1 1 0 011.414-1.414l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414 0z" clip-rule="evenodd" />
                          </svg>
                      </a>
                  </li>
              </ul>
          </nav>
      </div>
  </div>
</section>
</template>

<script setup>
const cvs = ref([])
const error = ref('')
const selectedCVs = ref([])
const { token } = useAuth()
const router = useRouter()
const availableTemplates = ref([])
const selectedTemplate = ref("")

function goToNewCv() {
  router.push('/cv/new')
}

function formatDate(dateStr) {
  return new Date(dateStr).toLocaleDateString()
}

function toggleSelectAll(event) {
  if (event.target.checked) {
    selectedCVs.value = cvs.value.map(cv => cv.id)
  } else {
    selectedCVs.value = []
  }
}

async function fetchTemplates() {
  try {
    const res = await $fetch('http://localhost:8000/templates', {
      headers: { Authorization: `Bearer ${token.value}` },
    })
    availableTemplates.value = res.templates
    if (availableTemplates.value.length) {
      selectedTemplate.value = availableTemplates.value[0]
    }
  } catch (err) {
    console.error("Errore nel caricamento dei template:", err)
  }
}

onMounted(() => {
  caricaCvs()
  fetchTemplates()
})

const areAllSelected = computed(() => {
  return cvs.value.length && selectedCVs.value.length === cvs.value.length
})

async function exportSelected(format) {
  alert(`Esportazione di ${selectedCVs.value.length} CV in formato ${format.toUpperCase()} (simulazione)`)
  // TODO: invia i selectedCVs.value al backend per esportazione
}

async function caricaCvs() {
  try {
    const res = await $fetch('http://localhost:8000/cvs', {
      headers: { Authorization: `Bearer ${token.value}` }
    })
    cvs.value = res
  } catch {
    error.value = 'Errore nel recupero dei CV'
  }
}

async function deleteSelected() {
  if (!confirm(`Sei sicuro di voler eliminare ${selectedCVs.value.length} CV?`)) return

  try {
    await Promise.all(
      selectedCVs.value.map((id) =>
        $fetch(`http://localhost:8000/cvs/${id}`, {
          method: 'DELETE',
          headers: {
            Authorization: `Bearer ${token.value}`,
          },
        })
      )
    )

    // Aggiorna la lista dei CV e svuota la selezione
    await caricaCvs()
    selectedCVs.value = []

    alert('CV eliminati con successo.')
  } catch (e) {
    alert('Errore durante l\'eliminazione dei CV.')
  }
}
function goToPreview(id) {
  router.push(`/cv/preview/${id}`)
}

function exportSingle(id, format) {
  alert(`Esporto il CV ${id} in formato ${format.toUpperCase()} (simulazione)`)
  // TODO: logica reale da implementare
}

async function deleteSingle(id) {
  if (!confirm('Eliminare questo CV?')) return

  try {
    await $fetch(`http://localhost:8000/cvs/${id}`, {
      method: 'DELETE',
      headers: { Authorization: `Bearer ${token.value}` },
    })
    await caricaCvs()
    alert('CV eliminato.')
  } catch {
    alert('Errore durante l\'eliminazione.')
  }
}

async function downloadWord(cvId, templateName = "cv_template.docx") {
  try {
    const response = await fetch(`http://localhost:8000/cvs/${cvId}/export/word?template=${templateName}`, {
      headers: {
        Authorization: `Bearer ${token.value}`,
      }
    })

    if (!response.ok) {
      throw new Error('Errore durante il download')
    }

    const blob = await response.blob()
    const url = window.URL.createObjectURL(blob)
    const link = document.createElement('a')
    link.href = url
    link.download = `CV_${cvId}.docx`
    document.body.appendChild(link)
    link.click()
    link.remove()
    window.URL.revokeObjectURL(url)
  } catch (error) {
    alert('Errore durante il download del file Word.')
  }
}


onMounted(caricaCvs)
</script>
