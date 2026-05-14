declare module '*.vue' {
  import Vue from 'vue'
  export default Vue
}

declare module '@meta-component/ui' {
  import { PluginObject } from 'vue'

  const plugin: PluginObject<never>
  export default plugin
}
