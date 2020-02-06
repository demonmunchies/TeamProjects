<template>
  <div>
    <label for="range-1">Temperature (F)</label>
    <b-form-input id="range-1" v-model="value" type="range" v-on:input="updateTemperature" min="60" max="85"></b-form-input>
    <div class="mt-2">{{ value }} </div>
  </div>
</template>

<script>
  export default {
    data() {
      return {
        value: '72'
      }
    },
    methods: {
      updateTemperature() {
        this.$store.scheduleTemp = this.value;
      }
    }
  }
</script>