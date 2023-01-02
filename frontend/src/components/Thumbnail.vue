<template>
  <div class="boundary">
    <div class="price_label">
      <p>{{ price }}萬</p>
    </div>
    <img v-bind:src="img_src" height="100%" width="100%" />
  </div>
</template>
<script>
export default {
  name: "Thumbnail",
  props: {
    img_src: String,
    price: Number,
  },
};
</script>
<style scoped>
.boundary {
  position: relative;
  display: flex;
  height: 230px;
  width: 300px;
}
.price_label {
  position: absolute;
  background-color: #fa9b0e;
  opacity: 0.75;
  top: 5%;
  font-size: 10px;
  font-weight: 900;
  padding: 0 3%;
}
.price_label > p {
  margin: 1px 2px;
  color: white;
}
</style>
