<template>
  <div class="fixed bottom-6 right-6">
    <!-- 채팅 열기/닫기 버튼 -->
    <button 
      @click="isOpen = !isOpen"
      class="bg-[#699BF7] p-4 rounded-full shadow-lg hover:bg-blue-500"
    >
      <svg 
        class="w-6 h-6 text-white"
        fill="none" 
        stroke="currentColor" 
        viewBox="0 0 24 24"
      >
        <path 
          stroke-linecap="round" 
          stroke-linejoin="round" 
          stroke-width="2" 
          d="M8 10h.01M12 10h.01M16 10h.01M9 16H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-5l-5 5v-5z"
        />
      </svg>
    </button>

    <!-- 채팅 창 -->
    <div v-if="isOpen" 
      class="absolute bottom-20 right-0 w-96 bg-white rounded-lg shadow-xl"
    >
      <!-- 헤더 -->
      <div class="p-4 border-b">
        <h3 class="text-lg font-semibold">Chat with us</h3>
      </div>

      <!-- 채팅 메시지 표시 -->
      <div class="h-96 p-4 overflow-y-auto" ref="chatBox">
        <div v-for="(message, index) in chatbotStore.messages" :key="index">
          <!-- 사용자 메시지 -->
          <div 
            v-if="message.role === 'user'" 
            class="text-right mb-2"
          >
            <div class="inline-block bg-blue-500 text-white px-4 py-2 rounded-lg">
              {{ message.content }}
            </div>
          </div>

          <!-- 챗봇 메시지 -->
          <div 
            v-else-if="message.role === 'system'" 
            class="text-left mb-2"
          >
            <div class="inline-block bg-gray-200 text-black px-4 py-2 rounded-lg">
              {{ message.content }}
            </div>
          </div>
        </div>

        <!-- 로딩 상태 표시 -->
        <div v-if="isLoading" class="text-center text-gray-500">
          Typing...
        </div>
      </div>

      <!-- 입력 필드 -->
      <div class="p-4 border-t flex">
        <input 
          v-model="userInput"
          @keypress.enter="sendMessage"
          type="text" 
          placeholder="Type a message..." 
          class="flex-grow px-3 py-2 border rounded-lg"
        >
        <button 
          @click="sendMessage"
          class="ml-2 bg-[#699BF7] text-white px-4 py-2 rounded hover:bg-blue-500"
        >
          Send
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, nextTick } from 'vue'
import { useChatbotStore } from '@/stores/chatbotStore'

// 상태 관리
const isOpen = ref(false) // 채팅창 열기/닫기 상태
const userInput = ref('') // 사용자 입력 값
const isLoading = ref(false) // 로딩 상태
const chatbotStore = useChatbotStore() // Chatbot Store

// 참조 설정
const chatBox = ref(null) // 채팅창 스크롤 참조

// 메시지 전송 핸들러
const sendMessage = async () => {
  if (!userInput.value.trim()) return // 빈 메시지 방지

  // 사용자 메시지 추가
  chatbotStore.addMessage({ role: 'user', content: userInput.value })
  scrollToBottom() // 스크롤 자동 이동

  // API에 메시지 전송 및 로딩 상태
  isLoading.value = true
  const botResponse = await chatbotStore.sendMessageToAPI(userInput.value)
  chatbotStore.addMessage({ role: 'system,', content: botResponse })
  isLoading.value = false
  scrollToBottom() // 스크롤 자동 이동

  // 입력 필드 초기화
  userInput.value = ''
}

// 스크롤 자동 이동 함수
const scrollToBottom = () => {
  nextTick(() => {
    if (chatBox.value) {
      chatBox.value.scrollTop = chatBox.value.scrollHeight
    }
  })
}

// 채팅창이 열릴 때 스크롤 맨 아래로 이동
onMounted(() => {
  scrollToBottom()
})
</script>

<style>
/* 필요한 추가 스타일 정의 (Tailwind CSS 사용 중이므로 최소화 가능) */
</style>
