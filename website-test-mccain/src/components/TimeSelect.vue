<template>
  <div>
    <b-form-input v-model="time" type="time" v-on:click="updateTime"></b-form-input>
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
        console.log(this.time)
        this.$store.scheduleTime = this.time;
      }
    }
  }
</script>