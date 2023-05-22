<template>
  <div class='hdbox'>
    <el-tooltip placement="top" v-for="(item, index) in planOrders" :key="index">
      <template #content> <span style="font-weight: 600;color: #e06c75;">{{ item.name }}</span><br />目标：{{ item.total }}
        件<br />完成：{{
          item.close }} 件</template>
      <div class="blood-Strip-box">
        <div class="title">{{ item.name }}</div>
        <div class="progress-bar">
          <p>{{ getPercentage(item.close, item.total).toFixed(1) }}%</p>
          <div class="progress" :style="{
            width: `${getPercentage(item.close, item.total).toFixed(1)}%`,
            backgroundColor: colors[index % colors.length]
          }"></div>
        </div>
      </div>
    </el-tooltip>
  </div>
</template>

<script lang="ts" setup>
import { ref } from "vue"
interface IPlanOrder {
  name: string;
  total: number;
  close: number;
}

let props = defineProps<{
  planOrders: IPlanOrder[];
}>()

const getPercentage = (num1: number, num2: number) => {
  let percentage = (num1 / num2) * 100
  return percentage > 100 ? 100 : percentage
}

let colors = [
  "#5c7bd9",
  "#91cc75",
  "#ffdc60",
  "#ff7070",
  "#7ed3f4",
]

</script>

<style lang="scss" scoped>
@import "./dashboard-horizontal-diagram.scss"
</style>
