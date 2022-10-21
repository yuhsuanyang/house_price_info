<template>
  <div>{{ txt }}</div>
</template>
<script>
export default {
  name: "FormHeader",
  props: {
    txt: String,
  },
};
</script>
<style scoped>
div {
  border-right: 5px solid #aacaff;
  padding: 1% 1em;
}
</style>
