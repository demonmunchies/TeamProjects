<template>
  <b-row>
    <b-col></b-col>
    <b-col>
      <b-row>
        <label for="input-pass">Password:</label>
        <b-form-input id="input-pass" type="password" v-model="password" :state="passState"
          aria-describedby="password-help"
          placeholder="Enter a new password"
          trim>
          </b-form-input>
        <b-form-invalid-feedback>
        </b-form-invalid-feedback>
        <b-form-text id="password-help">Must contain at least one upercase letter, lowercase letter, number, and special character. No spaces.</b-form-text>
      </b-row>
      <b-row>
        <label for="confirm-pass">Retype Password:</label>
        <b-form-input id="confirm-pass" type="password" v-model="confirmPassword" :state="confirmState"
          aria-describedby="inalid-feedback"
          placeholder="Retype password">
          </b-form-input>
        <b-form-invalid-feedback>
          Passwords don't match
        </b-form-invalid-feedback>
      </b-row>
      <b-row><b-button :disabled='isDisabled'>Submit</b-button></b-row>
    </b-col>
    <b-col></b-col>
  </b-row>
</template>

<script>
export default {
  name: "set-password",
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

      passConfirm()
      {
        return this.password == this.confirmPassword && this.passCorrect();
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
        return !this.passConfirm()
      }
  },
  data() {
    return {
      password: '',
      confirmPassword: ''
    }
  }
};
</script>
