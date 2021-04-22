import { createRouter, createWebHistory } from 'vue-router'

import Home from '@/components/views/Home.vue'
import Catalogue from '@/components/views/Catalogue.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/catalogue',
    name: 'Catalogue',
    component: Catalogue
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
