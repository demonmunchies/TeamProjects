<template>
  <div>
    <label for="range-form">Display Interval:</label>
    <b-form-select v-model="selected" :options="options" v-on:input="updateRange"></b-form-select>
  </div>
</template>

<script>
  export default {
    data() {
      return {
        selected: null,
        options: [
          { value: null, text: 'Please select a time frame' },
          { value: 'day', text: 'Day' },
          { value: 'week', text: 'Week' },
          { value: 'month', text: 'Month' },
          { value: 'year', text: 'Year' }
        ]
      }
     },
     methods: {
      updateRange() {
        this.$store.dispatch("setRange", this.selected)
      }
    }
  }
</script>