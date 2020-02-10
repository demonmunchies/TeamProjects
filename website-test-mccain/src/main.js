import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import {store} from "./store/store";
import "./custom.scss";
import { BootstrapVue, IconsPlugin} from "bootstrap-vue";

Vue.use(BootstrapVue);
Vue.use(IconsPlugin)
Vue.use(require('vue-shortkey'))
Vue.config.productionTip = false;

new Vue({
  store: store,
  router,
  render: h => h(App)
}).$mount("#app");
