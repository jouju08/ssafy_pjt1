<!-- src/App.vue -->
<template>
  <div>
    <Navbar />
    <main class="pt-16"> <!-- Add padding-top to account for fixed navbar -->
      <router-view></router-view>
    </main>
    <ChatBot />
  </div>
</template>

<script setup>
import Navbar from '@/components/layout/Navbar.vue'
import ChatBot from '@/components/layout/ChatBot.vue'
</script>