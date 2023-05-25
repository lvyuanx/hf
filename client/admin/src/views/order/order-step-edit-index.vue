<template>
  <div class='change-step-container'>
    <el-form :model="formData" label-position="left" ref="setpFormRef" :rules="rules" :inline="true" label-width="100px">
      <el-row>
        <el-col :span="12">
          <el-form-item label="流程类型" prop="order_type">
            <el-select v-model="formData.order_type" :disabled="!isChangeType" placeholder="请选项类型">
              <el-option v-for="ot in orderTypeList" :key="ot.id" :label="ot.name" :value="ot.id" />
            </el-select>
          </el-form-item>
        </el-col>
        <el-col :span="12">
          <el-form-item label="" style="float: right;">
            <el-tooltip class="box-item" effect="dark" content="添加流程" placement="left-start">
              <el-button type="primary" :icon="Plus" @click="dialogStepBaseTableVisible = true" circle />
            </el-tooltip>
          </el-form-item>
        </el-col>
      </el-row>
      <el-row>
        <el-col :span="24">
          <div class="sort-list-box">
            <div :span="24" class="sort-list-title">
              订单流程
            </div>

            <div class="step-list" ref="listRef">
              <FLIPWrapper>
                <el-col draggable="true" :span="20" :offset="2" class="step-item" v-for="item in selectStepList"
                  :key="item.id" :itemKey="item.id">
                  {{ item.name }}
                </el-col>
              </FLIPWrapper>

            </div>
          </div>

        </el-col>
      </el-row>
      <el-row>
        <el-col :span="24">
          <el-form-item prop="notes" label="备注" class="notes">
            <el-input v-model="formData.notes" :autosize="{ minRows: 2, maxRows: 4 }" type="textarea"
              placeholder="请输入备注信息" />
          </el-form-item>
        </el-col>
      </el-row>
    </el-form>

    <div class="btn-box">
      <el-button type="primary" @click="confirm_submit">提交</el-button>
      <el-button @click="back">返回</el-button>
    </div>

    <!-- 编辑订单项 start -->
    <el-dialog v-model="dialogStepBaseTableVisible" title="选择流程">
      <el-row :gutter="20">
        <el-col style="margin-bottom: 2rem;" v-for="item in stepBaseList" :key="item.id" :span="6">
          <el-checkbox v-model="item.isCheck" :label="item.name" size="small" border />
        </el-col>
      </el-row>
      <template #footer>
        <span class="dialog-footer">
          <el-button type="primary" @click="dialogStepBaseTableVisible = false">
            确认
          </el-button>
        </span>
      </template>
    </el-dialog>
    <!-- 编辑订单项 end -->
  </div>
</template>

<script lang="ts" setup>
import { ref, onMounted, nextTick } from 'vue';
import { Plus } from "@element-plus/icons-vue"
import request from "@/utils/request"
import { ElMessage, ElMessageBox, FormInstance, FormRules } from "element-plus"
import { isEmpty } from "@/utils/utils"
import FLIPWrapper from "@/components/Flip/index.vue"
import { useRoute, useRouter } from 'vue-router';
import { StepOrderChangeRecord, StepBase, StepSort } from './interfaces/order-step';
import { OrderType } from './interfaces/order-list';

let dialogStepBaseTableVisible = ref(false)

let route = useRoute()
let router = useRouter()
const back = () => {
  router.back()
}
let isChangeType = ref(true)

onMounted(async () => {
  let recordId = route.params.id
  try {
    await findAllTypes()
    await findAllSteps()
    ondragList()

    if (isEmpty(recordId)) { return }
    isChangeType.value = false
    const stepCR = await request.http<IResult<StepOrderChangeRecord>>("get_setpSortCR", {}, {}, { id: recordId })
    let { notes, order_type } = stepCR.data
    formData.notes = notes
    formData.order_type = order_type
    const stepBases = await request.http<IResult<StepSort[]>>("get_setpSortByRid", { record_id: recordId }, {})
    stepBases.data.forEach(sb => {
      let selectSb = stepBaseList.value.filter(s => s.id === sb.step_base)
      if (selectSb) {
        selectStepList.value.push(selectSb[0])
      }
    })
    stepBaseList.value = markCheckedItems(stepBaseList.value, selectStepList.value)
  } catch (error) {
    console.log(error)
    back()
  }
})

function markCheckedItems(items: StepBase[], checkedItems: StepBase[]): StepBase[] {
  // 构建一个字典，用于快速查找已选中的项
  const dict: Record<number | string, boolean> = {};
  for (const item of checkedItems) {
    dict[item.id] = true;
  }

  // 遍历未选中的项，为匹配的项添加 isCheck 属性
  const result: StepBase[] = [];
  for (const item of items) {
    if (dict[item.id]) {
      result.push({ ...item, isCheck: true });
    } else {
      result.push(item);
    }
  }

  return result;
}

