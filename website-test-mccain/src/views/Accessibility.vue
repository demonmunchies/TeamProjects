<template>
  <div class="accessibility">
    <b-row>
      <b-col></b-col>
      <b-col>
        <div>Background: <AccessibilityColor /></div>
        <div>Text: <AccessibilityColor /></div>
        <div>Graph: <AccessibilityColor /></div>
      </b-col>
      <b-col></b-col>
    </b-row>
    <b-row>
      <b-col>Keyboard Shortcuts:</b-col>
      <b-col></b-col>
      <b-col></b-col>
    </b-row>
  </div>
</template>

<script>
import AccessibilityColor from "../components/AccessibilityColor";
export default {
  name: "accessibility",
  components: {
    AccessibilityColor
  }
};
</script>
