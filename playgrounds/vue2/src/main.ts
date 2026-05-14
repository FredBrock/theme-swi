import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import MetaComponentUI from '@meta-component/ui'
import '@meta-component/ui/style.css'

Vue.config.productionTip = false
Vue.use(MetaComponentUI)

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
