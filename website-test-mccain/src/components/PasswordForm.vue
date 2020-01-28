<template>
    <div>
  <b-form>
    <label for="text-password">Password</label>
    <b-input type="password" id="text-password" aria-describedby="password-reset-block"></b-input>
    <router-link to="/myprivatelife/password-reset">
      <b-form-text id="password-reset-block">
        Reset your password
      </b-form-text>
    </router-link>
   </b-form>
</div>
</template>