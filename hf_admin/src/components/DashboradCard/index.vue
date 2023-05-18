<template>
  <div class="dashboardCardBox grid-content" :style="{ background: tInfo.background }">
    <div class="grid-content-info">
      <p class="grid-content-info-num">{{ num }}</p>
      <p class="grid-content-info-title">{{ title }}</p>
    </div>
    <div class="grid-content-icon"><img :src="tInfo.icon" alt="图标"></div>
    <div class="grid-content-footer">{{ footer }}</div>
  </div>
</template>

<script lang="ts" setup>
import { ref, toRefs, computed } from "vue"
import successIcon from "@/assets/img/dashboard-success.png"
import waitIcon from "@/assets/img/dashboard-wait.png"
import totalIcon from "@/assets/img/dashboard-total.png"
import historyIcon from "@/assets/img/dashboard-history.png"

interface IDashboardCardProps {
  num?: number;
  title?: string;
  theme?: string;
  footer?: string;
}

let props = withDefaults(defineProps<IDashboardCardProps>(), {
  num: 0,
  title: "xxx",
  theme: "success",
  footer: "查看详情"
})

let { theme } = toRefs(props)

let tInfo = computed(() => {
  return themes[theme.value]
})

interface ITheme {
  icon: string;
  background: string;
}

let themes: { [key: string]: ITheme } = {
  success: {
    icon: successIcon,
    background: "linear-gradient(to right, #fd826c, #e76b3e)"
  },
  wait: {
    icon: waitIcon,
    background: "linear-gradient(to right, #FFB75E, #ED8F03)"
  },
  total: {
    icon: totalIcon,
    background: "linear-gradient(to right, #4CB5F5, #2B73B6)"
  },
  history: {
    icon: historyIcon,
    background: "linear-gradient(to right, #00E4D0, #5983E8)"
  }
}


</script>

<style lang="scss" scoped>
.dashboardCardBox {
  width: 100%;
  height: 100%;
}

.grid-content:hover {
  // 缩放
  transform: scale(1.05);
}

.grid-content {
  min-height: 10vmax;
  border-radius: 5px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1), 0 1px 3px rgba(0, 0, 0, 0.08);
  position: relative;

  &-icon {
    float: right;
    width: 30%;
    height: 5vmax;

    // 子元素垂直居中
    display: flex;
    align-items: center;

    img {
      width: 100%;
      height: 70%;
      object-fit: contain;
      display: block;
      text-align: right;
    }
  }

  &-info {
    padding: 0.6vmax;
    float: left;
    width: 70%;

    &-num {
      font-size: 3vmax;
      color: #fff;
      text-align: left;
      font-weight: 800;
    }

    &-title {
      font-size: 1.3vmax;
      color: #fff;
      text-align: left;
      margin-top: 0.7vmax;
      font-weight: 400;
    }
  }

  &-footer {
    width: 100%;
    height: 3vmax;
    font-size: 1vmax;
    line-height: 3vmax;
    text-align: center;
    font-weight: 200;
    color: white;
    position: absolute;
    bottom: 0;
    border-bottom-left-radius: 5px;
    border-bottom-right-radius: 5px;
    background-color: rgba(255, 255, 255, 0.3);
  }

}
</style>
