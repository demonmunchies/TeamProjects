<template>
  <div class="usage-statistics" :style="{'background-color': $store.state.backgroundColor, 'color': $store.state.textColor}">
    <b-row>
      <b-col class="col-md-1"></b-col>
      <b-col class="col-md-2">
        <b-row class="mb-3"><RangeForm /></b-row>
        <b-row class="mb-3"><DateSelect /></b-row>
        <b-row class="mb-3"></b-row>
      </b-col>
      <b-col class="col-md" cols="8"><Graph :key="componentKey"/> </b-col>
      <b-col class="col-md" cols="1"></b-col>
    </b-row>  
  </div>
</template>

<script>
import RangeForm from "../components/RangeForm"
import DateSelect from "../components/DateSelect"
import Graph from "../components/Graph"
export default {
  name: "usage-statistics",
  components: {
    RangeForm,
    DateSelect,
    Graph
  },
  data() {
    return {
      componentKey: this.$store.state.graphComponentKey
    }
  }
};
</script>
