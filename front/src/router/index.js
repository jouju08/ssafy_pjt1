import { createRouter, createWebHistory } from 'vue-router'
import MainPage from '../views/MainPage.vue'
import SignUpPage from '../views/SignUpPage.vue'
import InterestRateComparatorPage from '../views/InterestRateComparatorPage.vue'
import ArticleView from '@/views/ArticleView.vue'
import DetailView from '@/views/DetailView.vue'
import CreateView from '@/views/CreateView.vue'
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
    {
      path: '/article',
      name: 'ArticleView',
      component: ArticleView,
    },
    {
      path: '/article/:id',
      name: 'DetailView',
      component: DetailView,
    },
    {
      path: '/article/create',
      name: 'CreateView',
      component: CreateView,
    },
  ],
})

export default router
