<template>
  <div class="accessibility">
    <b-row>
      <b-col></b-col>
      <b-col>
        <div>Background: <AccessibilityBackgroundColor /></div>
        <div>Text: <AccessibilityTextColor /></div>
      </b-col>
      <b-col></b-col>
    </b-row>
    <b-row class="mb-5"></b-row>
    <b-row>
      <b-col>Keyboard Shortcuts:</b-col>
      <b-col></b-col>
      <b-col></b-col>
    </b-row>
  </div>
</template>

<script>
import AccessibilityBackgroundColor from "../components/AccessibilityBackgroundColor";
import AccessibilityTextColor from "../components/AccessibilityTextColor";
export default {
  name: "accessibility",
  components: {
    AccessibilityBackgroundColor,
    AccessibilityTextColor
  }
};
</script>
