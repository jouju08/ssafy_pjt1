<template>
  <div class="signup-container">
    <h1 class="text-center">회원가입</h1>
    <form @submit.prevent="signUp" class="form-container">
      <!-- 아이디 -->
      <div class="form-group">
        <label for="username">아이디</label>
        <div class="input-group">
          <input type="text" id="username" v-model.trim="username" class="form-control" placeholder="4~20자리 / 영문, 숫자, 특수문자 '!'사용가능" required @input="checkUsername">
          <button type="button" class="btn" @click="checkUsernameAvailability" :class="{'btn-secondary': !usernameValid, 'btn-success': usernameValid}" :disabled="!usernameValid">아이디 중복확인</button>
        </div>
        <span v-if="username && usernameChecked" :class="usernameValid ? 'valid-check' : 'invalid-check'">{{ usernameValid ? '✔' : '✖' }}</span>
      </div>

      <!-- 비밀번호 -->
      <div class="form-group">
        <label for="password1">비밀번호</label>
        <input type="password" id="password1" v-model.trim="password1" class="form-control" placeholder="8~16자리/영문 대소문자, 숫자, 특수문자 조합" required>
        <span v-if="password1 && password1Checked" :class="password1Valid ? 'valid-check' : 'invalid-check'">{{ password1Valid ? '✔' : '✖' }}</span>
        <p class="helper-text">8~16자리 영문 대소문자, 숫자, 특수문자 중 3가지 이상 조합으로 만들어주세요.</p>
      </div>

      <!-- 비밀번호 확인 -->
      <div class="form-group">
        <label for="password2">비밀번호 확인</label>
        <input type="password" id="password2" v-model.trim="password2" class="form-control" @input="checkPasswordMatch" required>
        <span v-if="password2 && password2Checked" :class="password2Valid ? 'valid-check' : 'invalid-check'">{{ password2Valid ? '✔' : '✖' }}</span>
        <p class="error-text" v-if="!isPasswordMatch && password2">비밀번호가 일치하지 않습니다.</p>
      </div>

      <!-- 이름 -->
      <div class="form-group">
        <label for="last_name">성</label>
        <input type="text" id="last_name" v-model.trim="last_name" class="form-control" placeholder="성 입력" required>
      </div>

      <div class="form-group">
        <label for="first_name">이름</label>
        <input type="text" id="first_name" v-model.trim="first_name" class="form-control" placeholder="이름 입력" required>
      </div>

      <!-- 생년월일 -->
      <div class="form-group">
        <label for="birth">생년월일</label>
        <input type="date" id="birth" v-model="birth" class="form-control" required>
      </div>

      <!-- 휴대폰 -->
      <div class="form-group">
        <label for="phone">휴대폰</label>
        <div class="input-group">
          <input type="text" id="phone" v-model.trim="phone" class="form-control" placeholder="'-' 빼고 숫자만 입력" required>
        </div>
        <span v-if="phone && phoneChecked" :class="phoneValid ? 'valid-check' : 'invalid-check'">{{ phoneValid ? '✔' : '✖' }}</span>
      </div>

      <!-- 이메일 -->
      <div class="form-group">
        <label for="email">이메일</label>
        <input type="email" id="email" v-model.trim="email" class="form-control" placeholder="email@naver.co.kr" required>
      </div>

      <!-- 주거래 은행 -->
      <div class="form-group">
        <label for="mainBank">주거래 은행</label>
        <input 
          type="text" 
          id="mainBank" 
          v-model.trim="mainBank" 
          class="form-control" 
          placeholder="주거래 은행 입력 또는 선택"
          list="banks" 
          required
        >
        <datalist id="banks">
          <option value="우리은행"></option>
          <option value="신한은행"></option>
          <option value="국민은행"></option>
          <option value="하나은행"></option>
          <option value="카카오뱅크"></option>
          <option value="토스뱅크"></option>
        </datalist>
      </div>

      <!-- 연봉 -->
      <div class="form-group">
        <label for="income">연봉(만원)</label>
        <input type="number" id="income" v-model="income" class="form-control" placeholder="연봉 입력" required>
      </div>

      <!-- 잔고 -->
      <div class="form-group">
        <label for="balance">보유 잔고(원)</label>
        <input type="number" id="balance" v-model="balance" class="form-control" placeholder="보유 잔고 입력" required>
      </div>

      <!-- 약관 동의 -->
      <div class="form-group terms-box">
        <h3>약관</h3>
        <div class="terms-container">
          <div class="form-check">
            <input type="checkbox" id="checkAll" v-model="checkAll" @change="toggleAll" class="form-check-input">
            <label for="checkAll" class="form-check-label">전체 동의</label>
          </div>
          <div class="form-check">
            <input type="checkbox" id="agree1" v-model="agree1" class="form-check-input" @change="checkAgreement">
            <label for="agree1" class="form-check-label">(필수) 개인회원 약관에 동의</label>
          </div>
          <div class="form-check">
            <input type="checkbox" id="agree2" v-model="agree2" class="form-check-input" @change="checkAgreement">
            <label for="agree2" class="form-check-label">(필수) 개인정보 수집 및 이용에 동의</label>
          </div>
        </div>
      </div>

      <!-- 제출 버튼 -->
      <div class="form-group text-center">
        <input type="submit" value="회원가입" class="btn btn-primary mt-3" :disabled="!canSubmit">
      </div>
    </form>
  </div>
