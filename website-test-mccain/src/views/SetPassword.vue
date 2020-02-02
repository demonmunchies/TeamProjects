<template>
  <b-row>
    <b-col></b-col>
    <b-col>
      <div>
        <label for="input-pass">Password:</label>
        <b-form-input id="input-pass" type="password" v-model="password" :state="passState"
          aria-describedby="password-help"
          placeholder="Enter a new password"
          trim>
          </b-form-input>
        <b-form-invalid-feedback>
        </b-form-invalid-feedback>
        <b-form-text id="password-help"></b-form-text>
      </div>
      <div>
        <label for="confirm-pass">Retype Password:</label>
        <b-form-input id="confirm-pass" type="password" v-model="confirmPassword" :state="confirmState"
          aria-describedby="password-help"
          placeholder="Retype password"
          trim>
          </b-form-input>
        <b-form-invalid-feedback>
        </b-form-invalid-feedback>
        <b-form-text id="password-help"></b-form-text>
      </div>
      <div><b-button :disabled='isDisabled'>Submit</b-button></div>
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
        }
        return this.password.length >= 8 && num && specChar
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
