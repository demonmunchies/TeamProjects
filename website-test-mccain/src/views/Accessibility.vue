<template>
  <div class="accessibility">
    <b-row>
      <b-col class="col-md"></b-col>
      <b-col class="col-md">
        <div>Background: <AccessibilityBackgroundColor /></div>
        <div>Text: <AccessibilityTextColor /></div>
      </b-col>
      <b-col class="col-md"></b-col>
    </b-row>
    <b-row class="mb-5"></b-row>
    <b-row>
      <b-col class="col-md text-right">Keyboard Shortcuts:</b-col>
      <b-col class="col-md text-left">
        <div> ctrl + l: Rotate webpage left</div>	
        <div> ctrl + r: Rotate webpage right</div>
        <div> ctrl + a: Open Accessibility Settings</div>
        <div> ctrl + m: Return to homepage</div>	
        <div> ctrl + up arrow: Increase Temperature</div>	
        <div> ctrl + down arrow: Decrease Temperature</div>
      </b-col>
      <b-col class="col-md-1"></b-col>
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