let setpFormRef = ref<FormInstance>()
const confirm_submit = () => {
  if (isChangeType.value) {
    submit()
    return
  }
  ElMessageBox.confirm('修改流程，该类型已有订单流程不变，新创建订单将执行新的流程！', '消息提醒', {
    confirmButtonText: '确定',
    cancelButtonText: '取消',
    type: 'warning',
  }).then(submit)
}
const submit = async () => {
  let formEl: FormInstance | undefined = setpFormRef.value
  if (!formEl) return
  const valid = await formEl.validate()
  if (!valid) {
    return
  }
  if (isEmpty(selectStepList.value)) {
    ElMessage.warning("流程不能为空！")
  }
  let stepSortList: StepSort[] = []
  let setpList: StepBase[] = selectStepList.value
  for (let i = 0; i < setpList?.length; i++) {
    let curr = setpList[i]
    let parent = i > 0 ? setpList[i - 1].id : undefined
    let next = i < setpList?.length - 1 ? setpList[i + 1].id : undefined

    let setp: StepSort = {
      id: "",
      name: curr.name,
      step_base: curr.id,
      parent_step_id: parent,
      child_step_id: next,
      is_skip: curr.is_skip
    }
    stepSortList.push(setp)
  }
  let data = {
    ...formData,
    step_sort: stepSortList
  }
  try {
    await request.http<IResult<any>>("post_setpSortEdit", {}, data)
    ElMessageBox.alert('编辑成功！', '消息提醒', {
      confirmButtonText: '确定',
      type: "success",
      callback: () => {
        router.back()
      },
    })
  } catch (error) {
    console.log(error)
  }
}

let formData = reactive<IEditSetpSort>({
  order_type: "",
  notes: ""
})

const rules = reactive<FormRules>({
  order_type: [
    { required: true, message: '请选择类型！', trigger: 'blur' }
  ],
})

let orderTypeList = ref<OrderType[]>([])
// 查询所有类型
const findAllTypes = async () => {
  try {
    const result = await request.http<IResult<OrderType[]>>("get_orderTypeList", {}, {})
    orderTypeList.value = result.data
  } catch (error) {
    console.log(error)
  }
}
let stepBaseList = ref<StepBase[]>([])
let selectStepList = ref<StepBase[]>([])
watch(
  () => stepBaseList.value,
  (newList, oldList) => {
    const selectedSteps = newList.filter(item => item.isCheck);
    selectStepList.value.length = 0;
    selectStepList.value.push(...selectedSteps);
  },
  { deep: true }
);


const ondragList = () => {
  const list = document.querySelector('.step-list') as HTMLElement;
  let sourceNode: HTMLElement | null;

  list.ondragstart = (e: DragEvent) => { // 拖动开始
    setTimeout(() => {
      if (e.target instanceof HTMLElement) {
        e.target.classList.add("moving");
        sourceNode = e.target;
      }
    }, 0);
    e.dataTransfer!.effectAllowed = "move";
  }



  list.ondragend = (e: DragEvent) => { // 拖动结束
    if (e.target instanceof HTMLElement) {
      e.target.classList.remove("moving");
    }
  }

  list.ondragenter = (e: DragEvent) => {
    if (e.target instanceof HTMLElement) {
      e.preventDefault();
      if (e.target === list || e.target === sourceNode) {
        return;
      }
      if (sourceNode instanceof HTMLElement) {
        const children = Array.from(list.children)
        const sourceIndex = children.indexOf(sourceNode)
        const targetIndex = children.indexOf(e.target)
        let sourceId = sourceNode.getAttribute("itemKey") as string
        let targetId = e.target.getAttribute("itemKey") as string
        if (sourceIndex < targetIndex) {
          changeOrder<StepBase>(selectStepList, sourceId, targetId);
        } else {
          changeOrder<StepBase>(selectStepList, sourceId, targetId);
        }
      }
    }
  }

  list.ondragover = (e: DragEvent) => {
    if (e.target instanceof HTMLElement) {
      e.preventDefault();
    }
  }

}
function changeOrder<T extends { id: string | number }>(list: Ref<T[]>, id1: string, id2: string) {
  const index1 = list.value.findIndex((item) => item.id == id1);
  const index2 = list.value.findIndex((item) => item.id == id2);

  if (index1 === -1 || index2 === -1) {
    throw new Error('Item not found in list');
  }

  const item1 = list.value[index1]

  if (index1 < index2) {
    list.value.splice(index2 + 1, 0, item1);
    list.value.splice(index1, 1)
  } else if (index1 > index2) {
    list.value.splice(index2, 0, item1);
    list.value.splice(index1 + 1, 1)
  }


  return list;
}

// 查询所有流程
const findAllSteps = async () => {
  try {
    const result = await request.http<IResult<StepBase[]>>("get_setpBaseList", {}, {})
    let data = result.data
    data.forEach(item => {
      item["isCheck"] = false
    })
    stepBaseList.value = result.data
  } catch (error) {
    console.log(error)
  }
}

</script>

<style lang="scss" scoped>
@import "./order-step-edit-index.scss";
</style>
