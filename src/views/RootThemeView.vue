<template>
  <RootThemeDemo />
</template>

<script lang="ts">
import Vue from 'vue';
import RootThemeDemo from '@/components/RootThemeDemo.vue';

export default Vue.extend({
  name: 'RootThemeView',
  components: {
    RootThemeDemo,
  },
});
</script>
