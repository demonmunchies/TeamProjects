<template>
  <b-container class="login">
    <b-row><h3>Login:</h3></b-row>
    <b-row><ActivationForm /></b-row>
    <b-row><PasswordForm  /></b-row>
</b-container>
</template>

<script>
// @ is an alias to /src
import ActivationForm from "./ActivationForm.vue";
import PasswordForm from "./PasswordForm.vue"
export default {
  name: "login-pane",
  components: {
      ActivationForm,
      PasswordForm
  }
};
</script>