<template>
  <div id="app">
  <b-row>
    <b-col cols="12">
      <Navbar />
      <b-row rows id="test">
        kkkkk
      </b-row>
      <b-row>
        <b-col cols="12">
          <Footer />
        </b-col>
      </b-row>
    </b-col>
  </b-row>
  </div>
</template>

<script>
import Navbar from "./components/Navbar.vue";
import Footer from "./components/Footer.vue";
export default {
  name: "app",
  components: {
    Navbar,
    Footer
  }
};
</script>

<style lang="scss">
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 0px;
  margin-bottom: 0px;
}


</style>
