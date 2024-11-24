<template>
  <div>
    <p class="text-lg mb-4">{{ question.text }}</p>
    <div class="space-y-3">
      <button
        v-for="(choice, index) in question.choices"
        :key="index"
        @click="$emit('answer', choice.points)"
        class="block w-full bg-gray-100 px-4 py-2 rounded hover:bg-gray-200 transition"
      >
        {{ choice.text }}
      </button>
    </div>
  </div>
</template>

<script setup>
defineProps({
  question: Object,
});
</script>
