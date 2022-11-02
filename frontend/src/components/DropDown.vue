<template>
  <div>
    <input
      v-bind:list="list_name"
      v-bind:placeholder="txt"
      v-bind:size="size"
      v-bind:value="data"
      @input="$emit('input', $event.target.value)"
    />
    <datalist v-bind:id="list_name">
      <option
        v-for="(item, i) in values"
        v-bind:key="i"
        v-bind:value="item"
      ></option>
    </datalist>
  </div>
</template>
<script>
export default {
  name: "DropDown",
  model: {
    prop: "data",
  },
  props: {
    txt: String,
    list_name: String,
    size: Number,
    values: Array,
    data: { type: String },
  },
};
</script>
<style scoped>
div {
  /*  margin-left: 5%;*/
}
input {
  padding: 0.5em;
}
</style>
