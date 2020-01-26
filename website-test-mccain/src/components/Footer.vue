<template>
  <div class="footer">
    <b-row no-gutters="true">
      <b-col cols="3">3</b-col>
      <b-col cols="6">6</b-col>
      <b-col cols="2">2</b-col>
      <b-col cols="1"><AccessibilityButton /></b-col>
    </b-row>
  </div>
</template>

<script>
import AccessibilityButton from "./AccessibilityButton.vue";
export default {
  name: "footer",
  components: {
    AccessibilityButton
  }
};
</script>

<style lang="scss">
.footer {
  background-color: #8e44ad;
  color: white;
}
</style>
