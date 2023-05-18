<template>
  <div ref="chart" class='stockBox'>
  </div>
</template>

<script lang="ts" setup>
import { ref, onMounted } from "vue"
import * as echarts from 'echarts';

const chart = ref<HTMLElement>();

const data = [
  { name: '压花类', value: 100 },
  { name: '压胶类', value: 200 },
  { name: '凹凸类', value: 350 },
  { name: '激光类', value: 30 },
  { name: '水墨画类', value: 370 },
];

onMounted(() => {
  loadChart();
});

const loadChart = () => {
  if (!chart.value) return;
  const myChart = echarts.init(chart.value);
  let option = {
    tooltip: {
      trigger: 'item'
    },
    legend: {
      orient: 'vertical',
      left: 'left'
    },
    series: [
      {
        name: 'Access From',
        type: 'pie',
        radius: '50%',
        data: data.map(item => ({
          value: item.value,
          name: item.name,
        })),
        emphasis: {
          itemStyle: {
            shadowBlur: 10,
            shadowOffsetX: 0,
            shadowColor: 'rgba(0, 0, 0, 0.5)'
          }
        }
      }
    ]
  };
  myChart.setOption(option);
};



</script>

<style lang="scss" scoped>
.stockBox {
  width: 100%;
  height: 100%;
}
</style>
