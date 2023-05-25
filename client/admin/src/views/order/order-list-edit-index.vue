<template>
  <div class='order-container' v-loading="loadingPage" element-loading-text="加载中...">
    <!-- form start -->
    <el-form :model="formData" label-position="right" ref="orderListFormRef" :rules="rules" label-width="120px">
      <el-form-item prop="order_base" label="订单款号">
        <el-input v-model="formShow.orderValue" disabled placeholder="请选择款号">
          <template #append>
            <el-button @click="selectOrderBase">选择款号</el-button>
          </template>
        </el-input>
      </el-form-item>

      <el-form-item prop="customer" label="订单客户">
        <el-input v-model="formShow.customerValue" disabled placeholder="请选客户">
          <template #append>
            <el-button @click="selectCustomer">选择客户</el-button>
          </template>
        </el-input>
      </el-form-item>


      <el-form-item prop="order_technology" label="订单工艺">
        <el-input v-model="formData.order_technology" placeholder="请输入工艺" />
      </el-form-item>

      <el-form-item label="订单项">
        <Table :table-data="tableData" :table-title="tableTitle">
          <template #right>
            <el-table-column align="right" fixed="right" width="180">
              <template #header>
                <el-tooltip class="box-item" effect="dark" content="添加订单项" placement="top-end">
                  <el-button type="primary" class="add-btn" :icon="Plus" circle @click="addOrderDetail"></el-button>
                </el-tooltip>
              </template>
              <template #default="scope">
                <el-button size="small" @click="handleEdit(scope.$index, scope.row)">编辑</el-button>
                <el-button size="small" type="danger" @click="handleDelete(scope.$index, scope.row)">删除</el-button>
              </template>
            </el-table-column>
          </template>
        </Table>
      </el-form-item>
      <el-form-item label="订单总价">
        <el-input v-model="totalPrice" disabled />
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="submitForm">确定</el-button>
        <el-button @click="back">返回</el-button>
      </el-form-item>
    </el-form>
    <!-- form end -->

    <!-- 选择款号 start -->
    <el-dialog v-model="dialogOrderBaseTableVisible" title="请选择款号">
      <el-row style="margin-bottom: 10px;">
        <el-col :span="12">
        </el-col>
        <el-col :span="8">
          <el-input v-model="searchOrder" placeholder="请输入款号或者产品名称进行搜索" />
        </el-col>
        <el-col :span="4">
          <el-button style="width: 100%;" @click="selectOrderBase">搜索</el-button>
        </el-col>
      </el-row>
      <Table :table-data="orderBaseData" :table-title="orderBaseTableTitle" :page="orderPage"
        @changePage="changeOrderBasePage">
        <template #right>
          <el-table-column align="right" fixed="right">
            <template #header>
              操作
            </template>
            <template #default="scope">
              <el-button type="primary" size="small" @click="handleSelectOrder(scope.$index, scope.row)">选择</el-button>
            </template>
          </el-table-column>
        </template>
      </Table>
    </el-dialog>
    <!-- 选择款号 end -->

    <!-- 选择客户 start -->
    <el-dialog v-model="dialogCustomerTableVisible" title="请选客户">
      <el-row style="margin-bottom: 10px;">
        <el-col :span="12">
        </el-col>
        <el-col :span="8">
          <el-input v-model="searchCustomer" placeholder="请输入客户名/电话/公司名称进行搜索" />
        </el-col>
        <el-col :span="4">
          <el-button style="width: 100%;" @click="selectCustomer">搜索</el-button>
        </el-col>
      </el-row>
      <Table :table-data="customerData" :table-title="customerTableTitle" :page="customerPage"
        @changePage="changeOrderBasePage">
        <template #left>
          <el-table-column align="left">
            <template #header>
              头像
            </template>
            <template #default="scope">
              <el-image style="width: 100%;" :src="scope.row.avatar" fit="cover">
                <template #error>
                  <div class="image-slot">
                    <el-icon><i-ep-picture /></el-icon>
                  </div>
                </template>
              </el-image>
            </template>
          </el-table-column>
        </template>
        <template #right>
          <el-table-column align="right" fixed="right">
            <template #header>
              操作
            </template>
            <template #default="scope">
              <el-button type="primary" size="small" @click="handleSelectCustomer(scope.$index, scope.row)">选择</el-button>
            </template>
          </el-table-column>
        </template>
      </Table>
    </el-dialog>
    <!-- 选择客户 end -->


    <!-- 编辑订单项 start -->
    <el-dialog v-model="dialogOrderDetailTableVisible" :title="orderDetailTitle">

      <el-form :model="orderDetail" label-position="right" ref="customerDetailFormRef" :rules="detailRules"
        label-width="80px">

        <el-form-item prop="order_number" label="订单数量">
          <el-input-number v-model="orderDetail.order_number" :min="1"
            @change="(cur, pre) => { orderDetail.order_number = cur ?? 1 }" />
        </el-form-item>

        <el-form-item prop="order_price" label="单价(元)">
          <el-input-number v-model="orderDetail.order_price" :min="0.01" :precision="2"
            @change="(cur, pre) => { orderDetail.order_price = cur ?? 0.01 }" />
        </el-form-item>

        <el-form-item label="总价(元)">
          <el-input :value="orderDetail.order_price * orderDetail.order_number" :precision="2" disabled />
        </el-form-item>

        <el-form-item prop="color" label="颜色">
          <el-input v-model="orderDetail.color" placeholder="请输入颜色" />
        </el-form-item>
        <el-form-item prop="notes" label="备注">
          <el-input v-model="orderDetail.notes" :autosize="{ minRows: 2, maxRows: 4 }" type="textarea"
            placeholder="请输入备注信息" />
        </el-form-item>

        <el-form-item>
          <el-button type="primary" @click="editDtail">确定</el-button>
          <el-button>取消</el-button>
        </el-form-item>
      </el-form>

    </el-dialog>
    <!-- 编辑订单项 end -->


  </div>
