<template>
  <div>
    <b-form-input v-model="time" placeholder="Enter your name"></b-form-input>
    <div class="mt-2">Value: {{ text }}</div>
  </div>
</template>

<script>
  export default {
    data() {
      return {
        time: ''
      }
    }
  }
</script>