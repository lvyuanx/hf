<template>
  <div class="staff-edit-container">
    <el-form
      ref="staffFormRef"
      :model="staffData"
      :rules="rules"
      label-width="150px"
    >
      <el-form-item label="员工头像：" prop="avatar">
        <FileUpload v-model="staffData.avatar"></FileUpload>
      </el-form-item>
      <el-form-item label="真实姓名：" prop="fullname">
        <el-input v-model="staffData.fullname" />
      </el-form-item>
      <el-form-item label="员工编号:" prop="staff_code">
        <el-input v-model="staffData.staff_code" />
      </el-form-item>
      <el-form-item label="员工手机号:" prop="phone_number">
        <el-input v-model="staffData.phone_number" />
      </el-form-item>
      <el-form-item label="备注:" prop="notes">
        <el-input v-model="staffData.notes" />
      </el-form-item>
      <el-form-item label="员工权限:" prop="role_lst">
        <el-checkbox-group v-model="staffData.role_lst">
          <el-checkbox
            v-for="item in staffTypes"
            :key="item.id"
            :label="item.id"
            >{{ item.notes }}</el-checkbox
          >
        </el-checkbox-group>
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
import FileUpload from "@/components/file-upload/file-upload-image.vue";
import request from "@/utils/request";
import { FormInstance, FormRules, UploadFile } from "element-plus";
import { de } from "element-plus/es/locale";
import { useRouter } from "vue-router";

let router = useRouter();

let staffData = reactive<StaffBase>({
  avatar: "",
  fullname: "",
  staff_code: "",
  role_lst: [],
});

const staffTypes = ref<any>([]);

let avatarUploadFile = ref<UploadFile | null>(null);

watch(
  () => avatarUploadFile.value,
  (n) => {
    if (n?.raw) {
      staffData.avatar = n.raw;
    }
  }
);

const staffFormRef = ref<FormInstance>();
// 表单校验规则
const rules = reactive<FormRules>({
  fullname: [
    { required: true, message: "请输入员工真实姓名！", trigger: "blur" },
  ],
  staff_code: [
    { required: true, message: "请输入员工编号！", trigger: "blur" },
  ],
  role_lst: [
    {
      validator(rule, value, callback, source, options) {
        if (value.length < 1) {
          return callback(new Error("请最少选择一个权限"));
        }
        callback();
      },
      trigger: "blur",
    },
  ],
});
const submitForm = async () => {
  let formEl: FormInstance | undefined = staffFormRef.value;
  if (!formEl) return;
  const valid = await formEl.validate();
  if (!valid) {
    return;
  }
  const formData = new FormData();
  formData.append("avatar", staffData.avatar as File);
  formData.append("fullname", staffData.fullname);
  formData.append("staff_code", staffData.staff_code);
  formData.append("phone_number", staffData.phone_number || "");
  formData.append("notes", staffData.notes || "");
  formData.append("role_lst", JSON.stringify(staffData.role_lst));

  const result = await request.http<IResult<any>>(
    "upload_staffEdit",
    {},
    formData
  );
  if (result.code === 200) {
    ElMessage.success("保存成功");
    back();
  } else {
    ElMessage.error(result.msg);
  }
};

const getRoleLiteList = async () => {
  const result = await request.http<IResult<any>>("get_roleLiteList");
  staffTypes.value = result.data;
};
onMounted(() => {
  getRoleLiteList();
});

const back = () => {
  router.back();
};
</script>

<style lang="scss" scoped>
@import "./staff-edit-index.scss";
</style>
