<template>
  <div class="usage-statistics">
    <b-row>
    <b-col cols="3">
      <div> Display Interval: <RangeForm /></div>
      <div> <ExcelButton /> </div>
    </b-col>
    <b-col cols="8">The graph will be displayed here</b-col>
    <b-col cols="1"></b-col>
    </b-row>  
  </div>
</template>

<script>
import RangeForm from "../components/RangeForm"
import ExcelButton from "../components/ExcelButton"
export default {
  name: "usage-statistics",
  components: {
    RangeForm,
    ExcelButton
  }
};
</script>
