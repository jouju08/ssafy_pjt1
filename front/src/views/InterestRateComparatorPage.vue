<template>
  <div class="interest-rate-comparator">
    <!-- 필터링 조건 -->
    <div class="filters">
      <div class="filter-group">
        <label for="bank">은행 선택</label>
        <select v-model="selectedBank" id="bank">
          <option value="">모든 은행</option>
          <option v-for="bank in depositProducts.kor_co_nm" :key="bank" :value="bank">{{ bank }}</option>
        </select>
      </div>
      
      <div class="filter-group">
        <label for="productType">상품 선택</label>
        <select v-model="selectedProduct" id="productType">
          <option value="예금">예금</option>
          <option value="적금">적금</option>
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
            <th>상품명</th>
            <th>기본 금리</th>
            <th>최소 가입기간</th>
            <th>유형</th>
          </tr>
        </thead>
        <tbody>
          <!-- 필터링된 금리 데이터 출력 -->
          <tr v-for="(item, index) in filteredRates" :key="index">
            <td>{{ item.bank }}</td>
            <td>{{ item.fin_prdt_nm }}</td>
            <td>{{ item.rate }}%</td>
            <td>{{ item.term }}개월</td>
            <td>{{ item.product }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script setup>
import { computed, onMounted } from 'vue';
import { useRateComparatorStore } from '@/stores/RateComparatorStore';

const store = useRateComparatorStore()

// 예금 상품 데이터를 computed로 가져오기
const depositProducts = computed(() => store.getDepositProducts);

// 컴포넌트가 마운트되면 데이터를 가져오기
onMounted(async () => {
  await store.fetchDepositProducts(); // 비동기 데이터 fetch
  console.log(depositProducts.value); // 데이터가 로드된 후 출력
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
