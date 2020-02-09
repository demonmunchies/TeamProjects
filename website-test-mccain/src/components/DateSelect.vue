<template>
  <div>
    <label for="date-form">Select Date:</label>
    <b-form-input v-model="date" type="date" v-on:input="updateDate"></b-form-input>
  </div>
</template>

<script>
  export default {
    data() {
      return {
        date: ''
      }
    },
    methods: {
      updateDate() {
        this.$store.dispatch("setDate", this.date)
      }
    }
  }
</script>