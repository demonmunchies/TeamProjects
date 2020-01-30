<template>
  <div>
    <b-form  @>
      <label for="feedback-temp">User ID</label>
      <b-input v-model="temp" :state="validation" id="feedback-user"></b-input>
      <b-form-invalid-feedback :state="validation">
        The temperature must be a 2-digit positive whole number
      </b-form-invalid-feedback>
      <b-form-valid-feedback :state="validation">
        Looks Good.
      </b-form-valid-feedback>
     </b-form>
  </div>
</template>

<script>
  export default {
    data() {
      return {
        temp: ''
      }
    },
    computed: {
      validation() {
        return this.temp.length == 2 && this.temp.length < 13
      }
    }
  }
</script>