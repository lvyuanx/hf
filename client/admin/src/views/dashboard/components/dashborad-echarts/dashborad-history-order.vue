<template>
  <div class='historyOrderBox'>
    <div v-for="(item, index) in historyOrders" :key="item.orderId">{{ item.title }}</div>
    <div v-if="historyOrders && historyOrders.length > 0" class="findAllBox">查看更多></div>

  </div>
</template>

<script lang="ts" setup>
import { ref } from "vue"
interface IHistoryOrder {
  title: string;
  orderId: number;
}
const props = defineProps<{
  historyOrders?: IHistoryOrder[];
}>()
</script>

<style lang="scss" scoped>
@import "./dashborad-history-order.scss"
</style>
