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
.historyOrderBox {
  width: 100%;
  height: 100%;
  ;

  div {
    width: 100%;
    height: 1.8vmax;
    line-height: 1.8vmax;
    font-size: 0.8vmax;
    color: #aaa;
    border-bottom: 1px solid #ccc;
    // 超过一行显示省略号
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
    cursor: pointer;
  }

  div:hover {
    color: #000;
  }

  .findAllBox {
    width: 100%;
    height: 1.8vmax;
    line-height: 1.8vmax;
    text-align: center;
    font-size: 0.7vmax;
    color: #aaa;
    border-bottom: 0;
    cursor: pointer;
  }

}
</style>
