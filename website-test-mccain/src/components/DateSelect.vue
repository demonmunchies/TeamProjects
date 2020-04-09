<template>
  <div>
    <label for="date-form">Select Date:</label>
    <b-form-input v-model="date" type="date" v-on:input="updateDate" :state="dateState" aria-describedby="invalid-feedback"></b-form-input>
    <b-form-invalid-feedback :style="{'background-color': $store.state.backgroundColor, 'color': $store.state.textColor}">
          <font size="2">Please select a date up to today and make sure you are logged in </font>
        </b-form-invalid-feedback>
  </div>
</template>

<script>
  export default {
    data() {
      return {
        date: ''
      }
    },
    methods: {
      checkDateState() {
        var valid = false
        var enteredDate = this.date.split('-')
        var enteredYear = parseInt(enteredDate[0], 10)
        var enteredMonth = parseInt(enteredDate[1], 10)
        var enteredDay = parseInt(enteredDate[2], 10)

        var currentDate = new Date()
        var currentYear = currentDate.getFullYear()
        var currentMonth = currentDate.getMonth() + 1
        var currentDay = currentDate.getDate()
        if(enteredYear <  currentYear)
        {
          valid = true
        }
        else if(enteredYear == currentYear && enteredMonth < currentMonth)
        {
          valid = true
        }
        else if(enteredYear == currentYear && enteredMonth == currentMonth && enteredDay <= currentDay)
        {
          valid = true
        }
        return valid
      },
      updateDate() {
        if(this.checkDateState())
        {
          if(this.$store.state.activated == true)
          {
            var enteredDate = this.date.split('-')
            this.$store.dispatch("setDay", parseInt(enteredDate[2], 10))
            this.$store.dispatch("setMonth", parseInt(enteredDate[1], 10))
            this.$store.dispatch("setYear", parseInt(enteredDate[0], 10))
            this.updateGraph()
          }
        }
      },
      updateGraph() {
        var url = 'http://127.0.0.1:5000/get_singular_graph';
        var xhr = new XMLHttpRequest();
        xhr.open("POST", url, true);
        xhr.setRequestHeader("Content-Type", "application/json")
        xhr.onreadystatechange = function() {
            if(xhr.readyState == 4) {
              console.log("");
            }
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
    },
    computed: {
      dateState() {
        return this.$store.state.activated && this.checkDateState()
      }
    }
  }
</script>