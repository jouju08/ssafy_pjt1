import { fileURLToPath, URL } from 'node:url'
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import vueDevTools from 'vite-plugin-vue-devtools'

export default defineConfig({
  plugins: [
    vue(),
    vueDevTools(),
  ],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    },
  },
  server: {
    proxy: {
      '/api/chart': {
        target: 'https://api.stock.naver.com', // 실제 API 서버 주소
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\/api\/chart/, '/chart'), // '/api/chart'를 '/chart'로 바꿔서 실제 API 경로로 리다이렉트
      },
      // /api로 시작하는 모든 요청을 m.stock.naver.com API로 프록시
      '/api': {
        target: 'https://m.stock.naver.com',
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\/api/, ''), // '/api'를 제거하고 실제 API 경로로 리다이렉션
      },
      
    },
  },
})