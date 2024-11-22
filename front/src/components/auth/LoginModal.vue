<!-- src/components/auth/LoginModal.vue -->
<template>
  <div v-if="isOpen" class="fixed inset-0 z-50 overflow-y-auto">
    <div class="flex items-center justify-center min-h-screen">
      <!-- Backdrop -->
      <div class="fixed inset-0 bg-black opacity-50" @click="closeModal"></div>
      
      <!-- Modal -->
      <div class="relative bg-white rounded-lg w-full max-w-md p-6">
        <!-- Tabs -->
        <div class="flex border-b mb-6">
          <button 
            v-for="tab in tabs" 
            :key="tab"
            @click="currentTab = tab"
            :class="[
              'px-4 py-2',
              currentTab === tab ? 'border-b-2 border-[#699BF7] text-[#699BF7]' : 'text-gray-500'
            ]"
          >
            {{ tab }}
          </button>
        </div>

        <!-- Login Form -->
        <form v-if="currentTab === 'Login'" @submit.prevent="handleLogin" class="space-y-4">
          <div>
            <label class="block text-sm font-medium text-gray-700">아이디</label>
            <input 
              type="text" 
              v-model="loginForm.username"
              class="mt-1 block w-full rounded-md border border-gray-300 p-2"
            >
          </div>
          <div>
            <label class="block text-sm font-medium text-gray-700">비밀번호</label>
            <input 
              type="password" 
              v-model="loginForm.password"
              class="mt-1 block w-full rounded-md border border-gray-300 p-2"
            >
          </div>
          <button 
            type="submit"
            class="w-full bg-[#699BF7] text-white py-2 rounded-md hover:bg-blue-600"
          >
            로그인
          </button>
        </form>

        <!-- Register Form -->
        <form v-if="currentTab === 'Register'" @submit.prevent="handleRegister" class="space-y-4">
          <!-- Similar structure to login form with additional fields -->
        </form>

        <!-- Find ID Form -->
        <form v-if="currentTab === 'Find ID'" @submit.prevent="handleFindId" class="space-y-4">
          <!-- Find ID form fields -->
        </form>

        <!-- Find Password Form -->
        <form v-if="currentTab === 'Find Password'" @submit.prevent="handleFindPassword" class="space-y-4">
          <!-- Find password form fields -->
        </form>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const props = defineProps({
  isOpen: Boolean
})

const emit = defineEmits(['close'])

const tabs = ['Login', 'Register', 'Find ID', 'Find Password']
const currentTab = ref('Login')
const loginForm = ref({
  username: '',
  password: ''
})

const closeModal = () => {
  emit('close')
}

const handleLogin = () => {
  // Handle login logic
  console.log('Login:', loginForm.value)
}

const handleRegister = () => {
  // Handle registration logic
}

const handleFindId = () => {
  // Handle find ID logic
}

const handleFindPassword = () => {
  // Handle find password logic
}
</script>