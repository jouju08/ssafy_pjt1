<!-- src/components/ProductDetailsModal.vue -->
<template>
  <div class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
    <div class="bg-white rounded-lg max-w-2xl w-full mx-4 p-6">
      <!-- Header -->
      <div class="flex justify-between items-center mb-6">
        <div>
          <h3 class="text-xl font-bold">{{ product.productName }}</h3>
          <p class="text-gray-500 text-sm mt-1">{{ product.bankName }}</p>
        </div>
        <button @click="$emit('close')" class="text-gray-500 hover:text-gray-700">
          <span class="text-2xl">×</span>
        </button>
      </div>
      
      <!-- Content -->
      <div class="space-y-6">
        <!-- 기본 정보 -->
        <div class="grid grid-cols-2 gap-6">
          <div>
            <h4 class="font-medium text-gray-600 mb-2">가입 정보</h4>
            <div class="bg-gray-50 p-4 rounded">
              <div class="space-y-2">
                <div>
                  <span class="text-sm text-gray-500">가입 방법</span>
                  <p>{{ product.joinWay || '정보 없음' }}</p>
                </div>
                <div>
                  <span class="text-sm text-gray-500">가입 대상</span>
                  <p>{{ product.joinMember || '제한 없음' }}</p>
                </div>
              </div>
            </div>
          </div>

          <div>
            <h4 class="font-medium text-gray-600 mb-2">금리 정보</h4>
            <div class="bg-gray-50 p-4 rounded">
              <div class="space-y-2">
                <div>
                  <span class="text-sm text-gray-500">기본금리</span>
                  <p class="text-lg font-bold">{{ product.basicRate }}%</p>
                </div>
                <div>
                  <span class="text-sm text-gray-500">최고금리</span>
                  <p class="text-lg font-bold text-[#699BF7]">{{ product.maxRate }}%</p>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- 우대금리 옵션 -->
        <div v-if="options.length > 0">
          <h4 class="font-medium text-gray-600 mb-3">우대금리 조건</h4>
          <div class="space-y-3">
            <div 
              v-for="option in options" 
              :key="option.id"
              class="bg-gray-50 p-4 rounded"
            >
              <div class="flex justify-between items-start">
                <div class="flex-1">
                  <p class="font-medium">{{ option.intr_rate_type_nm }}</p>
                  <p class="text-sm text-gray-500 mt-1">
                    가입기간: {{ option.save_trm }}개월
                  </p>
                </div>
                <div class="ml-4 text-right">
                  <span class="text-sm text-gray-500">우대금리</span>
                  <p class="font-bold text-[#699BF7]">
                    {{ option.intr_rate2 }}%
                  </p>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- 기타 유의사항 -->
        <div v-if="product.etcNote">
          <h4 class="font-medium text-gray-600 mb-2">유의사항</h4>
          <div class="bg-gray-50 p-4 rounded">
            <p class="text-sm text-gray-600 whitespace-pre-line">{{ product.etcNote }}</p>
          </div>
        </div>
      </div>

      <!-- Footer -->
      <div class="mt-6 flex justify-end gap-3">
        <button 
          @click="$emit('close')"
          class="px-4 py-2 border rounded-lg hover:bg-gray-50"
        >
          닫기
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useFinanceStore } from '../stores/finance'

const store = useFinanceStore()
const options = ref([])

const props = defineProps({
  product: {
    type: Object,
    required: true
  }
})

onMounted(async () => {
  try {
    const data = await store.fetchProductOptions(props.product.id)
    options.value = data
  } catch (error) {
    console.error('Error fetching product options:', error)
  }
})

defineEmits(['close'])
</script>