</template>

<script setup>
import { ref, watch } from 'vue';
import axios from 'axios';

// 필드 상태
const username = ref('');
const password1 = ref('');
const password2 = ref('');
const first_name = ref('');
const last_name = ref('');
const birth = ref('');
const phone = ref('');
const email = ref('');
const mainBank = ref('');
const income = ref('');
const balance = ref('');
const agree1 = ref(false);
const agree2 = ref(false);
const checkAll = ref(false);

// 유효성 검사 상태
const usernameValid = ref(false);
const password1Valid = ref(false);
const password2Valid = ref(false);
const phoneValid = ref(false);
const isPasswordMatch = ref(true);

// 중복 확인 상태
const usernameChecked = ref(false);

// 버튼 활성화 여부
const canSubmit = ref(false);

// 아이디 유효성 검사
const checkUsername = () => {
  usernameValid.value = /^[a-zA-Z0-9!]{4,20}$/.test(username.value);
  usernameChecked.value = false;  // 아이디를 입력할 때마다 중복확인 여부 초기화
  checkFormValidity();
};
axios.defaults.baseURL = 'http://localhost:8000/api/accounts';  // Django 서버의 API URL

const checkUsernameAvailability = async () => {
  console.log("username.value:", username.value);
  if (usernameValid.value) {
    try {
      // URL이 간단해졌습니다.
      const response = await axios.get(`/check-username?username=${username.value}`);
      if (response.data.isAvailable) {
        usernameChecked.value = true;
        alert("아이디 사용 가능합니다.");
      } else {
        usernameChecked.value = false;
        alert("이미 사용 중인 아이디입니다.");
      }
    } catch (error) {
      console.error("아이디 중복 확인 실패", error);
      alert("아이디 중복 확인에 실패했습니다.");
    }
  }
  checkFormValidity();
};


// 비밀번호 유효성 검사
const checkPassword = () => {
  password1Valid.value = /^(?=.*[a-zA-Z])(?=.*\d)(?=.*[!@#$%^&*])[A-Za-z\d!@#$%^&*]{8,16}$/.test(password1.value);
  checkFormValidity();
};

// 비밀번호 확인
const checkPasswordMatch = () => {
  isPasswordMatch.value = password1.value === password2.value;
  password2Valid.value = isPasswordMatch.value;
  checkFormValidity();
};

// 전화번호 유효성 검사
const checkPhone = () => {
  phoneValid.value = /^\d{10,11}$/.test(phone.value);
  checkFormValidity();
};

// 약관 동의 체크
const checkAgreement = () => {
  checkFormValidity();
};

// 전체 동의 처리
const toggleAll = () => {
  agree1.value = checkAll.value;
  agree2.value = checkAll.value;
  checkAgreement();
};

// 폼 유효성 체크
const checkFormValidity = () => {
  canSubmit.value =
    usernameValid.value &&
    usernameChecked.value &&
    password1Valid.value &&
    password2Valid.value &&
    phoneValid.value &&
    agree1.value &&
    agree2.value;
};

// 회원가입 처리
const signUp = async () => {
  try {
    const response = await axios.post('/api/signup', {
      username: username.value,
      password1: password1.value,
      password2: password2.value,
      first_name: first_name.value,
      last_name: last_name.value,
      birth: birth.value,
      phone: phone.value,
      email: email.value,
      mainBank: mainBank.value,
      income: income.value,
      balance: balance.value,
    });
    console.log('회원가입 성공', response);
  } catch (error) {
    console.error('회원가입 실패', error);
  }
};

watch([username, password1, password2, phone, agree1, agree2], checkFormValidity);
</script>

<style scoped>
.signup-container {
  max-width: 500px;
  margin: 0 auto;
  padding: 20px;
  background-color: #f9f9f9;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.text-center {
  text-align: center;
}

.form-container {
  display: flex;
  flex-direction: column;
}

.form-group {
  position: relative;
  margin-bottom: 15px;
}

.form-group label {
  margin-bottom: 5px;
  display: block;
}

.form-control {
  width: 100%;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
  box-sizing: border-box;
}

.valid-check {
  position: absolute;
  right: 10px;
  top: 50%;
  transform: translateY(-50%);
  color: green;
}

.invalid-check {
  position: absolute;
  right: 10px;
  top: 50%;
  transform: translateY(-50%);
  color: red;
}

.btn {
  width: 100%;
  padding: 10px;
}

.helper-text {
  font-size: 0.875em;
  color: #6c757d;
}

.error-text {
  font-size: 0.875em;
  color: #dc3545;
}

.terms-box {
  background-color: #fff;
  border: 1px solid #ccc;
  border-radius: 5px;
  padding: 15px;
  margin-top: 20px;
}

.terms-container {
  margin-top: 20px;
}

.form-check {
  margin-bottom: 10px;
}

.form-check-input {
  margin-right: 10px;
}

.form-check-label {
  display: inline-block;
}

.modal-backdrop {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
}

.modal {
  background-color: white;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  text-align: center;
}

.modal-title {
  font-size: 1.25em;
  margin-bottom: 10px;
}

.modal-body {
  margin-bottom: 20px;
}
</style>
