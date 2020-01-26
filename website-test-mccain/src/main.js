import Vue from "vue";
import App from "./App.vue";
import "./custom.scss";
import { BootstrapVue } from "bootstrap-vue";
import router from "./router";

// Install BootstrapVue
Vue.use(BootstrapVue);
Vue.config.productionTip = false;

new Vue({
  router,
  render: h => h(App)
}).$mount("#app");
