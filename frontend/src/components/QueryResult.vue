<template>
  <div>
    <div class="nav">
      <div>
        <router-link to="/"
          ><img src="../assets/logo_bird.png" class="logo"
        /></router-link>
      </div>
      <div><p>查看喜歡</p></div>
      <div><p>排序</p></div>
    </div>
    <div class="content">
      <div class="description">
        <p>台北市, 文山區, 屋齡0~20年, 權狀0~40坪, 不限格局, 共7個物件</p>
      </div>
      <div style="display: flex">
        <div style="width: 200px; height: 80vh">
          <div class="top">
            <img src="../assets/top.png" style="width: 30%" />
          </div>
        </div>
        <div class="container">
          <div v-for="item in clusters" :key="item.id">
            <Thumbnail
              :img_src="item['img_url'][sample(item['img_url'])]"
              :price="item['price']"
            />
          </div>
        </div>
      </div>
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
      clusterId: [],
      clusters: {},
    };
  },
  methods: {
    sample(arr) {
      var x = Math.floor(Math.random() * arr.length);
      return x;
    },
  },
  created() {
    this.img_url = SampleData["1343"][0]["img_url"][0];
    for (var key in SampleData) {
      //        this.clusterId.push(key);
      var data = SampleData[key];
      this.clusters[key] = {
        address: data[0]["region_name"].concat(
          data[0]["section_name"],
          data[0]["address"]
        ),
        price: data[0]["price"],
        room: data[0]["room"],
        floor: data[0]["floor"],
        houseage: data[0]["houseage"],
        img_url: data[0]["img_url"],
      };
      for (var i in data) {
        var item = data[i];
        this.clusters[key]["img_url"].push(...item["img_url"]);
      }
    }
    console.log(this.clusters);
  },
};
</script>
<style scoped>
.content {
  background-color: #eff4fd;
  /*  display: flex;*/
}
.nav {
  background-color: white;
  display: flex;
  gap: 2%;
  border-bottom: 5px solid #faf8f8;
}
.logo {
  height: 10vh;
}
.nav > div {
  height: 10vh;
  display: flex;
  font-weight: bold;
}
p {
  margin: auto;
}
.container {
  display: flex;
  flex-wrap: wrap;
  align-content: flex-start;
  padding-left: 10%;
}
.container > div {
  margin: 3px;
}
.description {
  font-size: 8px;
  text-align: left;
  padding: 2%;
}
.top {
  position: fixed;
  bottom: 5%;
  left: 0;
}
</style>
