<template>
  <div>
    <NavBar />
    <slot />
    <Footer />
  </div>
</template>

<script setup>
import NavBar from '~/components/NavBar.vue'
import Footer from '~/components/Footer.vue'
</script>
