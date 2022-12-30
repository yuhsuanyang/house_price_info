<template>
  <div>
    <img v-bind:src="img_src" height="230" width="350" />
  </div>
</template>
<script>
export default {
  name: "Thumbnail",
  props: {
    img_src: String,
  },
};
</script>
<style scoped></style>
