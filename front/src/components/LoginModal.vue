<template>
  <div v-if="isVisible" class="modal fade show" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true" style="display: block;">
    <div class="modal-dialog modal-lg">
      <div class="modal-content">
        <div class="modal-body">
          <h3 class="modal-title">Login</h3>
          <form @submit.prevent="logIn">
            <div class="user-box">
              <input type="text" id="username" required v-model.trim="username" />
              <label>Username</label>
            </div>
            <div class="user-box">
              <input type="password" id="password" required v-model.trim="password" />
              <label>Password</label>
            </div>
            <div class="button-group">
              <input type="submit" class="btn btn-primary" value="로그인" />
              <input type="button" class="btn btn-secondary" value="회원가입" @click="goToSignUp" />
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";
import { useRouter } from "vue-router";
import { useAuthStore } from '@/stores/authStore'

const isVisible = ref(false);
const username = ref('');
const password = ref('');
const router = useRouter();
const store = useAuthStore();  // Pinia store 초기화

// 모달 열기 함수
const openModal = () => {
  isVisible.value = true;
};

// 모달 닫기 함수
const closeModal = () => {
  isVisible.value = false;
};

// 로그인 처리 함수
const logIn = async () => {
  const payload = {
    username: username.value,
    password: password.value
  };

  try {
    // 로그인 요청
    await store.logIn(payload);

    // 로그인 성공 후 모달 닫기
    closeModal();

    // 현재 페이지가 회원가입 페이지이면 메인 페이지로 이동
    if (router.currentRoute.value.path === '/signup') {
      router.push("/"); // 메인 페이지로 이동
    } else {
      // 회원가입 페이지가 아니면 모달만 닫기
      router.go(0); // 페이지 새로 고침
    }

    alert("로그인 성공!");

  } catch (error) {
    console.error("로그인 에러:", error);
    alert("아이디 또는 비밀번호가 일치하지 않습니다.");
  }
};

// 회원가입 페이지로 이동
const goToSignUp = () => {
  closeModal();
  router.push("/signup");
};

// Pinia store에서 모달 제어를 위해 expose
defineExpose({
  openModal,
});
</script>


<style scoped>
/* 모달 오버레이 */
.modal {
  position: fixed;
  top: 0;
  left: 0;
  z-index: 1050;
  width: 100%;
  height: 100%;
  background-color: rgba(169, 169, 169, 0.9); /* 짙은 회색 배경 */
  display: block;
}

/* 모달 다이얼로그 */
.modal-dialog {
  margin: 10% auto; /* 중앙 정렬 */
  max-width: 500px; /* 최대 너비 */
  height: auto; /* 높이 자동 */
  max-height: 80%; /* 최대 높이 제한 (80% 화면 크기) */
}

/* 모달 콘텐츠 높이 조정 */
.modal-content {
  height: 100%; /* 콘텐츠의 높이를 100%로 맞추기 */
  display: flex;
  flex-direction: column;
  padding: 20px;
  background: #878787; /* 어두운 배경 */
}

/* 중앙에 Login 텍스트 */
.modal-body {
  color: white;
  text-align: center;
}

.modal-title {
  font-size: 32px;
  margin-bottom: 30px;
  font-weight: bold;
}

/* 입력 박스 스타일 */
.user-box {
  position: relative;
  margin-bottom: 30px;
}

.user-box input {
  width: 100%;
  padding: 10px 0;
  font-size: 16px;
  color: #fff;
  border: none;
  border-bottom: 1px solid #fff; /* 하단에 흰색 줄 */
  background: transparent;
}

.user-box label {
  position: absolute;
  top: 0;
  left: 0;
  padding: 10px 0;
  font-size: 16px;
  color: #fff;
  pointer-events: none;
  transition: 0.5s;
}

/* 입력값이 있을 때 라벨 위치 */
.user-box input:focus ~ label,
.user-box input:valid ~ label {
  top: -20px;
  left: 0;
  color: #03e9f4;
  font-size: 12px;
}

/* 버튼 그룹 스타일 */
.button-group {
  display: flex;
  justify-content: space-between; /* 로그인, 회원가입 버튼을 양옆에 배치 */
}

input[type="submit"], input[type="button"] {
  width: 48%; /* 버튼 크기를 맞춤 */
  padding: 10px 0;
  font-size: 16px;
  border: none;
  cursor: pointer;
  transition: 0.3s;
}

input[type="submit"] {
  background-color: #03e9f4; /* 로그인 버튼 색상 */
  color: #fff;
}

input[type="button"] {
  background-color: #6c757d; /* 회원가입 버튼 색상 */
  color: #fff;
}

/* 버튼 호버 효과 */
input[type="submit"]:hover {
  background-color: #0294c6; /* 로그인 버튼 호버 색상 */
}

input[type="button"]:hover {
  background-color: #5a6268; /* 회원가입 버튼 호버 색상 */
}

input[type="submit"], input[type="button"] {
  width: 45%; /* 버튼 크기 줄이기 */
  padding: 8px 0; /* 패딩 줄이기 */
  font-size: 14px; /* 글씨 크기 줄이기 */
  border: none;
  cursor: pointer;
  transition: 0.3s;
}
</style>