</template>

<script lang="ts" setup>
import Table from '@/components/Table/index.vue'
import request from "@/utils/request"
import { Plus } from "@element-plus/icons-vue"
import { isEmpty } from '@/utils/utils'
import { useRouter, useRoute } from 'vue-router'
import { ElMessage, ElMessageBox, FormInstance, FormRules } from 'element-plus'
import { OrderBase, OrderDetail, OrderList } from './interfaces/order-list'

let router = useRouter()
let route = useRoute()

console.log("baseId: ", route.params.id)

let loadingPage = ref(true)
onMounted(async () => {
  let baseId = route.params.id
  if (!isEmpty(baseId)) {
    try {
      const orderListResult = await request.http<IResult<OrderList>>("get_orderList", {}, {}, { id: baseId })
      let orderListData = orderListResult.data

      if (isEmpty(orderListData)) {
        loadingPage.value = true
        return
      }

      formData.id = orderListData?.id as number
      formData.customer = orderListData?.customer as number
      formData.order_base = orderListData?.order_base as number
      formData.order_technology = orderListData?.order_technology as string

      let { customer, order_base } = orderListData as OrderList

      const orderBaseResult = await request.http<IResult<OrderBase>>("get_orderBase", {}, {}, { id: order_base })
      if (!isEmpty(orderBaseResult.data)) {
        let { order_code, model_base_name, order_product } = orderBaseResult.data as OrderBase
        formShow.value.orderValue = `${order_code}-${model_base_name}-${order_product}`
      }

      const customerResult = await request.http<IResult<ICustomer>>("get_customer", {}, {}, { id: customer })
      if (!isEmpty(customerResult.data)) {
        let { name, company_name, contact_number } = customerResult.data as ICustomer
        formShow.value.customerValue = `${name}-${company_name}-${contact_number}`
      }

      const orderDetailResult = await request.http<IResult<OrderDetail[]>>("get_findDetailByList", { list_id: orderListData?.id }, {})
      if (!isEmpty(orderDetailResult.data)) {
        tableData.value = orderDetailResult.data as OrderDetail[]
      }
    } catch (error) {
      console.log(error)
    } finally {
      loadingPage.value = false
    }

  } else {
    loadingPage.value = false
  }
})

