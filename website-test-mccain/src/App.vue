<template>
  <div id="app" :style="{ 'background-color': $store.state.backgroundColor, 'color': $store.state.textColor}">
    <NavBar />
    <b-row class="mb-3">
    </b-row>
    <router-view></router-view>
    <Footer />
  </div>
</template>

<script>
// @ is an alias to /src
import NavBar from "@/components/Navbar.vue"
import Footer from "@/components/Footer.vue"
export default {
  name: "app",
  components: {
    NavBar,
    Footer
  },
};
</script>

<style lang="scss">
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  height: 100vh;
}
</style>
