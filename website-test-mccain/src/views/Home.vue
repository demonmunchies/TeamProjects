<template>
  <div class="home" :style="{'background-color': $store.state.backgroundColor, 'color': $store.state.textColor}">
    <b-row class="mb-5">
      <b-col class="col-md"></b-col>
      <b-col class="col-md"><h1 class="welcome-text" :style="{'color': $store.state.textColor}">Welcome</h1></b-col>
      <b-col class="col-md"></b-col>
    </b-row>
    <b-row>
      <b-col class="col-md-6"><img src="../assets/MyPrivateLife_Logo.png" class="logo"></b-col>
      <b-col class="col-md-2"></b-col>
      <b-col class="col-md-3"><LoginPane /></b-col>
      <b-col class="col-md-1"></b-col>
    </b-row>
    <b-row no-gutters>
      <b-col class="col-md-6"><h5 class="logo-text" :style="{'color': $store.state.textColor}">The only system that keeps your data secure </h5> </b-col>
      <b-col class="col-md-6"></b-col>
    </b-row>
    </div>
</template>

<script>
import LoginPane from "../components/LoginPane.vue"
export default {
  name: "home",
  components: {
    LoginPane
  }
};
</script>

<style lang="scss">
.logo {
height: 200px;
}
.logo-text{
  color: #a569bd;
}
.welcome-text{
  color: #a569bd;
}
</style>