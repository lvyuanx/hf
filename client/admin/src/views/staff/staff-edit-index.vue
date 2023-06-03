<template>
  <div class="staff-edit-container">
    <el-form ref="staffFormRef" :model="staffData" :rules="rules" label-width="220px">
      <el-form-item label="员工头像：" prop="avatar">
        <Avatar v-model:avatar="avatarUploadFile"></Avatar>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="submitForm">确定</el-button>
        <el-button @click="back">返回</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script lang="ts" setup>
import { StaffBase } from "./interfaces/staff";
import Avatar from "@/components/avatar/avatar.vue";
import { FormInstance, FormRules, UploadFile } from "element-plus";
import { useRouter } from "vue-router";

let router = useRouter();

let staffData = reactive<StaffBase>({
  user: {
    username: "",
    password: ""
  },
  staff_code: "",
  phone_number: "",
  avatar: null,
  notes: ""
});

let avatarUploadFile = ref<UploadFile | null>(null);

watch(
  () => avatarUploadFile.value,
  n => {
    if (n?.raw) {
      staffData.avatar = n.raw;
    }
  }
);

const staffFormRef = ref<FormInstance>();
// 表单校验规则
const rules = reactive<FormRules>({
  avatar: [{ required: true, message: "请上传头像！", trigger: "blur" }]
});
const submitForm = async () => {
  let formEl: FormInstance | undefined = staffFormRef.value;
  if (!formEl) return;
  const valid = await formEl.validate();
  if(!valid) {
    return
  }
};
const back = () => {
  router.back();
};
</script>

<style lang="scss" scoped>
@import "./staff-edit-index.scss";
</style>
