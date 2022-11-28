//import Vue from "vue";
import { createRouter, createWebHistory } from "vue-router";
import Index from "./components/Index.vue";

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: "/query_result",
      name: "Query",
      components: Index,
    },
    //    {
    //      path: "",
    //      name: "/items/:clusterId",
    //      components:,
    //    },
  ],
});
export default router;
