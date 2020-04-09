<template>
  <div>
    <label for="range-form">Display Interval:</label>
    <b-form-select v-model="selected" :options="options" v-on:input="updateRange"></b-form-select>
  </div>
</template>

<script>
  export default {
    data() {
      return {
        selected: null,
        options: [
          { value: null, text: 'Please select a time frame' },
          { value: 1, text: 'Day' },
          { value: 2, text: 'Week' },
          { value: 3, text: 'Month' },
          { value: 4, text: 'Year' }
        ]
      }
     },
     methods: {
      updateRange() {
        if(this.$store.state.activated == true)
        {
          this.$store.dispatch("setRange", this.selected)
          this.updateGraph()
        }
      },
      updateGraph() {
        var url = 'http://127.0.0.1:5000/get_singular_graph';
        var xhr = new XMLHttpRequest();
        xhr.responseType = 'json';
        xhr.open("POST", url, true);
        xhr.setRequestHeader("Content-Type", "application/json")
        xhr.onreadystatechange = function() {
        }
        xhr.onerror = function(err)
        {
            console.warn(err);
        }
        let json = JSON.stringify({
        select : this.$store.state.range, 
        day : this.$store.state.day, 
        month : this.$store.state.month, 
        year : this.$store.state.year
        });
        xhr.send(json)
        if(xhr.status == 200)
        {
          this.forceRerender()
        }
      },
      forceRerender() {
        this.$store.commit("incrementGraphComponentKey");
      }
    }
  }
</script>