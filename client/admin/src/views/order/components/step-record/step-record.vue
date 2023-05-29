<template>
  <div class='step-record'>
    <div class="title-box">
      <span>订单流程</span>
    </div>

    <div class="step-list-box">
      <el-steps direction="vertical" finish-status="success" :active="1">
        <el-step v-for="item in stepRecordList" :key="item.id">
          <template #title>
            {{ item.step_sort_title }}
          </template>
          <template #description>
            <component :is="StepDefaultItem" :info="item"></component>
          </template>
        </el-step>
      </el-steps>
    </div>
  </div>
</template>

<script lang="ts" setup>
import StepDefaultItem from "./components/step-default-item.vue";
import { StepRecord } from "./interfaces/step-record";

let stepRecordList: StepRecord[] = [
  {
    id: 1,
    step_sort: 1,
    step_sort_title: "订单创建",
    order_list: 1,
    start_time: "2022/1/1",
    end_time: '2022/1/2',
    is_delete: false,
    notes: "备注"
  },
  {
    id: 2,
    step_sort: 1,
    step_sort_title: "生产跟单",
    order_list: 1,
    start_time: "2022/1/1",
    end_time: '2022/1/2',
    is_delete: false,
    notes: "备注"
  },
  {
    id: 2,
    step_sort: 1,
    step_sort_title: "业务跟单",
    order_list: 1,
    start_time: "2022/1/1",
    end_time: '2022/1/2',
    is_delete: false,
    notes: "备注"
  }
]
</script>

<style lang="scss" scoped>
@import './step-record.scss'
</style>
