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
            <Stock></Stock>
          </div>
        </div>
      </el-col>
      <el-col :span="12" class="right-contaier">
        <el-row :gutter="0" class="right-top-box charts-container">
          <div class="title-box">最近7天接单量图</div>
          <div class="charts-box">
            <ReceivingQuantity></ReceivingQuantity>
          </div>
        </el-row>
        <el-row :gutter="0" class="right-bottom-box">
          <div class="right-bottom-box-left charts-container">
            <div class="title-box">计划订单量</div>
            <div class="charts-box">
              <HorizontalDiagram :plan-orders="planOrder"></HorizontalDiagram>
            </div>
          </div>
          <div class="right-bottom-box-right charts-container">
            <div class="title-box">最近订单</div>
            <div class="charts-box">
              <HistoryOrder :history-orders="historyOrders"></HistoryOrder>
            </div>
          </div>
        </el-row>
      </el-col>
    </el-row>
  </div>
</template>

<script lang="ts" setup>
import DashboardCard from "@/components/DashboradCard/index.vue"
import Stock from "@/components/Echarts/Stock.vue"
import ReceivingQuantity from "@/components/Echarts/ReceivingQuantity.vue"
import HorizontalDiagram from "@/components/Echarts/HorizontalDiagram.vue"
import HistoryOrder from "@/components/Echarts/HistoryOrder.vue"
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
.dashboardBox {
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
}

.top-box {
  width: 100%;
  height: 10vmax;
}

.bottom-box {
  width: 100%;
  flex: 1;
}

.echarts-container {
  width: 100%;
  height: 100%;
  background-color: white;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1), 0 1px 3px rgba(0, 0, 0, 0.08);
  border-radius: 5px;
}

.charts-container {
  display: flex;
  flex-direction: column;

  .title-box {
    width: 100%;
    height: 2.5vmax;
    line-height: 2.5vmax;
    text-align: left;
    font-size: 1vmax;
    font-weight: 600;
    padding-left: 1vmax;
    border-bottom: 5px solid #f1f1f1;
  }

  .charts-box {
    width: 100%;
    flex: 1;
    padding: 1vmax;
    box-sizing: border-box;
    overflow: hidden;
  }
}

.right-contaier {
  width: 100%;
  height: 100%;

  .right-top-box {
    width: 100%;
    height: calc(50% - 0.5vmax);
    background-color: white;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1), 0 1px 3px rgba(0, 0, 0, 0.08);
    border-radius: 5px;
  }

  .right-bottom-box {
    margin-top: 1vmax;
    width: 100%;
    height: calc(50% - 0.5vmax);

    &-left {
      width: calc(50% - 0.5vmax);
      height: 100%;
      float: left;
      background-color: white;
      box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1), 0 1px 3px rgba(0, 0, 0, 0.08);
      border-radius: 5px;
    }

    &-right {
      width: calc(50% - 0.5vmax);
      height: 100%;
      float: left;
      margin-left: 1vmax;
      background-color: white;
      box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1), 0 1px 3px rgba(0, 0, 0, 0.08);
      border-radius: 5px;
    }
  }


}
</style>
