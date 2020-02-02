<template>
  <div class="set-password">
    <h1>Reset Your Passsword</h1>
    <b-row>
      <b-col></b-col>
      <b-col>
        <div> Passsword <PasswordSetForm /> </div>
        <div> Retype Passsword <PasswordConfirmForm /> </div>
        <div><b-button @click="handleClick">Submit</b-button></div>
      </b-col>
      <b-col></b-col>
    </b-row>
  </div>
</template>

<script>
import PasswordSetForm from "../components/PasswordSetForm"
import PasswordConfirmForm from "../components/PasswordConfirmForm"
export default {
  name: "set-password",
  components: {
    PasswordSetForm,
    PasswordConfirmForm
  },
  methods: {
    handleClick: function() {
      alert(PasswordSetForm.userID)
    }
  }
};
</script>
