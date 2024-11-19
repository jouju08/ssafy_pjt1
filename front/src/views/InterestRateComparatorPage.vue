<template>
  <div class="interest-rate-comparator">
    <!-- 필터링 조건 -->
    <div class="filters">
      <div class="filter-group">
        <label for="bank">은행 선택</label>
        <select v-model="selectedBank" id="bank">
          <option value="">모든 은행</option>
          <option v-for="bank in banks" :key="bank" :value="bank">{{ bank }}</option>
        </select>
      </div>
      
      <div class="filter-group">
        <label for="productType">상품 선택</label>
        <select v-model="selectedProduct" id="productType">
          <option value="savings">예금</option>
          <option value="deposit">적금</option>
        </select>
      </div>
      
      <div class="filter-group">
        <label for="minRate">최소 금리</label>
        <input type="number" v-model="minRate" id="minRate" placeholder="최소 금리 입력" />
      </div>
      
      <div class="filter-group">
        <label for="term">만기 기간</label>
        <select v-model="selectedTerm" id="term">
          <option value="6">6개월</option>
          <option value="12">12개월</option>
          <option value="24">24개월</option>
        </select>
      </div>
    </div>
    
    <!-- 금리 비교 테이블 -->
    <div class="rate-table">
      <table>
        <thead>
          <tr>
            <th>은행</th>
            <th>상품</th>
            <th>금리</th>
            <th>만기 기간</th>
          </tr>
        </thead>
        <tbody>
          <!-- 필터링된 금리 데이터 출력 -->
          <tr v-for="(item, index) in filteredRates" :key="index">
            <td>{{ item.bank }}</td>
            <td>{{ item.product }}</td>
            <td>{{ item.rate }}%</td>
            <td>{{ item.term }}개월</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue';

// 초기 데이터 예시
const banks = ['국민은행', '신한은행', '우리은행', '하나은행'];

const rates = [
  { bank: '국민은행', product: '예금', rate: 3.5, term: 6 },
  { bank: '국민은행', product: '적금', rate: 4.0, term: 12 },
  { bank: '신한은행', product: '예금', rate: 3.2, term: 12 },
  { bank: '우리은행', product: '적금', rate: 4.2, term: 24 },
  { bank: '하나은행', product: '예금', rate: 3.7, term: 6 },
  { bank: '하나은행', product: '적금', rate: 4.1, term: 24 },
];

const selectedBank = ref('');
const selectedProduct = ref('savings');
const minRate = ref(null);  // 금리 최소값 초기화
const selectedTerm = ref('6');

// 필터된 금리 데이터 계산
const filteredRates = computed(() => {
  console.log('Filtering with:', {
    selectedBank: selectedBank.value,
    selectedProduct: selectedProduct.value,
    minRate: minRate.value,
    selectedTerm: selectedTerm.value
  });

  const filteredData = rates.filter(item => {
    console.log('Checking item:', item);

    // 필터링 조건 개선
    return (
      (selectedBank.value ? item.bank === selectedBank.value : true) &&  // 은행 필터링
      item.product === selectedProduct.value &&  // 상품 필터링
      (minRate.value !== null ? item.rate >= minRate.value : true) &&  // 최소 금리 필터링
      item.term === parseInt(selectedTerm.value)  // 만기 기간 필터링 (숫자 비교)
    );
  });

  console.log('Filtered Data:', filteredData);

  // 금리 높은 순으로 정렬
  const sortedData = filteredData.sort((a, b) => b.rate - a.rate);

  console.log('Sorted Filtered Rates:', sortedData);

  // 필터링된 데이터가 없으면 모든 데이터를 반환
  return sortedData.length > 0 ? sortedData : rates.sort((a, b) => b.rate - a.rate);
});
</script>

<style scoped>
/* 필터 영역 */
.filters {
  display: flex;
  justify-content: center;  /* 가운데 정렬 */
  gap: 20px;
  margin-bottom: 20px;
  flex-wrap: wrap; /* 작은 화면에서도 잘 보이도록 wrap 추가 */
}

.filter-group {
  display: flex;
  flex-direction: column;
  align-items: center;  /* 라벨과 입력 필드를 수평 가운데 정렬 */
}

label {
  margin-bottom: 8px;
  text-align: center;
}

select, input {
  padding: 8px;
  font-size: 14px;
  border-radius: 4px;
  border: 1px solid #ccc;
  width: 150px;  /* 입력 필드 크기 일관성 유지 */
}

/* 테이블 스타일 */
.rate-table table {
  width: 100%;
  border-collapse: collapse;
}

.rate-table th,
.rate-table td {
  padding: 12px;
  text-align: center;
  border-bottom: 1px solid #ddd; /* 밑줄만 추가 */
}

.rate-table th {
  background-color: #f7f7f7;
  font-weight: bold;
}

.rate-table tr:hover {
  background-color: #f1f1f1;
}
</style>
