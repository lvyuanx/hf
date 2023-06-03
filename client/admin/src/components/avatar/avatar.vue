<template>
  <el-upload
    ref="upload"
    action="#"
    list-type="picture-card"
    :auto-upload="false"
    :limit="1"
    :on-exceed="handleExceed"
    :on-change="handleChange"
  >
    <el-icon>
      <Plus />
    </el-icon>
    <template #file="{ file }">
      <div>
        <img class="el-upload-list__item-thumbnail" :src="file.url" alt="" />
        <span class="el-upload-list__item-actions">
          <span class="el-upload-list__item-preview" @click="handlePictureCardPreview(file)">
            <el-icon><zoom-in /></el-icon>
          </span>
          <span v-if="!disabled" class="el-upload-list__item-delete" @click="handleRemove(file)">
            <el-icon>
              <Delete />
            </el-icon>
          </span>
        </span>
      </div>
    </template>
  </el-upload>

  <el-dialog v-model="dialogVisible">
    <img w-full :src="dialogImageUrl" alt="Preview Image" />
  </el-dialog>
</template>
<script lang="ts" setup>
import { ref } from "vue";
import { Delete, Download, Plus, ZoomIn } from "@element-plus/icons-vue";
import defaultAvatar from "@/assets/img/avatar.png";

import {
  UploadFile,
  UploadFiles,
  UploadInstance,
  UploadProps,
  UploadRawFile,
  UploadUserFile,
  genFileId
} from "element-plus";

defineProps<{
  avatar?: UploadFile | null;
}>();
const loadDefaultRawFile = () => {
  // 创建一个 Blob 对象，并将其转化为可用的 URL 地址
  const blob = new Blob([defaultAvatar], { type: "image/jpeg" });

  // 使用 File 构造函数创建一个 File 对象
  const file = new File([blob], "default-image.jpg", { type: "image/jpeg" });

  const uploadRawFile: UploadRawFile = {
    uid: new Date().getTime(),
    ...file
  };

  // 创建一个 UploadRawFile 对象
  upload.value?.handleStart(uploadRawFile);
};

onMounted(() => {
  loadDefaultRawFile();
});

// 子传父要此案定义好emit
const emit = defineEmits<{
  // update:xxx 固定写法，用于修改父组件中v-model绑定的值
  (event: "update:avatar", avatar: UploadFile | null): void;
}>();

const dialogImageUrl = ref("");
const dialogVisible = ref(false);
const disabled = ref(false);
const upload = ref<UploadInstance>();
let currentAvatar = ref<UploadFile | null>(null);

const handleExceed: UploadProps["onExceed"] = files => {
  upload.value!.clearFiles();
  const file = files[0] as UploadRawFile;
  file.uid = genFileId();
  upload.value!.handleStart(file);
};

const handleRemove = (file: UploadFile) => {
  upload.value!.handleRemove(file);
  currentAvatar.value = null;
  emit("update:avatar", null);
};

const handlePictureCardPreview = (file: UploadFile) => {
  dialogImageUrl.value = file.url!;
  dialogVisible.value = true;
};

const handleChange = (uploadFile: UploadFile) => {
  currentAvatar.value = uploadFile;
  emit("update:avatar", uploadFile);
};
</script>
