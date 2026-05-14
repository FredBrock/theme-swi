<template>
  <main class="home">
    <h1>Vue 2 Playground</h1>
    <McButton @click="onClick">Primary Button</McButton>
    <McButton variant="ghost">Ghost Button</McButton>
  </main>
</template>

<script lang="ts">
import Vue from 'vue';

export default Vue.extend({
  name: 'HomeView',
  methods: {
    onClick() {
      window.alert('Vue 2 click event works');
    },
  },
});
</script>

<style scoped>
.home {
  min-height: 60vh;
  display: grid;
  place-content: center;
  gap: 12px;
}
</style>
