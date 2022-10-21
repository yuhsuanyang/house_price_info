<template>
  <div>
    <input v-bind:size="size" />
  </div>
</template>
<script>
export default {
  name: "Input",
  props: {
    size: Number,
  },
};
</script>
<style scoped>
div {
  /*margin-left: 5%;*/
}
input {
  padding: 0.5em;
}
</style>
