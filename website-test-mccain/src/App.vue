<template>
  <div id="app">
    <body>
    <header><NavBar /></header>
    <section class="main-content"><router-view></router-view></section>
    <footer>...</footer>
</body>

  </div>
</template>

<script>
// @ is an alias to /src
import NavBar from "@/components/NavBar.vue"
export default {
  name: "app",
  components: {
    NavBar
  },
};
</script>

<style lang="scss">
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
