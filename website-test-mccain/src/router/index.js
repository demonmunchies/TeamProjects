import Vue from "vue";
import VueRouter from "vue-router";
import RouteNav from "../views/RouteNav.vue";
import Home from "../views/Home.vue";
import ThermostatControls from "../views/ThermostatControls.vue";
import UsageStatistics from "../views/UsageStatistics.vue";
import UserManual from "../views/UserManual.vue";
import Accessibility from "../views/Accessibility.vue";
import SetPassword from "../views/SetPassword.vue"

Vue.use(VueRouter);

const routes = [
  {
    path: "/myprivatelife",
    component: RouteNav,
    children: [
      // Note we provide the above parent route name on the default child tab
      // route to ensure this tab is rendered by default when using named routes
      { path: '', component: Home, name: '/myprivatelife' },
      { path: 'thermostat-controls', component: ThermostatControls},
      { path: 'usage-statistics', component: UsageStatistics},
      { path: 'user-manual', component: UserManual},
      { path: 'accessibility', component: Accessibility},
      { path: 'password-reset', component: SetPassword}
    ]
  }
];

const router = new VueRouter({
  routes
});

export default router;
