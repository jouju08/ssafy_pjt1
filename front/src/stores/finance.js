// src/stores/finance.js
import { defineStore } from 'pinia'
import axios from 'axios'

export const useFinanceStore = defineStore('finance', {
  state: () => ({
    banks: [],
    products: [],
    selectedProduct: null,
    productOptions: [],
    Rates:[],
    loading: false,
    error: null
  }),

  getters: {
    sortedProducts: (state) => {
      return [...state.products].sort((a, b) => b.maxRate - a.maxRate)
    },
  },

  actions: {
    async findRates(productId) {
      try {
        const response = await axios.get(`http://localhost:8000/finlife/${productId}/top_rate_month/`)
        console.log(response)
        this.rates_months = {
          maxRate: response.data.max_rate,
          minRate: response.data.min_rate,
          minMonth:response.data.min_month,
          maxMonth:response.data.max_month,
        }
        return this.rates_months
      } catch (error) {
        this.error = '은행 목록을 불러오는데 실패했습니다.'
        console.error('Error fetching banks:', error)
      }
    },

    async fetchBanks() {
      try {
        const response = await axios.get('http://localhost:8000/finlife/getBankName/')
        this.banks = response.data.map(bankName => ({
          code: bankName,
          name: bankName
        }))
      } catch (error) {
        this.error = '은행 목록을 불러오는데 실패했습니다.'
        console.error('Error fetching banks:', error)
      }
    },

    async fetchProducts() {
      this.loading = true
      try {
        // 1. 상품 목록 가져오기
        const response = await axios.get('http://localhost:8000/finlife/deposit-products/')
        const products = response.data
        
        // 2. 각 상품에 대해 추가 정보를 가져오기
        const productsWithDetails = await Promise.all(products.map(async (item) => {
          // 첫 번째 API로부터 상품 기본 정보 가져오기
          const product = {
            id: item.fin_prdt_cd,
            bankName: item.kor_co_nm,
            productName: item.fin_prdt_nm,
            joinWay: item.join_way,
            joinMember: item.join_member,
            etcNote: item.etc_note,
            joinDeny: item.join_deny,
            spclCnd: item.spcl_cnd,  // `spcl_cnd` 필드는 두 번째 API에서 가져옴
          }
    
          // 3. 각 상품에 대해 두 번째 API 호출하여 추가 정보 가져오기
          try {
            const optionResponse = await axios.get(`http://localhost:8000/finlife/${item.fin_prdt_cd}/top_rate_month/`)
            console.log('옵션 응답',optionResponse.data)
            product.maxRate = parseFloat(optionResponse.data.max_rate || 0),
            product.minRate = parseFloat(optionResponse.data.min_rate || 0),
            product.maxMRate = parseFloat(optionResponse.data.max_Mrate || 0),
            product.maxMonth = parseFloat(optionResponse.data.max_month || 0),
            product.minMonth = parseFloat(optionResponse.data.min_month || 0)
          } catch (error) {
            console.error(`Error fetching options for product ${item.fin_prdt_cd}:`, error)
            product.spclCnd = '정보 없음';  // 옵션 정보가 없으면 기본값으로 설정
          }
          console.log(product)
          return product
        }))
    
        // 4. 최종 상품 데이터 업데이트
        this.products = productsWithDetails
    
      } catch (error) {
        this.error = '상품 정보를 불러오는데 실패했습니다.'
        console.error('Error fetching products:', error)
      } finally {
        this.loading = false
      }
    },

    async fetchProductOptions(productId) {
      try {
        const response = await axios.get(`http://localhost:8000/finlife/${productId}/deposit-products-options/`)
        this.productOptions = response.data
        return response.data
      } catch (error) {
        this.error = '상품 옵션을 불러오는데 실패했습니다.'
        console.error('Error fetching product options:', error)
      }
    },

    setSelectedProduct(product) {
      this.selectedProduct = product
    },

    clearSelectedProduct() {
      this.selectedProduct = null
    },

    filterProducts(bankCode, period) {
      return this.products.filter(product => 
        (!bankCode || product.bankName === bankCode) &&
        (!period || product.minMonth <= parseInt(period)&&product.maxMonth>=parseInt(period))
      )
    }
  }
})