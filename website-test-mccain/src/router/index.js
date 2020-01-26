import Vue from "vue";
import VueRouter from "vue-router";
import RouteNav from "../views/RouteNav.vue"
import Home from "../views/Home.vue";
import About from "../views/About.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/myprivatelife",
    component: RouteNav,
    children: [
      // Note we provide the above parent route name on the default child tab
      // route to ensure this tab is rendered by default when using named routes
      { path: '', component: Home, name: '/myprivatelife' },
      { path: 'about', component: About}
    ]
  }
];

const router = new VueRouter({
  routes
});

export default router;
