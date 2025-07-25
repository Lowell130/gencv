export default defineNuxtPlugin((nuxtApp) => {
  const token = useCookie('token')
  const refreshToken = useCookie('refresh_token')

  // Intercetta tutte le richieste $fetch
  nuxtApp.$fetch = async (request, options = {}) => {
    try {
      // Prima invio regolare
      return await $fetch(request, {
        ...options,
        headers: {
          ...options.headers,
          Authorization: `Bearer ${token.value}`,
        }
      })
    } catch (error) {
      // Se il token è scaduto (401), provo il refresh
      if (error?.response?.status === 401 && refreshToken.value) {
        try {
          const res = await $fetch('http://localhost:8000/refresh', {
            method: 'POST',
            body: { refresh_token: refreshToken.value }
          })

          // Aggiorno i cookie
          token.value = res.access_token

          // Riprovo la richiesta originale
          return await $fetch(request, {
            ...options,
            headers: {
              ...options.headers,
              Authorization: `Bearer ${res.access_token}`,
            }
          })
        } catch (refreshError) {
          console.error('Refresh token fallito:', refreshError)
          token.value = null
          refreshToken.value = null
          await navigateTo('/login')
        }
      }

      // Se non era un errore da refresh, rilancio l'errore
      throw error
    }
  }
})
