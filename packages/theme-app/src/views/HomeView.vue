<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png">
    <HelloWorld msg="Welcome to Your Vue.js + TypeScript App"/>

    <section class="wx-panel">
      <h2>WeChat JS SDK</h2>
      <p>SDK 状态：{{ sdkStatus }}</p>
      <p class="wx-tip">签名参数需要服务端生成；请替换下方示例配置再进行真机微信内验证。</p>
      <button type="button" @click="checkSdk">检查 SDK 可用性</button>
    </section>
  </div>
</template>

<script lang="ts">
import Vue from 'vue';
import HelloWorld from '@/components/HelloWorld.vue'; // @ is an alias to /src

export default Vue.extend({
  name: 'HomeView',
  components: {
    HelloWorld,
  },
  data() {
    return {
      sdkStatus: '未检测',
    };
  },
  mounted() {
    this.initWechatSdk();
  },
  methods: {
    getWechatSdk() {
      return window.wx || window.jWeixin;
    },
    initWechatSdk() {
      const wx = this.getWechatSdk();

      if (!wx) {
        this.sdkStatus = '未加载（请确认 public/jweixin-1.6.0.js 已注入）';
        return;
      }

      this.sdkStatus = '已加载，待 config';

      wx.config({
        debug: false,
        appId: 'YOUR_APP_ID',
        timestamp: 0,
        nonceStr: 'YOUR_NONCE_STR',
        signature: 'YOUR_SIGNATURE',
        jsApiList: ['checkJsApi', 'updateAppMessageShareData', 'updateTimelineShareData'],
      });

      wx.ready(() => {
        this.sdkStatus = 'config 成功，可调用 JSAPI';
      });

      wx.error((error: unknown) => {
        this.sdkStatus = `config 失败：${JSON.stringify(error)}`;
      });
    },
    checkSdk() {
      const wx = this.getWechatSdk();

      if (!wx) {
        this.sdkStatus = '未加载 SDK';
        return;
      }

      if (!wx.checkJsApi) {
        this.sdkStatus = '当前 SDK 未暴露 checkJsApi';
        return;
      }

      wx.checkJsApi({
        jsApiList: ['updateAppMessageShareData', 'updateTimelineShareData'],
        success: () => {
          this.sdkStatus = 'checkJsApi 调用成功';
        },
        fail: (error: unknown) => {
          this.sdkStatus = `checkJsApi 调用失败：${JSON.stringify(error)}`;
        },
      });
    },
  },
});
</script>

<style scoped>
.wx-panel {
  margin: 24px auto;
  max-width: 640px;
  padding: 16px;
  border: 1px solid #d7dbe3;
  border-radius: 12px;
  text-align: left;
}

.wx-tip {
  font-size: 13px;
  color: #6b7280;
}

button {
  margin-top: 12px;
  height: 36px;
  padding: 0 12px;
  border: 1px solid #1f2937;
  background: #111827;
  color: #fff;
  border-radius: 8px;
  cursor: pointer;
}
</style>
