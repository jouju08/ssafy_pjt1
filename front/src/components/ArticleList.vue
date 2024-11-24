<template>
  <div>
    <h3>article list</h3>
    <ArticleListItem
      v-for="article in store.articles"
      :key="article.id"
      :article="article"
    />
  </div>
</template>

<script setup>
import { useCounterStore } from '@/stores/counter';
import ArticleListItem from '@/components/ArticleListItem.vue'; 
const store=useCounterStore()
</script>

<style scoped>

</style>