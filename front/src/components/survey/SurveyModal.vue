<template>
  <div>
    <h2 class="text-xl font-bold mb-4">{{ currentQuestion.question }}</h2>
    <ul>
      <!-- 단일 또는 다중 선택 옵션 -->
      <li
        v-for="(option, index) in currentQuestion.options"
        :key="index"
        @click="handleOptionClick(option, index)"
        class="py-2 px-4 bg-gray-100 rounded mb-2 cursor-pointer hover:bg-gray-200"
        :class="{
          'bg-blue-500 text-white': isOptionSelected(index)
        }"
      >
        {{ option.text }}
      </li>
    </ul>
    <!-- 이전/다음 버튼 -->
    <div class="flex justify-between mt-4">
      <button
        @click="prevQuestion"
        class="bg-gray-500 text-white px-4 py-2 rounded hover:bg-gray-600"
        :disabled="currentQuestionIndex === 0"
      >
        이전
      </button>
      <button
        @click="nextOrSubmit"
        class="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600"
      >
        {{ isLastQuestion ? '결과 보기' : '다음' }}
      </button>
    </div>
  </div>
</template>

<script setup>
import { computed, ref } from 'vue';
import { useSurveyStore } from '@/stores/surveyStore';
import surveyData from '@/data/surveyData';

const surveyStore = useSurveyStore();
const selectedAnswerIndex = ref(null);

const currentQuestionIndex = computed(() => surveyStore.currentQuestionIndex);
const currentQuestion = computed(() => surveyStore.questions[currentQuestionIndex.value]);
const isLastQuestion = computed(() => currentQuestionIndex.value === surveyStore.questions.length - 1);

// 선택된 옵션인지 확인 (index로 판별)
const isOptionSelected = (index) => {
  const answers = surveyStore.answers[currentQuestionIndex.value];
  console.log(`Checking if option index=${index} is selected for question ${currentQuestionIndex.value}`);
  console.log('Answers:', answers);

  if (currentQuestion.value.type === 'single') {
    return answers === index; // 단일 선택
  } else if (currentQuestion.value.type === 'multiple') {
    return Array.isArray(answers) && answers.includes(index); // 다중 선택
  }
  return false;
};

// 옵션 클릭 핸들러
const handleOptionClick = (option, index) => {
  console.log(`Option clicked: ${option.text} (points=${option.points}, index=${index})`);

  if (currentQuestion.value.type === 'single') {
    // 단일 선택: 선택한 인덱스만 저장
    selectedAnswerIndex.value = index;
    surveyStore.saveAnswer(index);
    console.log('Single choice selected:', index);
  } else if (currentQuestion.value.type === 'multiple') {
    // 다중 선택: 인덱스를 배열에 추가/삭제
    const answers = surveyStore.answers[currentQuestionIndex.value] || [];
    const existingIndex = answers.indexOf(index);

    if (existingIndex === -1) {
      answers.push(index);
      console.log('Added to multiple answers:', answers);
    } else {
      answers.splice(existingIndex, 1);
      console.log('Removed from multiple answers:', answers);
    }
    surveyStore.answers[currentQuestionIndex.value] = answers;
  }
};

// 이전 질문으로 이동
const prevQuestion = () => {
  console.log('Previous question selected');
  selectedAnswerIndex.value = null;
  surveyStore.prevQuestion();
};

// 다음 질문 또는 제출
const nextOrSubmit = () => {
  console.log('Next question or submit triggered');
  if (currentQuestion.value.type === 'single' && selectedAnswerIndex.value === null) {
    alert('답변을 선택해주세요.');
    return;
  }
  if (isLastQuestion.value) {
    surveyStore.calculateScore();
    surveyStore.showResult(); // 결과 표시
  } else {
    selectedAnswerIndex.value = null;
    surveyStore.nextQuestion();
  }
};
</script>