// 弹窗
let dialogOrderBaseTableVisible = ref(false)
let dialogCustomerTableVisible = ref(false)
let dialogOrderDetailTableVisible = ref(false)

// 表单Ref
const orderListFormRef = ref<FormInstance>()
const customerDetailFormRef = ref<FormInstance>()

const back = () => {
  router.back()
}

// 表单上显示的数据
let formShow = ref({
  orderValue: "",
  customerValue: "",
})

// 表单实际的值
let formData = reactive<OrderList>({
  id: "",
  order_base: "",
  customer: "",
  order_technology: "",
})


// 表单校验规则
const rules = reactive<FormRules>({
  order_base: [
    { required: true, message: '请选择款号！', trigger: 'blur' }
  ],
  customer: [
    { required: true, message: '请选择客户！', trigger: 'blur' }
  ],
  order_technology: [
    { required: true, message: '请选输入工艺！', trigger: 'blur' }
  ],
})

// 提交表单
const submitForm = async () => {
  let formEl: FormInstance | undefined = orderListFormRef.value
  if (!formEl) return
  const valid = await formEl.validate()
  if (valid) {
    if (isEmpty(tableData.value)) {
      ElMessage.warning("订单项不能为空！")
      return
    }
    const submitData = {
      ...formData,
      "detail": tableData.value
    }
    try {
      const result = await request.http<IResult<any>>("post_orderListEdit", {}, submitData)
      ElMessageBox.alert('编辑成功！', '消息提醒', {
        confirmButtonText: '确定',
        type: "success",
        callback: () => {
          router.back()
        },
      })
    } catch (error) {
      console.error(error)
    }

  }
}

// 选择款号弹窗
let searchOrder = ref("")
let orderPage = reactive<IPageInfo>({
  isPage: true,
  pageCount: 0,
  currentPage: 1,
  pageSize: 0,
  total: 0
})
const selectOrderBase = async () => {
  dialogOrderBaseTableVisible.value = true
  let params = {
    code_or_name: searchOrder.value,
    page: orderPage.currentPage
  }
  let result = await request.http<IPageResult<OrderBase>>("get_orderLike", params)
  if (result.code == 200 && result.data) {
    let data = result.data
    orderBaseData.value = data.results
    orderPage.pageCount = data.pageCount
    orderPage.currentPage = data.currentPage
    orderPage.pageSize = data.pageSize
    orderPage.total = data.total
  }
}
const changeOrderBasePage = async (page: number) => {
  orderPage.currentPage = page
  await selectOrderBase()

}
const handleSelectOrder = (idx: number, order: OrderBase) => {
  console.log(order)
  formData.order_base = order.id
  formShow.value.orderValue = `${order.order_code} - ${order.model_base_name} - ${order.order_product}`
  dialogOrderBaseTableVisible.value = false
}


// 选择客户弹窗相关
let searchCustomer = ref("")
let customerPage = reactive({
  isPage: true,
  pageCount: 0,
  currentPage: 1,
  pageSize: 0,
  total: 0
})
const selectCustomer = async () => {
  dialogCustomerTableVisible.value = true
  let params = {
    search: searchCustomer.value,
    page: orderPage.currentPage
  }
  let result = await request.http<IPageResult<ICustomer>>("get_customerLike", params)
  if (result.code == 200 && result.data) {
    let data = result.data
    customerData.value = data.results
    customerPage.pageCount = data.pageCount
    customerPage.currentPage = data.currentPage
    customerPage.pageSize = data.pageSize
    customerPage.total = data.total
  }
}
const handleSelectCustomer = (idx: number, customer: ICustomer) => {
  formData.customer = customer.id
  formShow.value.customerValue = `${customer.name} - ${customer.company_name} - ${customer.contact_number}`
  dialogCustomerTableVisible.value = false
}

