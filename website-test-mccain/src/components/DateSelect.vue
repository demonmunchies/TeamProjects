<template>
  <div>
    <label for="date-form">Select Date:</label>
    <b-form-input v-model="date" type="date" v-on:input="updateDate" :state="dateState" aria-describedby="invalid-feedback"></b-form-input>
    <b-form-invalid-feedback :style="{'background-color': $store.state.backgroundColor, 'color': $store.state.textColor}">
          <font size="2">Please select a date up to today</font>
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
          this.$store.dispatch("setDate", this.date)
        }
      }
    },
    computed: {
      dateState() {
        return this.checkDateState()
      }
    }
  }
</script>