import { ref } from 'vue';
import { defineStore } from 'pinia';
import axios from 'axios';

export const useRateComparatorStore = defineStore('rateComparator', {
  
  state: () => ({
    depositProducts: [], // 예금 상품 데이터를 저장할 배열
  }),

  actions: {
    // 예금 상품 데이터를 가져오는 비동기 액션
    async fetchDepositProducts() {
      try {
        const response = await axios.get('http://localhost:8000/finlife/deposit-products/');
        this.depositProducts = response.data; // 상태 업데이트
      } catch (error) {
        console.error('Failed to fetch deposit products:', error);
      }
    },
  },

  getters: {
    // 예금 상품 데이터를 반환하는 getter
    getDepositProducts: (state) => state.depositProducts,
  },
});
