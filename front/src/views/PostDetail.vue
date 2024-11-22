<!-- src/views/PostDetail.vue -->
<template>
  <div class="container mx-auto px-4 py-8">
    <div class="bg-white rounded-lg shadow-md p-6">
      <!-- Post Header -->
      <div class="border-b pb-4">
        <h1 class="text-2xl font-bold mb-4">{{ post.title }}</h1>
        <div class="flex justify-between text-gray-600">
          <div class="flex space-x-4">
            <span>작성자: {{ post.author }}</span>
            <span>작성일: {{ formatDate(post.createdAt) }}</span>
            <span>조회수: {{ post.views }}</span>
          </div>
          <div class="space-x-2">
            <button 
              v-if="isAuthor"
              @click="handleEdit" 
              class="text-[#699BF7] hover:text-[#5b8ce6]"
            >
              수정
            </button>
            <button 
              v-if="isAuthor"
              @click="handleDelete" 
              class="text-red-500 hover:text-red-600"
            >
              삭제
            </button>
          </div>
        </div>
      </div>

      <!-- Post Content -->
      <div class="py-6 min-h-[200px] whitespace-pre-wrap">
        {{ post.content }}
      </div>

      <!-- Comments Section -->
      <div class="border-t pt-6">
        <h2 class="text-xl font-bold mb-4">댓글 {{ comments.length }}개</h2>
        
        <!-- Comment Form -->
        <div class="mb-6">
          <textarea
            v-model="newComment"
            placeholder="댓글을 입력하세요"
            class="w-full border rounded p-2 min-h-[100px]"
          ></textarea>
          <div class="flex justify-end mt-2">
            <button 
              @click="submitComment"
              class="bg-[#699BF7] text-white px-4 py-2 rounded hover:bg-[#5b8ce6]"
            >
              댓글 작성
            </button>
          </div>
        </div>

        <!-- Comments List -->
        <div class="space-y-4">
          <div 
            v-for="comment in comments" 
            :key="comment.id"
            class="border-b last:border-b-0 pb-4"
          >
            <div class="flex justify-between mb-2">
              <div class="font-bold">{{ comment.author }}</div>
              <div class="text-gray-600 text-sm">
                {{ formatDate(comment.createdAt) }}
                <button 
                  v-if="comment.isAuthor"
                  @click="deleteComment(comment.id)"
                  class="ml-2 text-red-500 hover:text-red-600"
                >
                  삭제
                </button>
              </div>
            </div>
            <div class="text-gray-700">{{ comment.content }}</div>
          </div>
        </div>
      </div>

      <!-- Navigation Buttons -->
      <div class="flex justify-between mt-6 pt-4 border-t">
        <button 
          @click="router.push('/article')"
          class="px-4 py-2 border rounded hover:bg-gray-100"
        >
          목록으로
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter, useRoute } from 'vue-router'

const router = useRouter()
const route = useRoute()
const newComment = ref('')

// Sample data - replace with actual API calls
const post = ref({
  id: 1,
  title: '게시글 제목입니다',
  content: '게시글 내용입니다...',
  author: '홍길동',
  createdAt: '2024-03-21',
  views: 15,
})

const comments = ref([
  {
    id: 1,
    content: '댓글 내용입니다',
    author: '김철수',
    createdAt: '2024-03-21',
    isAuthor: true
  }
])

const isAuthor = ref(true) // Replace with actual auth check

const formatDate = (date) => {
  return new Date(date).toLocaleDateString()
}

const handleEdit = () => {
  router.push(`/board/edit/${post.value.id}`)
}

const handleDelete = async () => {
  if (confirm('정말 삭제하시겠습니까?')) {
    try {
      // Delete API call
      router.push('/board')
    } catch (error) {
      console.error('Error deleting post:', error)
    }
  }
}

const submitComment = async () => {
  try {
    // Comment submission logic
    comments.value.push({
      id: Date.now(),
      content: newComment.value,
      author: '현재 사용자',
      createdAt: new Date().toISOString(),
      isAuthor: true
    })
    newComment.value = ''
  } catch (error) {
    console.error('Error submitting comment:', error)
  }
}

const deleteComment = async (commentId) => {
  if (confirm('댓글을 삭제하시겠습니까?')) {
    try {
      // Delete comment API call
      comments.value = comments.value.filter(c => c.id !== commentId)
    } catch (error) {
      console.error('Error deleting comment:', error)
    }
  }
}

onMounted(async () => {
  // Fetch post and comments data
})
</script>