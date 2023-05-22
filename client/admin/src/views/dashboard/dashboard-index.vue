<template>
  <div class='dashboardBox'>
    <el-row :gutter="20" class="top-box">
      <el-col :span="6" v-for="item in cardList">
        <DashboardCard :num="item.num" :title="item.title" :theme="item.theme"></DashboardCard>
      </el-col>
    </el-row>
    <el-row :gutter="20" style="margin-top: 1vmax;" class="bottom-box">
      <el-col :span="12">
        <div class="echarts-container charts-container">
          <div class="title-box">三月订单详情图</div>
          <div class="charts-box">
            <DashboardStock></DashboardStock>
          </div>
        </div>
      </el-col>
      <el-col :span="12" class="right-contaier">
        <el-row :gutter="0" class="right-top-box charts-container">
          <div class="title-box">最近7天接单量图</div>
          <div class="charts-box">
            <DashboardReceivingQuantity></DashboardReceivingQuantity>
          </div>
        </el-row>
        <el-row :gutter="0" class="right-bottom-box">
          <div class="right-bottom-box-left charts-container">
            <div class="title-box">计划订单量</div>
            <div class="charts-box">
              <DashboardHorizontalDiagram :plan-orders="planOrder"></DashboardHorizontalDiagram>
            </div>
          </div>
          <div class="right-bottom-box-right charts-container">
            <div class="title-box">最近订单</div>
            <div class="charts-box">
              <DashboardHistoryOrder :history-orders="historyOrders"></DashboardHistoryOrder>
            </div>
          </div>
        </el-row>
      </el-col>
    </el-row>
  </div>
</template>

<script lang="ts" setup>
import DashboardCard from "./components/dashborad-card/dashborad-card.vue"
import DashboardStock from "./components/dashborad-echarts/dashborad-stock.vue"
import DashboardReceivingQuantity from "./components/dashborad-echarts/dashborad-receiving-quantity.vue"
import DashboardHorizontalDiagram from "./components/dashborad-echarts/dashboard-horizontal-diagram.vue"
import DashboardHistoryOrder from "./components/dashborad-echarts/dashborad-history-order.vue"
import request from "@/utils/request"
import { IDashboardCard } from './interface/index'

let cardList = ref<IDashboardCard[]>([
  {
    num: 0,
    title: "已完成订单",
    theme: "success",
  },
  {
    num: 0,
    title: "未完成订单",
    theme: "wait",
  },
  {
    num: 0,
    title: "总订单",
    theme: "total",
  },
  {
    num: 0,
    title: "历史订单",
    theme: "history",
  }
])

let planOrder = ref([
  {
    name: "压花类",
    total: 100,
    close: 70
  },
  {
    name: "压胶类",
    total: 100,
    close: 50
  },
  {
    name: "凹凸类",
    total: 100,
    close: 50
  },

  {
    name: "激光类",
    total: 60,
    close: 50
  },
  {
    name: "水墨画",
    total: 100,
    close: 30
  },
])

const historyOrders = ref([
  { title: "3/25 xxx工厂 压胶类 1000件", orderId: 1 },
  { title: "3/25 xxx工厂 压胶类 1000件", orderId: 2 },
  { title: "3/25 xxx工厂 压胶类 1000件", orderId: 3 },
  { title: "3/25 xxx工厂 压胶类 1000件", orderId: 4 },
  { title: "3/25 xxx工厂 压胶类 1000件", orderId: 5 },
  { title: "3/25 xxx工厂 压胶类 1000件", orderId: 6 },
])

onMounted(async () => {
  await loadCardList()
})

const loadCardList = async () => {
  let orderListCount = await findOrderListCountByState()
  cardList.value.forEach((item: IDashboardCard, idx: number) => {
    if (item.title == '总订单') {
      item.num = orderListCount as number
    }
  })
}

const findOrderListCountByState = async () => {
  try {
    let result = await request.http<IResult<number>>("get_FindOrderListCountByState", {}, {})
    return result.data
  } catch (error) {
    console.log(error)
    return 0
  }
}

</script>

<style lang="scss" scoped>
@import "./dashboard-index.scss"
</style>
