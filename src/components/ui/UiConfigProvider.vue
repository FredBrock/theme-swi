<template>
  <div
    class="ui-config-provider"
    :data-ui-theme="theme"
    :data-ui-density="density"
    :style="cssVars"
  >
    <slot />
  </div>
</template>

<script lang="ts">
import Vue, { PropType } from 'vue';

type Theme = 'light' | 'dark';
type Density = 'comfortable' | 'compact';
type ThemeVars = Record<string, string | number>;

function kebabCase(value: string): string {
  return value.replace(/[A-Z]/g, match => `-${match.toLowerCase()}`);
}

export default Vue.extend({
  name: 'UiConfigProvider',
  props: {
    theme: {
      type: String as PropType<Theme>,
      default: 'light',
      validator: (value: string) => ['light', 'dark'].includes(value),
    },
    density: {
      type: String as PropType<Density>,
      default: 'comfortable',
      validator: (value: string) => ['comfortable', 'compact'].includes(value),
    },
    themeVars: {
      type: Object as PropType<ThemeVars>,
      default: () => ({}),
    },
  },
  computed: {
    cssVars(): ThemeVars {
      return Object.entries(this.themeVars).reduce<ThemeVars>((vars, [key, value]) => {
        vars[`--mc-${kebabCase(key)}`] = value;
        return vars;
      }, {});
    },
  },
});
</script>

<style lang="scss">
.ui-config-provider {
  background: var(--mc-color-bg);
  color: var(--mc-color-text);
  font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
}
</style>
