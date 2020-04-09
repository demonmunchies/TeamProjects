<template>
   <b-button class="mb-2">
      <b-icon icon="chevron-down" v-on:click="decrementDesiredTemperature" v-shortkey="['ctrl', 'arrowdown']" @shortkey="decrementDesiredTemperature"></b-icon>
    </b-button>
</template>

<script>

export default {
    name: "temperature-down-button",
  components: {
  },
  methods: {
      decrementDesiredTemperature() {
        if(this.$store.state.activated == true)
        {
          this.$store.commit("decrementDesiredTemperature");
          var url = 'http://127.0.0.1:5000/update_desired_temperature';
          var xhr = new XMLHttpRequest();
          xhr.open("POST", url, true);
          xhr.setRequestHeader("Content-Type", "application/json")
          xhr.onreadystatechange = function() {
              if(xhr.readyState == 4) {
                xhr.response;
              }
          }
          xhr.onerror = function(err)
          {
              console.warn(err);
          }
          let json = JSON.stringify({
  data: this.$store.state.desiredTemperature
  })
          xhr.send(json)
        }
      }
    }
  }
</script>