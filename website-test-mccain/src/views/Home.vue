<template>
  <div class="home">
    <h1>Welcome</h1>
    <b-container class="home-layout">
  <b-row>
    <b-col>1 of 3</b-col>
    <b-col><LoginPane /></b-col>
  </b-row>
</b-container>
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
