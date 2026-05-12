import Vue from 'vue'
import VueRouter, { RouteConfig } from 'vue-router'
import HomeView from '../views/HomeView.vue'

Vue.use(VueRouter)

const routes: Array<RouteConfig> = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },
  {
    path: '/button-theme',
    name: 'button-theme',
    component: () => import(/* webpackChunkName: "button-theme" */ '../views/ButtonThemeView.vue')
  },
  {
    path: '/hct-palette',
    name: 'hct-palette',
    component: () => import(/* webpackChunkName: "hct-palette" */ '../views/HctPaletteView.vue')
  },
  {
    path: '/root-theme',
    name: 'root-theme',
    component: () => import(/* webpackChunkName: "root-theme" */ '../views/RootThemeView.vue')
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
