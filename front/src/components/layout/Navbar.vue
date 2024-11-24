<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import LoginModal from '../auth/LoginModal.vue';

const props = defineProps({
  isLoggedIn: Boolean
});

const emit = defineEmits(['logout']);
const router = useRouter();

const isOpen = ref(false);
const showLoginModal = ref(false);
const showRegisterModal = ref(false);
const menuItems = [
  { name: '근처 은행 찾기', link: '/find-bank' },
  { name: '금리 비교', link: '/RateComparator' },
  { name: '게시판', link: '/article' },
  { name: '고객센터', link: '/customer-service' }
];

const toggleMenu = () => {
  isOpen.value = !isOpen.value;
};

const closeMenu = () => {
  isOpen.value = false;
};

const handleLogout = () => {
  emit('logout');
};

const handleRegister = () => {
  showLoginModal.value = false;
  router.push('/register');
};
</script>

<template>
  <div>
    <nav class="bg-[#699BF7] px-6 py-4 flex justify-between items-center fixed w-full top-0 z-20">
      <router-link to="/" class="text-[#FFC700] text-2xl font-bold hover:text-yellow-300">
        Money Mate
      </router-link>
      <div class="flex items-center gap-4">
        <button v-if="isLoggedIn" @click="handleLogout" class="text-white hover:text-[#FFC700] transition-colors duration-200">
          Logout
        </button>
        <button v-else @click="showLoginModal = true" class="text-white hover:text-[#FFC700] transition-colors duration-200">
          Login
        </button>
        <button @click="router.push('/profile')" class="text-white hover:text-[#FFC700] transition-colors duration-200">
          My Profile
        </button>
        <button @click="toggleMenu" class="text-white hover:text-[#FFC700] transition-colors duration-200 px-4 py-2 rounded">
          Menu
        </button>
      </div>
    </nav>

    <div v-if="isOpen" class="fixed w-full bg-[#8CB3FA] top-16 z-10 transition-all duration-300 ease-in-out">
      <div class="py-4">
        <router-link
          v-for="(item, index) in menuItems"
          :key="index"
          :to="item.link"
          @click="closeMenu"
          class="block py-3 text-white text-center hover:bg-[#699BF7] hover:text-[#FFC700] transition-colors duration-200"
        >
          {{ item.name }}
        </router-link>
      </div>
    </div>

    <LoginModal
      :is-open="showLoginModal"
      @close="showLoginModal = false"
      @register="handleRegister"
    />
  </div>
</template>