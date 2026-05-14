<template>
  <main class="demo-page">
    <h1>Vue 3 Playground</h1>
    <McButton @click="onClick">Primary Button</McButton>
    <McButton variant="ghost">Ghost Button</McButton>
  </main>
</template>

<script setup lang="ts">
const onClick = () => {
  window.alert('Vue 3 click event works')
}
</script>

<style scoped>
.demo-page {
  min-height: 100vh;
  display: grid;
  place-content: center;
  gap: 12px;
}
</style>
