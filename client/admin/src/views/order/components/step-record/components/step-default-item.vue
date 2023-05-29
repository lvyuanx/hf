<template>
  <div class='setp-default-item-container'>
    <div v-if="!info" class="empty-box">暂无内容</div>
    <div class="step-info-container">
      <div class="step-info">
        {{ info?.notes }}
      </div>
      <div class="step-info">
        开始时间: {{ info?.start_time }}
      </div>
      <div class="step-info">
        结束时间: {{ info?.start_time }}
      </div>
    </div>
  </div>
</template>
<script lang="ts" setup name="StepDefaultItem">
import { StepRecord } from '../interfaces/step-record';

defineProps<{
  info?: StepRecord
}>()

</script>
<style lang="scss" scoped>
@import "./step-default-item.scss"
</style>
