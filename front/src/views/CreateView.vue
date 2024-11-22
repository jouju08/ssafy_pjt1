<!-- src/views/PostForm.vue -->
<template>
  <div class="container mx-auto px-4 py-8">
    <div class="bg-white rounded-lg shadow-md p-6">
      <h1 class="text-2xl font-bold text-[#699BF7] mb-6">
        {{ isEditing ? '게시글 수정' : '새 게시글 작성' }}
      </h1>

      <form @submit.prevent="handleSubmit" class="space-y-6">
        <div>
          <label class="block mb-2">제목</label>
          <input 
            v-model="title"
            type="text"
            class="w-full border rounded p-2"
            required
          >
        </div>

        <div>
          <label class="block mb-2">내용</label>
          <textarea
            v-model="content"
            class="w-full border rounded p-2 min-h-[300px]"
            required
          ></textarea>
        </div>

        <div class="flex justify-end gap-4">
          <button
            type="button"
            @click="router.back()"
            class="px-4 py-2 border rounded hover:bg-gray-100"
          >
            취소
          </button>
          <button
            type="submit"
            class="px-4 py-2 bg-[#699BF7] text-white rounded hover:bg-[#5b8ce6]"
          >
            {{ isEditing ? '수정하기' : '작성하기' }}
          </button>
        </div>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter, useRoute } from 'vue-router'

const router = useRouter()
const route = useRoute()
const isEditing = ref(false)
const title = ref('')
const content = ref('')

onMounted(() => {
  if (route.params.id) {
    isEditing.value = true
    // Fetch post data if editing
  }
})

const handleSubmit = async () => {
  try {
    // Submit logic here
    router.push('/article')
  } catch (error) {
    console.error('Error submitting post:', error)
  }
}
</script>