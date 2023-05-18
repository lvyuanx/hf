<template>
  <el-table :data="tableData" :border="true" style="width: 100%" height="230"
    :header-cell-style="{ backgroundColor: '#f5f7fa', color: '#93969c', fontWeight: 600 }">
    <slot name="left">
    </slot>
    <el-table-column v-for="item in tableTitle" :key="item.prop" :prop="item.prop" :label="item.lable"
      :width="item.width" />
    <slot name="right">
    </slot>
    <template #empty>
      <el-empty :image-size="100" description="暂无数据" />
    </template>
  </el-table>
  <el-pagination v-if="page" style="margin-top: 10px;" background layout="total, prev, pager, next" :total="page.total"
    :page-size="page.pageSize" :current-page="currentPage" @current-change="handleCurrentChange" />
</template>

<script lang="ts" setup>
import { ref, toRefs, watch, computed } from "vue"

interface ITableHealer {
  prop: string;
  lable: string;
  width?: string;
}
interface IPage {
  isPage?: boolean;
  pageCount?: number;
  currentPage?: number;
  pageSize?: number;
  total?: number
}

interface ITableProps {
  tableData: any[];
  tableTitle: ITableHealer[];
  page?: IPage;
}
let props = defineProps<ITableProps>()

let { page } = toRefs(props)

let currentPage = computed(() => {
  return page?.value?.currentPage
})


// 子传父要此案定义好emit
const emit = defineEmits<{
  // (event: '方法名称'): 方法的返回值
  (event: "changePage", currentPage: number): void;
}>();

const handleCurrentChange = (val: number) => {
  emit("changePage", val)
}

</script>

<style lang="scss" scoped>
.com-table-box {
  width: 100%;
  height: 100%;
}
</style>
