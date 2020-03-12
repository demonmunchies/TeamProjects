<template>
  <div>
    <b-form-input v-model="color" type="color" v-on:input="updateTextColor"></b-form-input>
  </div>
</template>

<script>
  export default {
    data() {
      return {
        color: this.$store.state.textColor
      }
    },
    methods: {
      updateTextColor() {
        this.$store.dispatch("setTextColor", this.color)
      }
    }
  }
</script>