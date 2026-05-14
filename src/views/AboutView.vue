<template>
  <div class="about">
    <h1>This is an about page</h1>
    <p>WeChat SDK 状态：{{ sdkStatus }}</p>
    <wx-open-launch-weapp
      uid="udc9829"
      appid="wxa5bde20e1cbebfd3"
      username="gh_19031b59ab68"
      env-version="release"
      path="/omodule/webview/trd?shareable=Y&amp;url=https%3A%2F%2Fm.lifeapp.pingan.com.cn%2Fm%2Fshopevo%2Fweb%2Findex.html%3FprdSource%3Dzeb%26zebopenid%3Dundefined%26zebTemp%3D1778751492670%23%2Fr%2F3KymVF%3Fp%3D3KymVF%26productCode%3D2648A%26parentCode%3Dfe0871eb-f333-479b-841f-7937cd147137%26isWechatAuth%3DY%26detailNo%3D1"
      ><script type="text/wxtag-template">
        <div>2222</div>
      </script></wx-open-launch-weapp
    >
  </div>
</template>
<script lang="ts">
import Vue from "vue";

export default Vue.extend({
  name: "AboutView",
  data() {
    return {
      sdkStatus: "初始化中",
    };
  },
  mounted() {
    this.initWechatSdk();
  },
  methods: {
    initWechatSdk() {
      const wx = window.wx || window.jWeixin;
      console.log("检测 wx 对象：", wx);
      if (!wx) {
        this.sdkStatus = "未检测到 wx，请确认 jweixin-1.6.0.js 已加载";
        return;
      }

      this.sdkStatus = "已检测到 wx，等待 config";

      wx.config({
        debug: true,
        appId: "wxa5bde20e1cbebfd3",
        timestamp: 1778753647,
        nonceStr: "6pdwkj435yx",
        signature: "a3c2b0fc96c341582b70d6a18ead5d85366b254c",
        jsApiList: [
          "checkJsApi",
          "updateAppMessageShareData",
          "updateTimelineShareData",
        ],
        openTagList: ["wx-open-launch-app"],
      });
      console.log("已调用 wx.config，等待 ready/error 事件");
      wx.ready(() => {
        this.sdkStatus = "wx ready，可调用微信 JSAPI";
      });

      wx.error((error: unknown) => {
        this.sdkStatus = `wx config 失败：${JSON.stringify(error)}`;
      });

      document.addEventListener("WeixinOpenTagsError", function (e) {
        console.warn(
          "检测到 WeixinOpenTagsError 事件，可能是开放标签使用受限：",
          e,
        );
        console.error(e); // 无法使用开放标签的错误原因，需回退兼容。仅无法使用开放标签，JS-SDK其他功能不受影响
      });
    },
  },
});
</script>
