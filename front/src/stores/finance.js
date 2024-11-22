// src/stores/finance.js
import { defineStore } from 'pinia'
import axios from 'axios'

export const useFinanceStore = defineStore('finance', {
  state: () => ({
    banks: [],
    products: [],
    selectedProduct: null,
    productOptions: [],
    loading: false,
    error: null
  }),

  getters: {
    sortedProducts: (state) => {
      return [...state.products].sort((a, b) => b.maxRate - a.maxRate)
    },
  },

  actions: {
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
        const response = await axios.get('http://localhost:8000/finlife/deposit-products/')
        this.products = response.data.map(item => ({
          id: item.fin_prdt_cd,
          bankName: item.kor_co_nm,
          productName: item.fin_prdt_nm,
          basicRate: parseFloat(item.intr_rate || 0),
          maxRate: parseFloat(item.intr_rate2 || 0),
          period: parseInt(item.save_trm || 0),
          joinWay: item.join_way,
          joinMember: item.join_member,
          etcNote: item.etc_note
        }))
      } catch (error) {
        this.error = '상품 정보를 불러오는데 실패했습니다.'
        console.error('Error fetching products:', error)
      } finally {
        this.loading = false
      }
    },

    async fetchProductOptions(productId) {
      try {
        const response = await axios.get(`http://localhost:8000/finlife/deposit-products-options/${productId}/`)
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
        (!period || product.period === parseInt(period))
      )
    }
  }
})