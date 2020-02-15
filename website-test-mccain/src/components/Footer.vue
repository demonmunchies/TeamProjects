<template>
  <b-navbar variant="primary" fixed="bottom">
    <b-col class="col-md-3"></b-col>
    <b-col class="col-md-6"><div id="mytext">My Private Life</div></b-col>
    <b-col class="col-md-1"></b-col>
    <b-col class="col-md-1"><AccessibilityButton /></b-col>
    <b-col class="col-md-1"></b-col>
  </b-navbar>
</template>

<script>
import AccessibilityButton from "../components/AccessibilityButton";
export default {
  components: {
    AccessibilityButton
  }
}
</script>

<style lang="scss">
  #mytext {
    color: #f8f9fa;
    font-family: Comfortaa;
  }
</style>