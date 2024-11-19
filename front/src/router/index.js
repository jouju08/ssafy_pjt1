import { createRouter, createWebHistory } from 'vue-router'
import MainPage from '../views/MainPage.vue'
import SignUpPage from '../views/SignUpPage.vue'
import InterestRateComparatorPage from '../views/InterestRateComparatorPage.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: MainPage,
    },
    {
      path: '/signup',
      name: 'SignUp',
      component: SignUpPage,
    },
    {
      path: '/RateComparator',
      name: 'RateComparator',
      component: InterestRateComparatorPage,
    },
  ],
})

export default router
