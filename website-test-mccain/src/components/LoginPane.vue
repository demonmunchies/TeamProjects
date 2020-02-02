<template>
  <b-container class="login">
    <b-row><h3>Login:</h3></b-row>
    <b-row>
      <div>
        <label for="text-activation-key">Activation Key</label>
        <b-form-input v-model="activationKey" placeholder="XXX-XXX-XXX"></b-form-input>
      </div>
    </b-row>
    <b-row>  
      <div>
        <b-form>
          <label for="text-password">Password</label>
          <b-input type="password" v-model="password" aria-describedby="password-reset-block"></b-input>
          <router-link to="/myprivatelife/password-reset">
            <b-form-text id="password-reset-block">
              Reset your password
            </b-form-text>
          </router-link>
        </b-form>
      </div>
    </b-row>
    <b-row><b-button>Submit</b-button></b-row>
</b-container>
</template>

<script>
// @ is an alias to /src
export default {
  name: "login-pane",
  data() {
    return {
      activationKey: '',
      password: ''
    }
  }
};
</script>