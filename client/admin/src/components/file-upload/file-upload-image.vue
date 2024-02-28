<template>
  <div class="file-upload-image-container">
    <el-upload
      style="display: none"
      ref="uploadRef"
      action="#"
      :auto-upload="false"
      :on-change="onChangeHandler"
      :show-file-list="false"
    >
      <button type="button" ref="uploadBtn">上传</button>
    </el-upload>
    <div class="img-upload-box">
      <div class="image-list">
        <div
          v-if="Object.keys(imgDict).length < 1"
          class="image-default image-base image-size-md"
          @click="onClickUpload"
        ></div>
        <div
          class="image-base image-size-md"
          v-for="key in Object.keys(imgDict)"
          :key="key"
        >
          <img :src="getImgUrl(imgDict[key])" />
          <div class="image-delete">
            <el-icon @click="handleDelete(key)"><i-ep-delete /></el-icon>
          </div>
        </div>
      </div>
      <ElButton type="primary" @click="onClickUpload">上传</ElButton>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ElMessage, UploadFile, UploadInstance } from "element-plus";
import { generateSimpleUuid } from "@/utils/utils";
import { ref } from "vue";

let props = withDefaults(
  defineProps<{
    count?: number;
    maxSize?: number;
    modelValue: "" | File | File[];
  }>(),
  {
    maxSize: 1024 * 5, // 5M
    count: 1, // -1表示無限制
  }
);
const uploadBtn = ref();

const onClickUpload = () => {
  uploadBtn.value?.click();
};
let { count, modelValue } = toRefs(props);
const isMax = computed(() => {
  if (count.value === -1) {
    return false;
  }
  if (Array.isArray(modelValue.value)) {
    return count.value <= modelValue.value.length;
  } else {
    return typeof modelValue.value !== "string";
  }
});

const imgDict = ref<{ [key: string]: File }>({});
watch(
  () => modelValue.value,
  (nval) => {
    imgDict.value = {};
    if (Array.isArray(nval)) {
      nval.forEach((item) => (imgDict.value[generateSimpleUuid()] = item));
    } else if (typeof nval !== "string") {
      imgDict.value[generateSimpleUuid()] = nval;
    }
  }
);

const uploadRef = ref<UploadInstance>();

const getImgUrl = (img: File) => {
  return URL.createObjectURL(img);
};

const onChangeHandler = (uploadFile: UploadFile, uploadFiles: UploadFile[]) => {
  if (isMax.value) {
    ElMessage.warning("最多只能上传" + count.value + "张图片");
    return;
  }
  // 文件大小
  if (!uploadFile.size || uploadFile.size < props.maxSize) {
    ElMessage.warning("图片大小不能超过" + props.maxSize + "kb");
    return;
  }
  if (Array.isArray(modelValue.value)) {
    emit(
      "update:modelValue",
      uploadFiles.map((item) => item.raw as File)
    );
  } else {
    emit("update:modelValue", uploadFile.raw as File);
  }
};

const handleDelete = (key: string) => {
  if (Array.isArray(modelValue.value)) {
    let files: File[] = [];
    for (const k in Object.keys(imgDict.value)) {
      if (k !== key) {
        files.push(imgDict.value[key]);
      }
    }
    emit("update:modelValue", files);
  } else {
    emit("update:modelValue", "");
  }
};

const emit = defineEmits<{
  (event: "update:modelValue", img: "" | File | File[]): void;
}>();
</script>
<style lang="scss" scoped>
@import "./file-upload-image.scss";
</style>
