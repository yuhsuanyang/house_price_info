<template>
  <div>
    <input
      v-bind:list="list_name"
      v-bind:placeholder="txt"
      v-bind:size="size"
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
  props: {
    txt: String,
    list_name: String,
    size: Number,
    values: Array,
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
