<!-- src/components/layout/Navbar.vue -->
<template>
  <div>
    <nav class="bg-[#699BF7] px-6 py-4 flex justify-between items-center fixed w-full top-0 z-20">
      <router-link to="/" class="text-[#FFC700] text-2xl font-bold hover:text-yellow-300">
        Money Mate
      </router-link>
      
      <div class="flex items-center gap-4">
        <button 
          @click="showLoginModal = true"
          class="text-white hover:text-[#FFC700] transition-colors duration-200"
        >
          Login
        </button>
        <button class="text-white hover:text-[#FFC700] transition-colors duration-200">
          My Profile
        </button>
        
        <button 
          @click="isOpen = !isOpen"
          class="text-white hover:text-[#FFC700] transition-colors duration-200 px-4 py-2 rounded"
        >
          Menu
        </button>
      </div>
    </nav>

    <!-- Full-width dropdown menu -->
    <div 
      v-if="isOpen" 
      class="fixed w-full bg-[#8CB3FA] top-16 z-10 transition-all duration-300 ease-in-out"
    >
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

    <!-- Login Modal -->
    <LoginModal 
      :is-open="showLoginModal"
      @close="showLoginModal = false"
    />
  </div>
</template>

<script setup>
import { ref } from 'vue'
import LoginModal from '../auth/LoginModal.vue'

const isOpen = ref(false)
const showLoginModal = ref(false)
const menuItems = ref([
  { name: '근처 은행 찾기', link: '/find-bank' },
  { name: '금리 비교', link: '/RateComparator' },
  { name: '게시판', link: '/article' },
  { name: '고객센터', link: '/customer-service' },
])

// 드롭다운 메뉴 열기/닫기
const toggleMenu = () => {
  isOpen.value = !isOpen.value
}

// 드롭다운 메뉴 닫기
const closeMenu = () => {
  isOpen.value = false
}
</script>