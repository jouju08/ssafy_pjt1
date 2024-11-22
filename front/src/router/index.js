import { createRouter, createWebHistory } from 'vue-router'
import MainPage from '@/views/MainPage.vue'
import SignUpPage from '@/views/SignUpPage.vue'
import InterestRateComparatorPage from '@/views/InterestRateComparatorPage.vue'
import ArticleView from '@/views/ArticleView.vue'
import PostDetail from '@/views/PostDetail.vue'
import CreateView from '@/views/CreateView.vue'
import BankSearch from '@/views/BankSearch.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'MainPage',
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
    // {
    //   path: '/article/:id',
    //   name: 'PostDetail',
    //   component: PostDetail,
    // },
    {
      path: '/detail',
      name: 'PostDetail',
      component: PostDetail,
    },
    {
      path: '/article/create',
      name: 'CreateView',
      component: CreateView,
    },
    {
      path: '/find-bank',
      name: 'BankSearch',
      component: BankSearch,
    },
  ],
})

export default router
