//import Vue from "vue";
import { createRouter, createWebHistory } from "vue-router";
import Index from "./components/Index.vue";
import HelloWorld from "./components/HelloWorld.vue";
//import QueryResult from "./components/QueryResult.vue";

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: "/",
      name: "Index",
      componenets: Index,
    },
    {
      path: "/query_result",
      name: "Query",
      components: HelloWorld,
      //      components: QueryResult,
    },
    //    {
    //      path: "",
    //      name: "/items/:clusterId",
    //      components:,
    //    },
  ],
});
export default router;
