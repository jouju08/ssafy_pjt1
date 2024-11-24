<script setup>
import { ref, computed, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import { useAuthStore } from '@/stores/authStore';
import Navbar from '@/components/layout/Navbar.vue';
import ChatBot from '@/components/layout/ChatBot.vue';
import RegisterPage from '@/views/RegisterPage.vue';

const router = useRouter();
const authStore = useAuthStore();

// computed 속성으로 인증 상태 관리
const isLoggedIn = computed(() => authStore.isAuthenticated);

const handleLogout = () => {
  authStore.logOut();
  router.push('/');
};

// 컴포넌트 마운트 시 토큰 확인
onMounted(() => {
  authStore.getTokenFromCookie();
});
</script>

<template>
  <div>
    <Navbar :is-logged-in="isLoggedIn" @logout="handleLogout" />
    <main class="pt-16">
      <router-view></router-view>
    </main>
    <ChatBot />
  </div>
</template>