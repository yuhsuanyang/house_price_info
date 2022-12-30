<template>
  <div class="content">
    <div class="nav">
      <div>
        <router-link to="/"
          ><img src="../assets/logo_bird.png" class="logo"
        /></router-link>
      </div>
      <div>
        <p>查看喜歡</p>
      </div>
      <div>
        <p>排序</p>
      </div>
    </div>
    <div class="container">
      <!--      <Thumbnail
        img_src="https://img1.591.com.tw/house/2022/12/08/167050412587925907.jpg!1000x.water2.jpg"
      />-->
      <Thumbnail :img_src="img_url" />
    </div>
  </div>
</template>
<script>
import Thumbnail from "./Thumbnail.vue";
import SampleData from "../sample_data.json";
export default {
  name: "QueryResult",
  components: {
    Thumbnail,
  },
  props: {
    data: SampleData,
  },
  data() {
    return {
        img_url: "",
    };
  },
  created() {
    this.img_url=SampleData["1343"][0]["img_url"][0];
    console.log(this.img_url);
  },
};
</script>
<style scoped>
.content {
  background-color: aliceblue;
  /*  display: flex;*/
}
.nav {
  background-color: white;
  display: flex;
  gap: 2%;
  border-bottom: 5px solid #faf8f8;
}
.logo {
  height: 60px;
}
.nav > div {
  height: 60px;
  display: flex;
  font-weight: bold;
}
p {
  margin: auto;
}
.container {
  display: flex;
  gap: 2%;
  padding: 2% 5%;
}
</style>
