<script setup>
import LeftSection from "@/components/LeftSection.vue";
import RightSection from "@/components/RightSection.vue";
</script>

<template>
  <div class="main-page">
    <div class="container-fluid main-content">
      <div class="row">
        <div class="col-md-4 bg-light py-3">
          <LeftSection /> <!-- 왼쪽 섹션 컴포넌트 -->
        </div>
        <div class="col-md-8 py-3">
          <RightSection /> <!-- 오른쪽 섹션 컴포넌트 -->
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>

</style>
