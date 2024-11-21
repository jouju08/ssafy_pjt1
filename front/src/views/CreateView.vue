<template>
  <div>
    <h1>게시글 작성하기</h1>
    <form @submit.prevent="createArticle">
      <label for="title">제목: </label>
      <input type="text" id="title" v-model.trim="title"><br>
      <label for="content">내용: </label>
      <textarea id="content" v-model.trim="content"></textarea><br>
      <input type="submit">
    </form>
  </div>
</template>

<script setup>
import axios from 'axios';
import { useAuthStore } from '@/stores/authStore';
import { useCounterStore } from '@/stores/articleStore';
import { useRouter } from 'vue-router';
import { ref } from 'vue';
const AUTH=useAuthStore()
const store=useCounterStore()
const router=useRouter()
const title=ref(null)
const content=ref(null)
const createArticle=function(){
  axios({
    method:'post',
    url:`${store.API_URL}/article/create/`,
    headers:{
      Authorization:`Token ${AUTH.token}`
    },
    data:{
      title:title.value,
      content:content.value
    },
  }).then(()=>{
    router.push({name:'ArticleView'})
  }).catch(err=>console.log(err))
}
</script>

<style lang="scss" scoped>

</style>