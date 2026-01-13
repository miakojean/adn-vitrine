import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: () => import('../views/HomePage.vue'),
    },
    {
      path:'/about',
      name: 'about',
      component: () => import('../views/AboutUsPage.vue')
    },
    {
      path:'/services',
      name: 'services',
      component: () => import('../views/ServicesPage.vue')
    }
    
  ],
})

export default router
