<template>
  <div>
    <label for="range-1">Temperature (F)</label>
    <b-form-input id="range-1" v-model="temp" type="range" v-on:input="updateTemp" min="60" max="85"></b-form-input>
    <div class="mt-2">{{ temp }} </div>
  </div>
</template>

<script>
  export default {
    data() {
      return {
        temp: '72'
      }
    },
    methods: {
      updateTemp() {
        this.$store.dispatch("setScheduleTemp", this.temp)
      }
    }
  }
</script>