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
        <div v-for="i in clusters" :key="i.id">
          <Thumbnail :img_src="i['img_url'][0]"/>
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
  created() {
    this.img_url=SampleData["1343"][0]["img_url"][0];
    for (var key in SampleData){
//        this.clusterId.push(key);
        var data = SampleData[key]
        this.clusters[key] = {
            "address": data[0]["region_name"].concat(data[0]["section_name"], data[0]["address"]),
            "price": data[0]["price"],
            "room": data[0]["room"],
            "floor": data[0]["floor"],
            "houseage": data[0]["houseage"],
            "img_url": data[0]["img_url"]
        }
        for (var i in data){
            var item = data[i]
            this.clusters[key]["img_url"].push(...item["img_url"])
        }
    }
    console.log(this.clusters);
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
  flex-wrap: wrap;
  gap: 2%;
  padding: 2% 5%;
}
</style>
