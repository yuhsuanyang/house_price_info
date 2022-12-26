import Vue from "vue";
import VueRouter from "vue-router";
import Index from "./components/Index.vue";
import HelloWorld from "./components/HelloWorld.vue";
//import QueryResult from "./components/QueryResult.vue";

Vue.use(VueRouter);
export default new VueRouter({
  mode: "history",
  routes: [
    {
      path: "/",
      name: "Index",
      component: Index,
    },
    {
      path: "/query_result",
      name: "Query",
      component: HelloWorld,
      //      components: QueryResult,
    },
  ],
});
