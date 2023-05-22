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
@import "./dashborad-card.scss"
</style>
