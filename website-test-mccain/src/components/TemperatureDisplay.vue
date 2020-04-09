<template>
    <b-card no-body class="text-center" title="Current Temperature">
      <div class="bg-primary text-light">
        <div> Temperature: {{$store.state.currentTemperature}} </div>
        <div> Desired Temperature: {{$store.state.desiredTemperature}} </div>
      </div>
    </b-card>
</template>

<script>
export default {
  created() {
    if(this.$store.state.activated)
    {
      var comp = this;
      var url = 'http://127.0.0.1:5000/get_temperature';
      var xhr = new XMLHttpRequest();
      xhr.open("GET", url);
      xhr.setRequestHeader("Content-Type", "application/json")
      xhr.onreadystatechange = function() {
          if(xhr.readyState == 4) {
              comp.$store.dispatch("setCurrentTemperature", parseInt(xhr.response))
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
