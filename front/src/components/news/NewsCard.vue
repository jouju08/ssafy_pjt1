<!-- src/components/news/NewsCard.vue -->
<template>
  <div class="flex gap-4 p-4 border-b hover:bg-gray-50 transition-colors">
    <img 
      :src="news.imageUrl" 
      :alt="news.title"
      class="w-24 h-24 object-cover rounded"
    >
    <div>
      <h3 class="font-bold mb-2">{{ news.title }}</h3>
      <p class="text-sm text-gray-600">{{ news.description }}</p>
    </div>
  </div>
</template>

<script setup>
defineProps({
  news: {
    type: Object,
    required: true
  }
})
</script>