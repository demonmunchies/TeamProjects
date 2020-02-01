<template>
  <div class="set-password">
    <h1>Reset Your Passsword</h1>
    <b-row>
      <b-col></b-col>
      <b-col>
        <div> Passsword <PasswordSetForm /> </div>
        <div> Retype Passsword <PasswordSetForm /> </div>
        <div><b-button>Submit</b-button></div>
      </b-col>
      <b-col></b-col>
    </b-row>
  </div>
</template>

<script>
import PasswordSetForm from "../components/PasswordSetForm"
export default {
  name: "set-password",
  components: {
    PasswordSetForm
  }
};
</script>
