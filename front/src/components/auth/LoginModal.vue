<script setup>
import { ref } from 'vue';
import { useAuthStore } from '@/stores/authStore';
import { useRouter } from 'vue-router';  // 추가

const router = useRouter();  // 추가
const props = defineProps({
  isOpen: Boolean
});

const emit = defineEmits(['close']);  // register emit 제거

const currentTab = ref('Login');
const loginForm = ref({
  username: '',
  password: ''
});

const authStore = useAuthStore();

const closeModal = () => {
  emit('close');
};

const handleLogin = () => {
  authStore.logIn(loginForm.value);
  closeModal();
};

// Register 탭 클릭 시 register 페이지로 이동
const handleRegisterClick = () => {
  closeModal();
  router.push('/register');
};
</script>

<template>
  <div v-if="isOpen" class="fixed inset-0 z-50 overflow-y-auto">
    <div class="flex items-center justify-center min-h-screen">
      <div class="fixed inset-0 bg-black opacity-50" @click="closeModal"></div>
      <div class="relative bg-white rounded-lg w-full max-w-md p-6">
        <div class="flex border-b mb-6">
          <button
            class="px-4 py-2 border-b-2 border-[#699BF7] text-[#699BF7]"
          >
            로그인
          </button>
          <button
            @click="handleRegisterClick"
            class="px-4 py-2 text-gray-500 hover:text-[#699BF7]"
          >
            회원가입
          </button>
        </div>

        <form @submit.prevent="handleLogin" class="space-y-4">
          <div>
            <label class="block text-sm font-medium text-gray-700">아이디</label>
            <input
              type="text"
              v-model="loginForm.username"
              class="mt-1 block w-full rounded-md border border-gray-300 p-2"
            />
          </div>
          <div>
            <label class="block text-sm font-medium text-gray-700">비밀번호</label>
            <input
              type="password"
              v-model="loginForm.password"
              class="mt-1 block w-full rounded-md border border-gray-300 p-2"
            />
          </div>
          <button type="submit" class="w-full bg-[#699BF7] text-white py-2 rounded-md hover:bg-blue-600">
            로그인
          </button>
        </form>
      </div>
    </div>
  </div>
</template>