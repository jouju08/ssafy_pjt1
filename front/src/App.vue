<script setup>
import { ref, computed, onMounted, onUnmounted } from 'vue';
import { useRouter } from 'vue-router';
import { useAuthStore } from '@/stores/authStore';
import Navbar from '@/components/layout/Navbar.vue';
import ChatBot from './components/layout/chatbot.vue';
import CurrencyConverter from '@/components/layout/CurrencyConverter.vue';

const router = useRouter();
const authStore = useAuthStore();

// 인증 상태 관리
const isLoggedIn = computed(() => authStore.isAuthenticated);

const handleLogout = () => {
  authStore.logOut();
  router.push('/');
};

// 컴포넌트 마운트 시 토큰 확인
onMounted(() => {
  authStore.getTokenFromCookie();
});

// 창 관리 상태
const isChatBotOpen = ref(false);
const isCurrencyConverterOpen = ref(false);

// 창 열기 함수
const openChatBot = () => {
  isChatBotOpen.value = true;
  isCurrencyConverterOpen.value = false;
};

const openCurrencyConverter = () => {
  isCurrencyConverterOpen.value = true;
  isChatBotOpen.value = false;
};

// 외부 클릭 시 창 닫기
const handleOutsideClick = (event) => {
  if (
    !event.target.closest('.chatbot-container') &&
    !event.target.closest('.currency-converter-container') &&
    !event.target.closest('.chatbot-button') &&
    !event.target.closest('.currency-converter-button')
  ) {
    isChatBotOpen.value = false;
    isCurrencyConverterOpen.value = false;
  }
};

onMounted(() => {
  document.addEventListener('click', handleOutsideClick);
});

onUnmounted(() => {
  document.removeEventListener('click', handleOutsideClick);
});
</script>

<template>
  <div>
    <Navbar :is-logged-in="isLoggedIn" @logout="handleLogout" />
    <main class="pt-16">
      <router-view></router-view>
    </main>
    <!-- 버튼들 -->
    <div class="fixed bottom-6 right-6 flex space-x-4">
      <button
        @click.stop="openChatBot"
        class="bg-[#699BF7] p-4 rounded-full shadow-lg hover:bg-blue-500 text-white chatbot-button"
      >
        <svg 
          v-if="!isChatBotOpen"
          class="w-6 h-6"
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
        <svg
          v-else
          xmlns="http://www.w3.org/2000/svg"
          fill="none"
          viewBox="0 0 24 24"
          stroke-width="1.5"
          stroke="currentColor"
          class="w-6 h-6"
        >
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            d="M6 18L18 6M6 6l12 12"
          />
        </svg>
      </button>
      <button
        @click.stop="openCurrencyConverter"
        class="bg-[#699BF7] p-4 rounded-full shadow-lg hover:bg-blue-500 text-white currency-converter-button"
      >
        <svg
          v-if="!isCurrencyConverterOpen"
          xmlns="http://www.w3.org/2000/svg"
          fill="none"
          viewBox="0 0 24 24"
          stroke-width="1.5"
          stroke="currentColor"
          class="w-6 h-6"
        >
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            d="M12 6v6m0 0v6m0-6h6m-6 0H6"
          />
        </svg>
        <svg
          v-else
          xmlns="http://www.w3.org/2000/svg"
          fill="none"
          viewBox="0 24 24"
          stroke-width="1.5"
          stroke="currentColor"
          class="w-6 h-6"
        >
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            d="M6 18L18 6M6 6l12 12"
          />
        </svg>
      </button>
    </div>
    <!-- 컴포넌트들 -->
    <div
      v-if="isChatBotOpen"
      class="fixed bottom-20 right-6 chatbot-container"
    >
      <ChatBot />
    </div>
    <div
      v-if="isCurrencyConverterOpen"
      class="fixed bottom-20 right-6 currency-converter-container"
    >
      <CurrencyConverter />
    </div>
  </div>
</template>
