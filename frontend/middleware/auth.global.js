
// frontend/middleware/auth.global.js
export default defineNuxtRouteMiddleware((to) => {
  const token = useCookie('token')

  // Se sei su una pagina pubblica, lascia passare
  if (['/login', '/register'].includes(to.path)) {
    return
  }

  // Se non hai un token, blocca l’accesso
  if (!token.value) {
    return navigateTo('/login')
  }
})
