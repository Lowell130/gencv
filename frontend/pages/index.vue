<script setup>
const { isLoggedIn } = useAuth()

onMounted(() => {
  if (isLoggedIn.value) {
    navigateTo('/dashboard')
  } else {
    navigateTo('/login')
  }
})
</script>
