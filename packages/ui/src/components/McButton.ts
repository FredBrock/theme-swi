export default {
  name: 'McButton',
  props: {
    variant: {
      type: String,
      default: 'primary',
    },
    disabled: {
      type: Boolean,
      default: false,
    },
  },
  methods: {
    onClick(this: any, event: MouseEvent) {
      if (this.disabled) return
      this.$emit('click', event)
    },
  },
  render(this: any) {
    return this.$createElement(
      'button',
      {
        class: ['mc-button', `mc-button--${this.variant}`],
        attrs: {
          disabled: this.disabled,
          type: 'button',
        },
        on: {
          click: this.onClick,
        },
      },
      this.$slots.default || ['Button'],
    )
  },
}
