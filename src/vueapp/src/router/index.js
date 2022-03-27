import { createRouter, createWebHistory } from "vue-router";
import Home from "../views/Home.vue";
import TestView from "../views/TestView.vue";
import PokemonView from "../views/PokemonView.vue";
import DevelopView from "../views/DevelopView.vue";

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/about",
    name: "About",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/About.vue"),
  },
  {
    path: "/test",
    name: "test",
    component: TestView,
  },
  {
    path: "/pokemon",
    name: "pokemon",
    component: PokemonView,
  },
  {
    path: "/develop",
    name: "develop",
    component: DevelopView,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
