<template>
    <div>
  <b-navbar type="dark" variant="primary" 
  v-shortkey="{left: ['ctrl', 'l'], right: ['ctrl', 'r'], accessibility: ['ctrl', 'a'], home: ['ctrl', 'm']}" @shortkey="rotatePage">
    <b-navbar-brand href="#">My Private Life</b-navbar-brand>
      <b-navbar-nav align="center">
        <b-nav-item to="/myprivatelife/" exact exact-active-class="active">Home</b-nav-item>
        <b-nav-item to="/myprivatelife/thermostat-controls" exact exact-active-class="active">Thermostat Controls</b-nav-item>
        <b-nav-item to="/myprivatelife/usage-statistics" exact exact-active-class="active">Usage Statistics</b-nav-item>
        <b-nav-item to="/myprivatelife/user-manual" exact exact-active-class="active">User Manual</b-nav-item>
      </b-navbar-nav>
  </b-navbar>
</div>
</template>

<script>
export default {
   methods: {
    rotatePage(event) {
      switch (event.srcKey) {
        case 'accessibility':
          this.$router.replace("/myprivatelife/accessibility")
          break
        case 'home':
          if(this.$router.currentRoute.path != "/myprivatelife/") {
            this.$router.replace("/myprivatelife/")
          }
          break
        default:
          var pageList= ["/myprivatelife/", "/myprivatelife/thermostat-controls", "/myprivatelife/usage-statistics", "/myprivatelife/user-manual"]
          var currentPage = this.$router.currentRoute.path
          for(var i = 0; i < pageList.length; i = i + 1){
            if(pageList[i] == currentPage){
              switch (event.srcKey) {
                case 'right':
                  if(i == pageList.length - 1) {
                    this.$router.replace(pageList[0])
                  }
                  else {
                    this.$router.replace(pageList[i + 1])
                  }
                  break
                case 'left':
                  if(i == 0) {
                    this.$router.replace(pageList[pageList.length - 1])
                  }
                  else {
                    this.$router.replace(pageList[i - 1])
                  }
                  break
              }
            }
          }
          break  
      }
    }
   }
};
</script>