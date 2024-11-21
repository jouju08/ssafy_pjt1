<template>
  <div id="app">
    <Navbar @showLoginModal="openLoginModal" /> <!-- 네비게이션 바에서 이벤트 받아옴 -->

    <div id='main'>
      <RouterView /> <!-- 현재 페이지에 맞는 콘텐츠가 여기에 렌더링됨 -->
    </div>

    <!-- 로그인 모달 컴포넌트 추가 -->
    <LoginModal ref="loginModal" />
    <nav>
      <RouterLink :to="{name: 'ArticleView'}">Articles</RouterLink>
    </nav>
  </div>
</template>

<script setup>
import Navbar from "@/components/Navbar.vue";
import LoginModal from "@/components/LoginModal.vue"; // 로그인 모달 컴포넌트
import { ref } from 'vue';
import { RouterLink } from "vue-router";
import ArticleView from "./views/ArticleView.vue";

// 로그인 모달 컴포넌트 참조
const loginModal = ref(null);

// 네비게이션 바에서 로그인 버튼 클릭 시 모달 열기
const openLoginModal = () => {
  loginModal.value.openModal();
};
</script>

<style>
/* App.vue의 스타일 */
#app {
  font-family: 'Arial', sans-serif;
  background-color: #f8f9fa; /* 배경 색상 */
  min-height: 100vh; /* 화면 최소 높이를 100%로 설정 */
  display: flex;
  flex-direction: column;
}

/* header는 네비게이션 바가 들어가는 곳 */
header {
  position: sticky; /* 상단에 고정 */
  top: 0;
  z-index: 1050;
  width: 100%;
  background-color: white; /* 배경색 설정 */
}

/* main 영역에 RouterView를 배치 */
#main {
  padding-top: 120px; /* 네비게이션 바 높이에 맞춰 여백 설정 */
  flex: 1; /* 남은 공간을 모두 차지하도록 설정 */
}

/* 미디어 쿼리로 반응형 처리 */
@media (max-width: 768px) {
  #main {
    padding-top: 120px; /* 모바일에서는 약간의 여백을 더 설정 */
  }
}

@media (max-width: 216px) {
  #main {
    padding-top: 55px; /* 더 작은 화면에서는 여백을 줄임 */
  }
}
</style>
