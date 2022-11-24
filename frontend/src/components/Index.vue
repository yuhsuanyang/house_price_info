<template>
  <div>
    <img src="../assets/logo_bird.png" class="content_width" />
    <form id="form" class="content_width">
      <div class="row">
        <div class="cell" style="width: 100%">
          <FormHeader txt="位置" />
          <DropDown
            txt="選擇縣市"
            list_name="city"
            :values="cities"
            v-model="selectedCity"
          />
          <DropDown
            txt="選擇行政區"
            list_name="district"
            :values="districts"
            v-model="selectedDistrict"
          />
        </div>
      </div>
      <div class="row">
        <div class="cell" style="width: 50%">
          <FormHeader txt="格局" />
          <DropDown
            txt="選擇房數"
            list_name="pattern"
            :values="rooms"
            size="10"
            v-model="selectedRoom"
          />
          <FormText txt="房" />
        </div>
        <div class="cell" style="width: 50%">
          <FormHeader txt="面積" />
          <Input size="5" txt="0" v-model="areaMin" />
          <FormText txt="~" />
          <Input size="5" v-model="areaMax" />
          <FormText txt="坪" />
        </div>
      </div>
      <div class="row">
        <div class="cell" style="width: 50%">
          <FormHeader txt="屋齡" />
          <Input size="5" txt="0" v-model="ageMin" />
          <FormText txt="~" />
          <Input size="5" v-model="ageMax" />
          <FormText txt="年" />
        </div>
        <div class="cell" style="width: 50%">
          <FormHeader txt="售金" />
          <Input size="5" txt="0" v-model="priceMin" />
          <FormText txt="~" />
          <Input size="5" v-model="priceMax" />
          <FormText txt="萬" />
        </div>
      </div>
    </form>
    <div class="tools">
      <div>
        <!--<button form="form" type="submit" @click="submitForm()">-->
        <button @click="submitForm()">
          <img src="../assets/search.png" />
          <p>搜尋中古屋</p>
        </button>
      </div>
      <div>
        <button onclick='window.location.href = "url here"'>
          <img src="../assets/like.png" />
          <p>查看喜歡</p>
        </button>
      </div>
      <div>
        <button>
          <img src="../assets/update.png" />
          <p>更新資料庫</p>
        </button>
      </div>
    </div>
  </div>
</template>
<script>
import FormHeader from "./FormHeader.vue";
import FormText from "./FormText.vue";
import DropDown from "./DropDown.vue";
import Input from "./Input.vue";
export default {
  name: "Index",
  components: {
    FormHeader,
    FormText,
    DropDown,
    Input,
  },
  data() {
    return {
      cities: [],
      selectedCity: "",
      sections: {},
      districts: [],
      selectedDistrict: "",
      rooms: ["不限", "1", "2", "3", "4", "5"],
      selectedRoom: "",
      areaMin: "0",
      areaMax: "",
      ageMin: "0",
      ageMax: "",
      priceMin: "0",
      priceMax: "",
    };
  },
  methods: {
    async getData() {
      try {
        const response = await this.$http.get(
          "http://127.0.0.1:8327/api1/sections"
        ); //上面執行完了才會執行下面的
        //console.log(response.data);
        this.sections = response.data;
        this.cities = Object.keys(this.sections);
      } catch (error) {
        console.log(error);
      }
    },
    async submitForm() {
      let queryArgs = {
        region: this.selectedCity,
        section: this.selectedDistrict,
        rooms: this.selectedRoom,
        area_min: this.areaMin,
        area_max: this.areaMax,
        age_min: this.ageMin,
        age_max: this.ageMax,
        price_min: this.priceMin,
        price_max: this.priceMax,
      };
      console.log(queryArgs);
      try {
        const response = await this.$http.post(
          "http://127.0.0.1:8327/query/",
          queryArgs
        );
        console.log(response);
      } catch (error) {
        console.log(error);
      }
    },
    logUpdate(newValue) {
      console.log(newValue);
    },
  },
  watch: {
    selectedCity: function () {
      this.logUpdate(this.selectedCity);
      this.districts = this.sections[this.selectedCity];
    },
    selectedDistrict: function () {
      this.logUpdate(this.selectedDistrict);
    },
  },
  created() {
    this.getData();
  },
};
</script>
<style>
body {
  min-width: 700px;
  margin: 0;
  font-size: 16px;
}
#form {
  margin: auto;
  font-size: 1em;
}
.row {
  display: flex;
  margin: 5% 0%;
  /*  justify-content: space-between;*/
}
.cell {
  display: flex;
  gap: 1em;
  justify-content: flex-start;
}
.tools {
  display: flex;
  gap: 1em;
  justify-content: center;
}
.content_width {
  width: 45%;
}
@media screen and (max-width: 1200px) {
  .content_width {
    width: 55%;
  }
}
@media screen and (max-width: 1000px) {
  .content_width {
    width: 70%;
  }
}
@media screen and (max-width: 800px) {
  .content_width {
    width: 90%;
  }
}
button {
  border: none;
  background-color: white;
}
button > p {
  margin: 0;
}
button > img {
  margin: auto;
  width: 1.5em;
}
</style>
