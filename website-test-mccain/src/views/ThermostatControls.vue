<template>
  <div class="thermostat-controls" :style="{'background-color': $store.state.backgroundColor, 'color': $store.state.textColor}">
    <b-row>
    <b-col class="col-md">
      <b-jumbotron header="Temperature" lead="Current Temperature and Controls" :style="{ 'background-color': $store.state.backgroundColor, 'color': $store.state.textColor}">
        <TemperatureDisplay :key='this.$store.state.currentTemperature'/>
        <div>Increase Temperature <TemperatureUpButton /></div>
        <div>Decrease Temperature <TemperatureDownButton /></div>
      </b-jumbotron>
    </b-col>
    <b-col class="col-md">
      <b-jumbotron header="Schedule" lead="Set Thermostat Schedule" :style="{ 'background-color': $store.state.backgroundColor, 'color': $store.state.textColor}">
        Select Time
        <TimeSelect />
        <TemperatureSelect />
        <AddScheduleButton />
        <b-table :items='this.$store.state.schedule' :style="{'background-color': $store.state.backgroundColor, 'color': $store.state.textColor}"/>
      </b-jumbotron>
    </b-col>
    </b-row>
  </div>
</template>

<script>
import TemperatureDisplay from "../components/TemperatureDisplay";
import TemperatureUpButton from "../components/TemperatureUpButton";
import TemperatureDownButton from "../components/TemperatureDownButton";
import TimeSelect from "../components/TimeSelect";
import TemperatureSelect from "../components/TemperatureSelect";
import AddScheduleButton from "../components/AddScheduleButton";
export default {
  name: "thermostat-controls",
  components: {
    TemperatureDisplay,
    TemperatureUpButton,
    TemperatureDownButton,
    TimeSelect,
    TemperatureSelect,
    AddScheduleButton
  }
};
</script>
