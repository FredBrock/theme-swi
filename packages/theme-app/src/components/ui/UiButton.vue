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
@import '@/styles/tokens/themes';

.ui-button {
  #{css-var-name(button-current-bg)}: css-var(button-secondary-bg);
  #{css-var-name(button-current-bg-hover)}: css-var(button-secondary-bg-hover);
  #{css-var-name(button-current-bg-active)}: css-var(button-secondary-bg-active);
  #{css-var-name(button-current-text)}: css-var(button-secondary-text);
  #{css-var-name(button-current-border)}: css-var(button-secondary-border);
  #{css-var-name(button-current-height)}: css-var(button-height-md);
  #{css-var-name(button-current-padding-x)}: css-var(button-padding-x-md);
  #{css-var-name(button-current-font-size)}: css-var(button-font-size-md);

  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  height: css-var(button-current-height);
  padding: 0 css-var(button-current-padding-x);
  border: 1px solid css-var(button-current-border);
  border-radius: css-var(button-radius);
  background: css-var(button-current-bg);
  color: css-var(button-current-text);
  font: inherit;
  font-size: css-var(button-current-font-size);
  font-weight: 600;
  line-height: 1;
  text-decoration: none;
  cursor: pointer;
  transition: background-color 160ms ease, border-color 160ms ease, color 160ms ease, transform 120ms ease;
}

.ui-button:hover:not(:disabled) {
  background: css-var(button-current-bg-hover);
}

.ui-button:active:not(:disabled) {
  background: css-var(button-current-bg-active);
  transform: translateY(1px);
}

.ui-button:focus-visible {
  outline: 3px solid color-mix(in srgb, #{css-var(color-primary)}, transparent 65%);
  outline-offset: 2px;
}

.ui-button:disabled,
.ui-button[aria-disabled='true'] {
  border-color: transparent;
  background: css-var(color-disabled-bg);
  color: css-var(color-disabled-text);
  cursor: not-allowed;
}

.ui-button--primary {
  #{css-var-name(button-current-bg)}: css-var(button-primary-bg);
  #{css-var-name(button-current-bg-hover)}: css-var(button-primary-bg-hover);
  #{css-var-name(button-current-bg-active)}: css-var(button-primary-bg-active);
  #{css-var-name(button-current-text)}: css-var(button-primary-text);
  #{css-var-name(button-current-border)}: css-var(button-primary-border);
}

.ui-button--danger {
  #{css-var-name(button-current-bg)}: css-var(button-danger-bg);
  #{css-var-name(button-current-bg-hover)}: css-var(button-danger-bg-hover);
  #{css-var-name(button-current-bg-active)}: css-var(button-danger-bg-active);
  #{css-var-name(button-current-text)}: css-var(button-danger-text);
  #{css-var-name(button-current-border)}: css-var(button-danger-border);
}

.ui-button--ghost {
  #{css-var-name(button-current-bg)}: transparent;
  #{css-var-name(button-current-bg-hover)}: color-mix(in srgb, #{css-var(color-primary)}, transparent 90%);
  #{css-var-name(button-current-bg-active)}: color-mix(in srgb, #{css-var(color-primary)}, transparent 82%);
  #{css-var-name(button-current-text)}: css-var(color-primary);
  #{css-var-name(button-current-border)}: transparent;
}

.ui-button--sm {
  #{css-var-name(button-current-height)}: css-var(button-height-sm);
  #{css-var-name(button-current-padding-x)}: css-var(button-padding-x-sm);
  #{css-var-name(button-current-font-size)}: css-var(button-font-size-sm);
}

.ui-button--lg {
  #{css-var-name(button-current-height)}: css-var(button-height-lg);
  #{css-var-name(button-current-padding-x)}: css-var(button-padding-x-lg);
  #{css-var-name(button-current-font-size)}: css-var(button-font-size-lg);
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
