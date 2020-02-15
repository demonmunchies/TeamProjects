<template>
  <div class="usage-statistics">
    <b-row>
      <b-col cols="1"></b-col>
      <b-col cols="2">
        <b-row class="mb-3"><RangeForm /></b-row>
        <b-row class="mb-3"><DateSelect /></b-row>
      </b-col>
      <b-col cols="8">The graph will be displayed here</b-col>
      <b-col cols="1"></b-col>
    </b-row>  
  </div>
</template>

<script>
import RangeForm from "../components/RangeForm"
import DateSelect from "../components/DateSelect"
export default {
  name: "usage-statistics",
  components: {
    RangeForm,
    DateSelect
  }
};
</script>
