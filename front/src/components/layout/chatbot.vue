<!-- src/components/layout/ChatBot.vue -->
<template>
  <div class="fixed bottom-6 right-6">
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

    <div v-if="isOpen" 
      class="absolute bottom-20 right-0 w-96 bg-white rounded-lg shadow-xl"
    >
      <div class="p-4 border-b">
        <h3 class="text-lg font-semibold">Chat with us</h3>
      </div>
      <div class="h-96 p-4 overflow-y-auto">
        <!-- Chat messages will go here -->
      </div>
      <div class="p-4 border-t">
        <input 
          type="text" 
          placeholder="Type a message..." 
          class="w-full px-3 py-2 border rounded-lg"
        >
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const isOpen = ref(false)
</script>