// Table表单定义
const tableData = ref<OrderDetail[]>([])
let totalPrice = ref(0)
watch(() => tableData.value, (newValue) => {
  totalPrice.value = 0
  newValue.forEach(item => {
    item.order_total_price = item.order_price * item.order_number
    totalPrice.value += item.order_total_price
  })
}, {
  immediate: true,
  deep: true
})
const tableTitle = [
  { prop: 'color', lable: "颜色" },
  { prop: 'order_number', lable: "数量" },
  { prop: 'order_price', lable: "单价(元)" },
  { prop: 'order_total_price', lable: "总价(元)" },
  { prop: 'notes', lable: "备注" },
]
const orderBaseData = ref<OrderBase[]>([])
const orderBaseTableTitle = [
  { prop: 'order_code', lable: '款号' },
  { prop: 'order_type_name', lable: '订单类型' },
  { prop: 'model_base_name', lable: '磨具名称' },
  { prop: 'order_product', lable: '产品名称' },
  { prop: 'notes', lable: '备注' },
]
const customerData = ref<ICustomer[]>([])
const customerTableTitle = [
  { prop: 'name', lable: '客户名称' },
  { prop: 'company_name', lable: '公司名称' },
  { prop: 'contact_number', lable: '联系电话' },
  { prop: 'notes', lable: '备注' },
]

let orderDetailTitle = ref("")
let orderDetail = ref<OrderDetail>({
  id: "",
  color: "",
  order_list_id: "",
  notes: "",
  order_number: 0,
  order_price: 0.0,
  temp_id: ""
})

// 表单校验规则
const detailRules = reactive<FormRules>({
  color: [
    { required: true, message: '请输入颜色！', trigger: 'blur' }
  ],
  order_number: [
    { required: true, message: '请输入数量！', trigger: 'blur' }
  ],
  order_price: [
    { required: true, message: '请输入单价！', trigger: 'blur' }
  ],
})
const addOrderDetail = () => {
  dialogOrderDetailTableVisible.value = true
  orderDetailTitle.value = "添加订单项"
  orderDetail.value.temp_id = new Date().getTime() // 临时id
}
const editDtail = async () => {
  let formEl: FormInstance | undefined = customerDetailFormRef.value
  if (!formEl) return
  const valid = await formEl.validate()
  if (!valid) {
    return
  }
  let isTempId = true
  // 是否是临时id
  if (!isEmpty(orderDetail.value.id)) {
    isTempId = false
  }

  let updateIdx = -1

  tableData.value.forEach((item: OrderDetail, idx: number) => {
    if (isTempId) {
      if (!isEmpty(item.temp_id) && item.temp_id == orderDetail.value.temp_id) {
        updateIdx = idx
      }
    } else {
      if (!isEmpty(item.id) && item.id == orderDetail.value.id) {
        updateIdx = idx
      }
    }
  })

  if (updateIdx > -1) {
    tableData.value[updateIdx] = orderDetail.value
  } else {
    tableData.value.push(orderDetail.value)
  }

  orderDetail.value = {
    id: "",
    color: "",
    order_list_id: "",
    notes: "",
    order_number: 0,
    order_price: 0.0,
    temp_id: ""
  }

  dialogOrderDetailTableVisible.value = false
}

const handleEdit = (idx: number, data: OrderDetail) => {
  orderDetail.value = data
  dialogOrderDetailTableVisible.value = true
}
const handleDelete = (idx: number, data: OrderDetail) => {
  let delIdx = -1
  tableData.value.forEach((item: OrderDetail, idx: number) => {
    if (!isEmpty(data.temp_id)) {
      if (!isEmpty(item.temp_id) && data.temp_id == item.temp_id) {
        delIdx = idx
      }
    } else if (!isEmpty(data.id)) {
      if (!isEmpty(item.id) && item.id == data.id) {
        delIdx = idx
      }
    }
  })
  if (delIdx > -1) {
    tableData.value.splice(delIdx, 1)
  }
}

</script>

<style lang="scss" scoped>
@import "./order-list-edit-index.scss"
</style>
