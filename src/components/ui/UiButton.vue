<template>
  <button
    class="ui-button"
    :class="buttonClasses"
    :type="nativeType"
    :disabled="disabled || loading"
    :aria-busy="loading ? 'true' : undefined"
    @click="$emit('click', $event)"
  >
    <span v-if="loading" class="ui-button__spinner" aria-hidden="true" />
    <slot />
  </button>
</template>

<script lang="ts">
import Vue, { PropType } from 'vue';

type ButtonVariant = 'primary' | 'secondary' | 'danger' | 'ghost';
type ButtonSize = 'sm' | 'md' | 'lg';
type NativeType = 'button' | 'submit' | 'reset';

export default Vue.extend({
  name: 'UiButton',
  props: {
    variant: {
      type: String as PropType<ButtonVariant>,
      default: 'secondary',
      validator: (value: string) => ['primary', 'secondary', 'danger', 'ghost'].includes(value),
    },
    size: {
      type: String as PropType<ButtonSize>,
      default: 'md',
      validator: (value: string) => ['sm', 'md', 'lg'].includes(value),
    },
    nativeType: {
      type: String as PropType<NativeType>,
      default: 'button',
      validator: (value: string) => ['button', 'submit', 'reset'].includes(value),
    },
    disabled: {
      type: Boolean,
      default: false,
    },
    loading: {
      type: Boolean,
      default: false,
    },
  },
  computed: {
    buttonClasses(): Record<string, boolean> {
      return {
        [`ui-button--${this.variant}`]: this.variant !== 'secondary',
        [`ui-button--${this.size}`]: this.size !== 'md',
        'ui-button--loading': this.loading,
      };
    },
  },
});
</script>

<style lang="scss">
.ui-button {
  --button-bg: var(--button-secondary-bg);
  --button-bg-hover: var(--button-secondary-bg-hover);
  --button-bg-active: var(--button-secondary-bg-active);
  --button-text: var(--button-secondary-text);
  --button-border: var(--button-secondary-border);
  --button-height: var(--button-height-md);
  --button-padding-x: var(--button-padding-x-md);
  --button-font-size: var(--button-font-size-md);

  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  height: var(--button-height);
  padding: 0 var(--button-padding-x);
  border: 1px solid var(--button-border);
  border-radius: var(--radius-md);
  background: var(--button-bg);
  color: var(--button-text);
  font: inherit;
  font-size: var(--button-font-size);
  font-weight: 600;
  line-height: 1;
  text-decoration: none;
  cursor: pointer;
  transition: background-color 160ms ease, border-color 160ms ease, color 160ms ease, transform 120ms ease;
}

.ui-button:hover:not(:disabled) {
  background: var(--button-bg-hover);
}

.ui-button:active:not(:disabled) {
  background: var(--button-bg-active);
  transform: translateY(1px);
}

.ui-button:focus-visible {
  outline: 3px solid color-mix(in srgb, var(--color-primary), transparent 65%);
  outline-offset: 2px;
}

.ui-button:disabled,
.ui-button[aria-disabled='true'] {
  border-color: transparent;
  background: var(--color-disabled-bg);
  color: var(--color-disabled-text);
  cursor: not-allowed;
}

.ui-button--primary {
  --button-bg: var(--button-primary-bg);
  --button-bg-hover: var(--button-primary-bg-hover);
  --button-bg-active: var(--button-primary-bg-active);
  --button-text: var(--button-primary-text);
  --button-border: var(--button-primary-border);
}

.ui-button--danger {
  --button-bg: var(--button-danger-bg);
  --button-bg-hover: var(--button-danger-bg-hover);
  --button-bg-active: var(--button-danger-bg-active);
  --button-text: var(--button-danger-text);
  --button-border: var(--button-danger-border);
}

.ui-button--ghost {
  --button-bg: transparent;
  --button-bg-hover: color-mix(in srgb, var(--color-primary), transparent 90%);
  --button-bg-active: color-mix(in srgb, var(--color-primary), transparent 82%);
  --button-text: var(--color-primary);
  --button-border: transparent;
}

.ui-button--sm {
  --button-height: var(--button-height-sm);
  --button-padding-x: var(--button-padding-x-sm);
  --button-font-size: var(--button-font-size-sm);
}

.ui-button--lg {
  --button-height: var(--button-height-lg);
  --button-padding-x: var(--button-padding-x-lg);
  --button-font-size: var(--button-font-size-lg);
}

.ui-button--loading {
  cursor: progress;
}

.ui-button__spinner {
  width: 1em;
  height: 1em;
  border: 2px solid currentColor;
  border-right-color: transparent;
  border-radius: 50%;
  animation: ui-button-spin 700ms linear infinite;
}

@keyframes ui-button-spin {
  to {
    transform: rotate(360deg);
  }
}
</style>
