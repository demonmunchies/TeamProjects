<template>
  <b-row>
    <b-col class="col-md"></b-col>
    <b-col class="col-md">
      <b-row>
        <label for="input-current-pass">Current Password:</label>
        <b-form-input id="input-current-pass" type="password" v-model="currentPassword">
          </b-form-input>
      </b-row>
      <b-row>
        <label for="input-pass">Password:</label>
        <b-form-input id="input-pass" type="password" v-model="password" :state="passState"
          aria-describedby="password-help"
          placeholder="Enter a new password"
          trim>
          </b-form-input>
        <b-form-invalid-feedback>
        </b-form-invalid-feedback>
        <div id="password-help" :style="{'background-color': $store.state.backgroundColor, 'color': $store.state.textColor}">
          <font size="2">Must contain at least one upercase letter, lowercase letter, number, and special character. No spaces. Minimum of 8 characters.</font>
          </div>
      </b-row>
      <b-row>
        <label for="confirm-pass">Retype Password:</label>
        <b-form-input id="confirm-pass" type="password" v-model="confirmPassword" :state="confirmState"
          aria-describedby="invalid-feedback"
          placeholder="Retype password">
          </b-form-input>
        <b-form-invalid-feedback :style="{'background-color': $store.state.backgroundColor, 'color': $store.state.textColor}">
          <font size="2">Passwords don't match</font>
        </b-form-invalid-feedback>
      </b-row>
      <b-row>
        {{this.feedbackText}}
      </b-row>
      <b-row><b-button v-bind:disabled="isDisabled" v-on:click="setPassword" v-shortkey="['ctrl', 'enter']" @shortkey="setPassword">Submit</b-button></b-row>
    </b-col>
    <b-col class="col-md"></b-col>
  </b-row>
</template>

<script>
export default {
  name: "set-password",
  created() {
    if(!this.$store.state.activated)
    {
      this.feedbackText = 'Error: You are not logged in'
    }

  },
  methods: {
    passCorrect() {
        var num = false;
        var specChar = false;
        var lLetter = false;
        var uLetter = false;
        for (var i = 0; i < this.password.length; i++) 
        {
          if (this.password.charAt(i) >= '0' && this.password.charAt(i) <= '9')
          {
            num = true;
          }
          else if (this.password.charAt(i) == '!' || this.password.charAt(i) == '@' || this.password.charAt(i) == '#' || this.password.charAt(i) == '$' || this.password.charAt(i) == '%' || this.password.charAt(i) == '^' || this.password.charAt(i) == '&' || this.password.charAt(i) == '*')
          {
            specChar = true;
          }     
          else if (this.password.charAt(i) >= 'a' && this.password.charAt(i) <= 'z')
          {
            lLetter = true;
          }
          else if (this.password.charAt(i) >= 'A' && this.password.charAt(i) <= 'Z')
          {
            uLetter = true;
          }
        }
        return this.password.length >= 8 && num && specChar && uLetter && lLetter && this.password.indexOf(' ') == -1;;
      },

      passConfirm() {
        return this.password.localeCompare(this.confirmPassword) == 0 && this.passCorrect();
      },
      setPassword() {
        if(!this.isDisabled && this.$store.state.activationKey != "") {
          var comp = this
          var url = 'http://127.0.0.1:5000/update_passwd';
          var xhr = new XMLHttpRequest();
          xhr.open("POST", url, true);
          xhr.setRequestHeader("Content-Type", "application/json")
          xhr.onreadystatechange = function() {
              if(xhr.readyState == 4) {
                var sucess = JSON.parse(this.responseText);
                if (!sucess && comp.$store.state.activated)
                {
                  comp.feedbackText = 'Error: Check your current password'
                }
                else
                {
                  comp.feedbackText = 'Your password has changed'
                  comp.$store.state.activated = false
                }
                comp.currentPassword = ''
                comp.password = ''
                comp.confirmPassword = ''
              }
          }
          xhr.onerror = function(err)
          {
              console.warn(err);
          }
          let json = JSON.stringify({
            user: this.$store.state.activationKey,
            new_passwd: this.confirmPassword,
            passwd: this.currentPassword
          });
          xhr.send(json)
        }
      }
  },
  computed: {
      passState() {
        return this.passCorrect();
      },

      confirmState() {
        return this.passConfirm();
      },
      isDisabled() {
        return !this.passConfirm() || !this.$store.state.activated
      }
  },
  data() {
    return {
      password: '',
      confirmPassword: '',
      currentPassword: '',
      feedbackText: ''
    }
  }
};
</script>
