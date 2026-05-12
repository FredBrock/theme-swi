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
        vars[`--${kebabCase(key)}`] = value;
        return vars;
      }, {});
    },
  },
});
</script>

<style lang="scss">
$light-theme: (
  color-primary: #2563eb,
  color-primary-hover: #1d4ed8,
  color-primary-active: #1e40af,
  color-danger: #dc2626,
  color-danger-hover: #b91c1c,
  color-danger-active: #991b1b,
  color-bg: #ffffff,
  color-surface: #ffffff,
  color-text: #111827,
  color-text-muted: #6b7280,
  color-border: #d1d5db,
  color-disabled-bg: #f3f4f6,
  color-disabled-text: #9ca3af,
  radius-md: 8px,
  button-height-sm: 32px,
  button-height-md: 40px,
  button-height-lg: 48px,
  button-padding-x-sm: 12px,
  button-padding-x-md: 16px,
  button-padding-x-lg: 20px,
  button-font-size-sm: 14px,
  button-font-size-md: 14px,
  button-font-size-lg: 16px,
  button-primary-bg: var(--color-primary),
  button-primary-bg-hover: var(--color-primary-hover),
  button-primary-bg-active: var(--color-primary-active),
  button-primary-text: #ffffff,
  button-primary-border: var(--color-primary),
  button-secondary-bg: var(--color-surface),
  button-secondary-bg-hover: #f9fafb,
  button-secondary-bg-active: #f3f4f6,
  button-secondary-text: var(--color-text),
  button-secondary-border: var(--color-border),
  button-danger-bg: var(--color-danger),
  button-danger-bg-hover: var(--color-danger-hover),
  button-danger-bg-active: var(--color-danger-active),
  button-danger-text: #ffffff,
  button-danger-border: var(--color-danger),
);

$dark-theme: (
  color-primary: #60a5fa,
  color-primary-hover: #93c5fd,
  color-primary-active: #bfdbfe,
  color-danger: #f87171,
  color-danger-hover: #fca5a5,
  color-danger-active: #fecaca,
  color-bg: #0f172a,
  color-surface: #111827,
  color-text: #f8fafc,
  color-text-muted: #cbd5e1,
  color-border: #334155,
  color-disabled-bg: #1f2937,
  color-disabled-text: #64748b,
  radius-md: 8px,
  button-height-sm: 32px,
  button-height-md: 40px,
  button-height-lg: 48px,
  button-padding-x-sm: 12px,
  button-padding-x-md: 16px,
  button-padding-x-lg: 20px,
  button-font-size-sm: 14px,
  button-font-size-md: 14px,
  button-font-size-lg: 16px,
  button-primary-bg: var(--color-primary),
  button-primary-bg-hover: var(--color-primary-hover),
  button-primary-bg-active: var(--color-primary-active),
  button-primary-text: #0f172a,
  button-primary-border: var(--color-primary),
  button-secondary-bg: var(--color-surface),
  button-secondary-bg-hover: #1f2937,
  button-secondary-bg-active: #334155,
  button-secondary-text: var(--color-text),
  button-secondary-border: var(--color-border),
  button-danger-bg: var(--color-danger),
  button-danger-bg-hover: var(--color-danger-hover),
  button-danger-bg-active: var(--color-danger-active),
  button-danger-text: #0f172a,
  button-danger-border: var(--color-danger),
);

@mixin theme-vars($theme) {
  @each $name, $value in $theme {
    --#{$name}: #{$value};
  }
}

.ui-config-provider {
  background: var(--color-bg);
  color: var(--color-text);
  color-scheme: light;
  font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
  @include theme-vars($light-theme);
}

.ui-config-provider[data-ui-theme='dark'] {
  color-scheme: dark;
  @include theme-vars($dark-theme);
}

.ui-config-provider[data-ui-density='compact'] {
  --button-height-sm: 28px;
  --button-height-md: 34px;
  --button-height-lg: 40px;
  --button-padding-x-sm: 10px;
  --button-padding-x-md: 12px;
  --button-padding-x-lg: 16px;
}
</style>
