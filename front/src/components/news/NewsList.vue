<!-- src/components/news/NewsList.vue -->
<template>
  <div class="bg-white rounded-lg shadow-md">
    <h2 class="text-lg font-bold p-4 border-b">최신 뉴스</h2>
    <div class="divide-y">
      <NewsCard
        v-for="news in newsList"
        :key="news.id"
        :news="news"
      />
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import NewsCard from './NewsCard.vue'

const newsList = ref([
  {
    id: 1,
    title: '신비의비버랜드 푸꾸미&도다리축제 개최',
    description: '상포항과 삼포항수산물위판장 3월 23일부터...',
    imageUrl: '/news-image-1.jpg'
  },
  // More news items...
])
</script>