<template>
  <header>
    <!-- 상단 네비게이션 (프로필, 마이데이터) -->
    <div v-show="showTopBar" class="top-bar bg-light py-2 border-bottom">
      <div class="container d-flex justify-content-end">
        <router-link to="/profile" class="nav-link">프로필</router-link>
        <router-link to="/my-data" class="nav-link">마이데이터</router-link>
      </div>
    </div>

    <!-- 고정된 네비게이션 바 -->
    <nav class="navbar navbar-expand-lg navbar-light bg-white shadow-sm" :class="{ 'fixed-nav': !showTopBar }">
      <div class="container">
        <a class="navbar-brand" href="#">LOGO</a>
        <div class="d-flex">
          <button class="btn btn-primary me-2" @click="openLoginModal">로그인</button>
          <button class="btn btn-outline-secondary" @click="toggleDropdown">☰</button>
        </div>
      </div>
    </nav>
  </header>
</template>

<script>
import { ref, onMounted, onUnmounted } from "vue";

export default {
  setup(props, { emit }) {
    const showTopBar = ref(true);

    const handleScroll = () => {
      showTopBar.value = window.scrollY === 0;
    };

    onMounted(() => window.addEventListener("scroll", handleScroll));
    onUnmounted(() => window.removeEventListener("scroll", handleScroll));

    const openLoginModal = () => {
      emit("showLoginModal"); // 부모에게 모달 열기 요청
    };

    const toggleDropdown = () => alert("드롭다운 버튼 클릭");

    return {
      showTopBar,
      openLoginModal,
      toggleDropdown,
    };
  },
};
</script>

<style scoped>
/* 상단 바 */
.top-bar {
  position: fixed;
  top: 0;
  width: 100%;
  z-index: 1050;
  background-color: #f8f9fa;
  transition: opacity 0.3s ease, transform 0.3s ease;
  width: 100%;
}

/* 네비게이션 바 */
.navbar {
  position: fixed;
  width: 100%;
  top: 40px; /* 상단 바의 기본 높이와 맞추기 */
  z-index: 1040;
  transition: top 0.3s ease;
}

/* 스크롤 시 네비게이션 바가 상단으로 이동 */
.fixed-nav {
  top: 0;
  z-index: 1050;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); /* 고정 시 그림자 효과 */
}

/* 전역 스타일 */
html,
body {
  margin: 0;
  padding: 0;
  font-family: Arial, sans-serif;
  padding-top: 50px; /* 네비게이션 바 공간 확보 */
}
</style>
