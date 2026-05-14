declare module '*.vue' {
  import Vue from 'vue'
  export default Vue
}

interface WechatConfigPayload {
  debug?: boolean
  appId: string
  timestamp: number
  nonceStr: string
  signature: string
  jsApiList: string[]
}

interface WechatJsSdk {
  config: (config: WechatConfigPayload) => void
  ready: (callback: () => void) => void
  error: (callback: (error: unknown) => void) => void
  checkJsApi?: (options: {
    jsApiList: string[]
    success?: (res: unknown) => void
    fail?: (err: unknown) => void
  }) => void
}

interface Window {
  wx?: WechatJsSdk
  jWeixin?: WechatJsSdk
}
