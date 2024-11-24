import { defineStore } from 'pinia';
import { surveyData } from '@/data/surveyData.js';

export const useSurveyStore = defineStore('survey', {
  state: () => ({
    questions: surveyData,
    currentQuestionIndex: 0,
    answers: [], // 각 질문의 답변 인덱스를 저장
    result: null,
    showResultModal: false,
  }),
  actions: {
    saveAnswer(index) {
      console.log(`Saving answer index=${index} for question ${this.currentQuestionIndex}`);
      if (this.questions[this.currentQuestionIndex].type === 'single') {
        this.answers[this.currentQuestionIndex] = index;
      } else if (this.questions[this.currentQuestionIndex].type === 'multiple') {
        if (!Array.isArray(this.answers[this.currentQuestionIndex])) {
          this.answers[this.currentQuestionIndex] = [];
        }
        const existingIndex = this.answers[this.currentQuestionIndex].indexOf(index);
        if (existingIndex === -1) {
          this.answers[this.currentQuestionIndex].push(index);
        } else {
          this.answers[this.currentQuestionIndex].splice(existingIndex, 1);
        }
      }
      console.log('Updated answers:', this.answers);
    },
    nextQuestion() {
      console.log('Moving to next question');
      if (this.currentQuestionIndex < this.questions.length - 1) {
        this.currentQuestionIndex++;
      }
      console.log('Current question index:', this.currentQuestionIndex);
    },
    prevQuestion() {
      console.log('Moving to previous question');
      if (this.currentQuestionIndex > 0) {
        this.currentQuestionIndex--;
      }
      console.log('Current question index:', this.currentQuestionIndex);
    },
    calculateScore() {
      console.log('Calculating total score');
      let totalScore = 0;

      this.answers.forEach((answer, questionIndex) => {
        const question = this.questions[questionIndex];
        if (Array.isArray(answer)) {
          // 다중 선택 점수 계산
          totalScore += answer.reduce((acc, index) => acc + question.options[index].points, 0);
        } else if (typeof answer === 'number') {
          // 단일 선택 점수 계산
          totalScore += question.options[answer]?.points || 0;
        }
      });

      console.log('Total score:', totalScore);

      if (totalScore <= 20) this.result = '안정형';
      else if (totalScore <= 40) this.result = '안정추구형';
      else if (totalScore <= 60) this.result = '위험중립형';
      else if (totalScore <= 80) this.result = '적극투자형';
      else this.result = '공격투자형';

      console.log('Investment style:', this.result);
    },
    showResult() {
      this.showResultModal = true;
      console.log(`Final result: ${this.result}`);
    },
    hideResult() {
      this.showResultModal = false;
    },
  },
});
