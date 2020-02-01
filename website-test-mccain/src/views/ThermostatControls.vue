<template>
  <div class="thermostat-controls">
    <b-row>
    <b-col>
      <b-jumbotron header="Temperature" lead="Current Temperature and Controls">
        <TemperatureDisplay />
        <div>Increase Temperature <TemperatureUpButton /></div>
        <div>Decrease Temperature <TemperatureDownButton /></div>
      </b-jumbotron>
    </b-col>
    <b-col>
      <b-jumbotron header="Schedule" lead="Set Thermostat Schedule">
        Select Time
        <TimeSelect />
        <TemperatureSelect />
        <AddScheduleButton />
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
