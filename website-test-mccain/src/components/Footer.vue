<template>
  <footer class="myFooter">
    <b-row class="mb-1"></b-row>
    <b-row no-gutters=true>
    <b-col cols="3"></b-col>
    <b-col cols="6">My Private Life</b-col>
    <b-col cols="1"></b-col>
    <b-col cols="1"><AccessibilityButton /></b-col>
    <b-col cols="1"></b-col>
  </b-row>
</footer>
</template>

<script>
import AccessibilityButton from "./AccessibilityButton.vue";
export default {
  name: "myFooter",
  components: {
    AccessibilityButton
  }
};
</script>

<style lang="scss">
.myFooter {
  position: absolute;
  bottom: 0;
  width: 100%;
  /* Set the fixed height of the footer here */
  height: 60px;
  color: #f8f9fa;
  font-family: Comfortaa;
  font-size: .8 rem;
  background-color: #8e44ad;
}
</style>

