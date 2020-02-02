<template>
  <div>
    <b-form  @submit.stop.prevent>
      <b-input type="password" v-model="userId" :state="validation" id="confirm-password"></b-input>
      <b-form-invalid-feedback :state="validation">
        Your password must be 5-12 characters long.
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
        userId: ''
      }
    },
    computed: {
      validation() {
        return this.userId.length > 4 && this.userId.length < 13
      }
    }
  }
</script>