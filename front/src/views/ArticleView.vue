<template>
  <div>
    <RouterLink :to="{name:'CreateView'}">
      [CREATE]
    </RouterLink>
    <ArticleList/>
  </div>
</template>

<script setup>
import { onMounted } from 'vue';
import { useCounterStore } from '@/stores/articleStore';
import ArticleList  from '@/components/ArticleList.vue';
import { RouterLink } from 'vue-router';

const store=useCounterStore()
onMounted(()=>{
  store.getArticles()
})
</script>

<style scoped>

</style>