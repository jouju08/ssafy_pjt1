<template>
  <div>
    <h1>detail</h1>
    <div v-if="article">
      <p>글 번호:{{ article.id }}</p>
      <p>제목:{{ article.title }}</p>
      <p>내용:{{ article.content }}</p>
      <p>작성 시간:{{ article.created_at }}</p>
      <p>수정 시간:{{ article.updated_at }}</p>
    </div>
    <br>
    <div>
    <button @click="DeleteArticle">삭제</button>
    <button @click="ModifyArticle">수정</button>
    </div>
  </div>
</template>

<script setup>
import axios from 'axios';
import { onMounted , ref} from 'vue';
import { useAuthStore } from '@/stores/authStore';
import { RouterLink, useRoute, useRouter} from 'vue-router';
import { useCounterStore } from '@/stores/articleStore';
const AUTH=useAuthStore()
const store=useCounterStore()
const route=useRoute()
const router=useRouter()
const article=ref(null)
onMounted(()=>{
  axios({
    method:'get',
    url:`${store.API_URL}/article/${route.params.id}/`,
  })
    .then((res)=>{
      article.value=res.data
    })
    .catch(
      err=>console.log(err)
    )
})
const DeleteArticle=function(){
  axios({
    method:'delete',
    url:`${store.API_URL}/article/${route.params.id}/modify/`,
    headers:{
      Authorization:`Token ${AUTH.token}`
    },
  }).then(()=>{
    router.push({name:'ArticleView'})
  }).catch(err=>console.log(err))
}
const ModifyArticle=function(){
  axios({
    method:'put',
    url:`${store.API_URL}/article/${route.params.id}/modify/`,
    headers:{
      Authorization:`Token ${AUTH.token}`
    },
  }).then(()=>{
    router.push({name:'ArticleView'})
  }).catch(err=>console.log(err))
}
</script>

<style scoped>

</style>