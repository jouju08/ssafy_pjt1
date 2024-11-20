// src/stores/authStore.js
import { ref } from 'vue';
import { defineStore } from 'pinia';
import axios from 'axios';

export const useAuthStore = defineStore('user', () => {
  const API_URL = 'http://localhost:8000';
  const token = ref(null);

  // 쿠키에 토큰을 저장하는 함수
  const setToken = (tokenValue) => {
    document.cookie = `token=${tokenValue}; path=/; max-age=3600`; // 1시간 만료
    token.value = tokenValue;
  };

  // 쿠키에서 토큰을 읽는 함수
  const getTokenFromCookie = () => {
    const match = document.cookie.match(/(?:^| )token=([^;]+)(?=;|$)/);
    if (match) {
      token.value = match[1];
    }
  };

  // 로그인 요청을 보내고 성공 시 토큰 저장
  const logIn = function (payload) {
    const { username, password } = payload;
    
    axios.post(`${API_URL}/accounts/login/`, { username, password })
      .then(res => {
        const { key } = res.data;
        setToken(key); // 로그인 성공 후 토큰을 쿠키에 저장
        console.log('로그인 완료');
        console.log(res.data);
      })
      .catch(err => console.log(err));
  };

  // 로그아웃 처리 (쿠키에서 토큰 삭제)
  const logOut = function () {
    axios.post(`${API_URL}/api/accounts/logout/`)
      .then((res) => {
        console.log(res.data);
        document.cookie = 'token=; path=/; max-age=0'; // 쿠키에서 토큰 삭제
        token.value = null;
      })
      .catch((err) => {
        console.log(err);
      });
  };

  // 페이지 로드 시 쿠키에서 토큰 읽기
  getTokenFromCookie();

  return { API_URL, logIn, logOut, token };
}, { persist: true });
