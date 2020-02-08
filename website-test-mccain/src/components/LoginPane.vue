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
          <b-input type="password" v-model="password"></b-input>
          <router-link to="/myprivatelife/password-reset" :style="{'color': $store.state.textColor}">
              <font size="2">Reset your password</font>
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
