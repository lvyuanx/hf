<template>
  <div class='appBox'>
    <router-view></router-view>
  </div>
</template>

<script lang="ts" setup>
import { ref } from "vue"

</script>

<style lang="scss" scoped>
.appBox {
  width: 100%;
  height: 100%;
  background-color: #f1f1f1;
  padding: 1vmax;
}
</style>
