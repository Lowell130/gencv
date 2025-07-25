<template>
  <div class="max-w-md mx-auto mt-12 p-6 bg-white rounded shadow dark:bg-gray-800">
    <h1 class="text-2xl font-semibold mb-4 text-gray-900 dark:text-white">Login</h1>
    <form @submit.prevent="loginUser" class="space-y-4">
      <input v-model="email" type="email" placeholder="Email" class="w-full p-2 border rounded dark:bg-gray-700 dark:text-white" />
      <input v-model="password" type="password" placeholder="Password" class="w-full p-2 border rounded dark:bg-gray-700 dark:text-white" />
      <button type="submit" class="w-full py-2 bg-blue-600 text-white rounded hover:bg-blue-700">Login</button>
    </form>
    <p v-if="error" class="mt-4 text-red-500 text-sm">{{ error }}</p>
  </div>
</template>

<script setup>
const email = ref('')
const password = ref('')
const error = ref('')
const { login } = useAuth()

async function loginUser() {
  try {
    const res = await $fetch('http://localhost:8000/login', {
      method: 'POST',
      body: {
        email: email.value,
        password: password.value
      }
    })

    // Salva entrambi i token nei cookie
    login(res.access_token)
    useCookie('refresh_token').value = res.refresh_token

    await navigateTo('/dashboard')
  } catch (err) {
    error.value = err?.data?.detail || 'Errore durante il login'
  }
}
</script>
