<template>
  <div class="container mx-auto px-4 py-8">
    <!-- 프로필 섹션 -->
    <div class="bg-white rounded-lg shadow-md p-6 flex flex-col items-center">
      <!-- 프로필 이미지 -->
      <img 
        :src="profileImageUrl" 
        alt="프로필 이미지"
        class="w-24 h-24 rounded-full mb-4"
      />
      <!-- 사용자 정보 -->
      <div class="text-center">
        <p class="text-lg font-semibold">{{ username }}</p>
        <p class="text-gray-600">주거래 은행: {{ mainBank }}</p>
        <p class="text-gray-600">가입한 예적금 목록:</p>
        <ul class="text-gray-700">
          <li v-for="product in subscribedProducts" :key="product.id">
            - {{ product.name }}
          </li>
        </ul>
      </div>
      <!-- 수정하기 버튼 -->
      <button 
        @click="navigateToEdit"
        class="mt-4 bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600"
      >
        수정하기
      </button>
    </div>
    <!-- 나의 투자 성향 섹션 -->
    <div class="mt-8 bg-white rounded-lg shadow-md p-6">
      <h2 class="text-xl font-bold mb-4">나의 투자성향은?</h2>
      <div v-if="investmentStyle">
        <p class="text-gray-700">당신의 투자 성향: {{ investmentStyle }}</p>
      </div>
      <div v-else>
        <p class="text-gray-600 mb-4">투자 성향을 파악해보세요.</p>
        <button 
          @click="showSurveyModal = true"
          class="bg-green-500 text-white px-4 py-2 rounded hover:bg-green-600"
        >
          투자 성향 파악하기
        </button>
      </div>
    </div>
    <!-- Survey Modal -->
    <SurveyModal v-if="showSurveyModal" />
    <SurveyResultModal />
  </div>
</template>

<script setup>
import { ref } from 'vue';
import SurveyModal from '@/components/survey/SurveyModal.vue';
import SurveyResultModal from '@/components/survey/resultModal.vue';

const profileImageUrl = ref('https://via.placeholder.com/150');
const username = ref('홍길동');
const mainBank = ref('국민은행');
const subscribedProducts = ref([
  { id: 1, name: '정기 예금 1년 만기' },
  { id: 2, name: '적금 6개월 만기' }
]);
const investmentStyle = ref('');
const showSurveyModal = ref(false);

const navigateToEdit = () => {
  console.log('Edit Profile');
};
</script>
