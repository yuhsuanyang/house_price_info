<template>
  <div>
    <input
      v-bind:placeholder="txt"
      v-bind:size="size"
      v-bind:value="data"
      @input="$emit('input', $event.target.value)"
    />
  </div>
</template>
<script>
export default {
  name: "Input",
  model: {
    prop: "data",
  },
  props: {
    size: Number,
    txt: Number,
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
