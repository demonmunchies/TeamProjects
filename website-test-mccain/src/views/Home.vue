<template>
  <div class="home">
    <h1>Welcome</h1>
  <b-row no-gutters=true>
    <b-col cols ="6"><img src="../assets/MyPrivateLife_Logo.jpg" class="logo"></b-col>
    <b-col cols="3"></b-col>
    <b-col cols="3"><LoginPane /></b-col>
  </b-row>
  <b-row no-gutters=true>
    <b-col cols ="6"><h5 class="logo-text">The only system that keeps your data secure </h5> </b-col>
    <b-col cols="6"></b-col>
  </b-row>
  </div>
</template>

<script>
// @ is an alias to /src
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
</style>