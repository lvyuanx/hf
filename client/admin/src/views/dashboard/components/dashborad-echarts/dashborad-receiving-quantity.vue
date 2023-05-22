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

const getRandomData = () => {
  const data = []
  for (let i = 0; i < 7; i++) {
    data.push(Math.floor(Math.random() * 500))
  }
  return data
}

const loadChart = () => {
  if (!chart.value) return;
  const myChart = echarts.init(chart.value);
  let option = {
    tooltip: {},
    legend: {
      data: ['压花类', '压胶类', '凹凸类', '激光类', '水墨画类']
    },
    xAxis: {
      type: 'category',
      data: ['第1天', '第2天', '第3天', '第4天', '第5天', '第6天', '第7天']
    },
    yAxis: {
      type: 'value'
    },
    grid: {
      top: '10%',
      left: '3%',
      right: '3%',
      bottom: '4%',
      containLabel: true
    },
    series: [
      {
        name: '压花类',
        type: 'line',
        data: getRandomData()
      },
      {
        name: '压胶类',
        type: 'line',
        data: getRandomData()
      },
      {
        name: '凹凸类',
        type: 'line',
        data: getRandomData()
      },
      {
        name: '激光类',
        type: 'line',
        data: getRandomData()
      },
      {
        name: '水墨画类',
        type: 'line',
        data: getRandomData()
      }
    ]
  }

  myChart.setOption(option);
};



</script>

<style lang="scss" scoped>
@import url('./dashborad-receiving-quantity.scss');
</style>
