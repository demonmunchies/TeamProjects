<template>
  <div>
    <b-form-input v-model="color" type="color" v-on:input="updateBackgroundColor"></b-form-input>
  </div>
</template>

<script>
  export default {
    data() {
      return {
        color: this.$store.state.backgroundColor
      }
    },
    methods: {
      updateBackgroundColor() {
        this.$store.dispatch("setBackgroundColor", this.color)
      }
    }
  }
</script>