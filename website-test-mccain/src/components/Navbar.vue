<template>
    <div>
  <b-navbar toggleable="lg" type="dark" variant="primary">
    <b-navbar-brand href="#">My Private Life</b-navbar-brand>
    <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
    <b-collapse id="nav-collapse" is-nav>
      <b-navbar-nav>
        <b-nav-item to="/myprivatelife/">Home</b-nav-item>
        <b-nav-item to="/myprivatelife/thermostat-controls">Thermostat Controls</b-nav-item>
        <b-nav-item to="/myprivatelife/usage-statistics">Usage Statistics</b-nav-item>
        <b-nav-item to="/myprivatelife/user-manual">User Manual</b-nav-item>
      </b-navbar-nav>
    </b-collapse>
  </b-navbar>
</div>
</template>
