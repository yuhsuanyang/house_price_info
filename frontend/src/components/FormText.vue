<template>
  <div>{{ txt }}</div>
</template>
<script>
export default {
  name: "FormText",
  props: {
    txt: String,
  },
};
</script>
<style scoped>
div {
  padding: 1% 0%;
}
</style>
