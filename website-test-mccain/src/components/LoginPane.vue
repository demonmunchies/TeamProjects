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
    <b-row><b-button v-on:click="loginCheck" v-shortkey="['ctrl', 'enter']" @shortkey="loginCheck">Submit</b-button></b-row>
    <p>{{ clickText }}</p>
</b-container>
</template>

<script>
// @ is an alias to /src
export default {
  name: "login-pane",
  data() {
    return {
      activationKey: '',
      password: '',
      clickText: ''
    }
  },
  methods: {
    loginCheck(){
        var comp = this;
        var url = 'http://127.0.0.1:5000/login';
        var xhr = new XMLHttpRequest();
        xhr.open("POST", url, true);
        xhr.setRequestHeader("Content-Type", "application/json")
        xhr.onreadystatechange = function() {
            if(xhr.readyState == 4) {
              var sucess = JSON.parse(this.responseText);
              if(sucess == true)
              {
                comp.$store.dispatch("setCurrentActivationKey", comp.activationKey)
                comp.$store.dispatch("setActivated", true)
                comp.clickText = 'You are logged in'
                comp.activationKey = ''
                comp.password = ''
                comp.initializeSchedule()

              }
              else {
                comp.$store.dispatch("setCurrentActivationKey", "")
                comp.$store.dispatch("initializeSchedule", [])
                comp.$store.dispatch("setActivated", false)
                comp.clickText = 'Error: Incorrect activation key or password'
                comp.activationKey = ''
                comp.password = ''
              }
            }
        }
        xhr.onerror = function(err)
        {
            console.warn(err);
        }

          let json = JSON.stringify({
          user: this.activationKey,
          passwd: this.password
        });
        xhr.send(json)
    },
    initializeSchedule(){
      var comp = this
      var url = 'http://127.0.0.1:5000/get_schedule';
      var xhr = new XMLHttpRequest();
      xhr.open("GET", url);
      xhr.setRequestHeader("Content-Type", "application/json")
      xhr.onreadystatechange = function() {
        if(xhr.readyState == 4) {
            comp.$store.dispatch("initializeSchedule", JSON.parse(xhr.response))
        }
      } 

      xhr.onerror = function(err)
      {
          console.warn(err);
      }
      xhr.send();
    }
  }
};
</script>