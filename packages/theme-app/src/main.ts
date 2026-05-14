import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import '@/styles/theme.scss'

Vue.config.productionTip = false
Vue.config.ignoredElements = ['wx-open-launch-weapp']

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
