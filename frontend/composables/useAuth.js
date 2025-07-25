export const useAuth = () => {
  const token = useCookie('token')
  const refreshToken = useCookie('refresh_token') // nuovo

  const isLoggedIn = computed(() => !!token.value)

  const login = (access, refresh) => {
    token.value = access
    refreshToken.value = refresh
  }

  const logout = () => {
    token.value = null
    refreshToken.value = null
  }

  return { token, refreshToken, isLoggedIn, login, logout }
}
