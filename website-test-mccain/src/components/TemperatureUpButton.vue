<template>
   <b-button class="mb-2">
      <b-icon icon="chevron-up" v-on:click="incrementDesiredTemperature" v-shortkey="['ctrl', 'arrowup']" @shortkey="incrementDesiredTemperature"></b-icon>
    </b-button>
</template>

<script>

export default {
    name: "temperature-up-button",
  components: {
  },
  methods: {
      incrementDesiredTemperature() {
        if(this.$store.state.activated == true)
        {
          this.$store.commit("incrementDesiredTemperature");
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