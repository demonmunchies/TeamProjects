<template>
  <div>
    <b-form-input v-model="time" type="time" v-on:input="updateTime"></b-form-input>
  </div>
</template>

<script>
  export default {
    data() {
      return {
        time: ''
      }
    },
    methods: {
      updateTime() {
        this.$store.dispatch("setScheduleTime", this.time)
      }
    }
  }
</script>