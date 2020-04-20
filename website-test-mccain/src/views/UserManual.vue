<template>
  <div class="user-manual" :style="{'background-color': $store.state.backgroundColor, 'color': $store.state.textColor}">
    <b-row>
      <b-col class="col-md-2"></b-col>
      <b-col class="col-md-8">
    <h1>User Manual</h1>
    <h3>Section I: installation</h3>
<h3>Section II: Account Setup</h3>
<p align="left">Go to the following website: to set up your account. enter the appropriate information that came with the system in the login pane. 
Note: it is highly suggested that after the first login to use the password reset link at the bottom of the login page to update the account password. 
Keep the page that contains your activation key in a safe location because this can never be changed.<p align="left">
<h3>Section III: Thermostat Controls</h3>
<p align="left">Once you navigate to the My Private Life homepage, click on the thermostat controls button at the top of the screen.
The pane on the left side of the page displays the current temperature of the household and the desired temperature of the household, like a typical thermostat. You can use the cursor to click the up and down buttons in the left pane to change the desired temperature of the household.
The pane on the right side of the page allows you to update a daily schedule that will automatically change the desired temperature of the household at the specified time. The top input box is to select the time to add to the schedule. The time requires an input of hours, minutes, and AM/PM. The slider below the time input allows you to set the desired temperature of your household at the previously specified time. Drag the slider left and right to set the desired temperature. Once both a time and temperature been selected, you can click the add to schedule button to add this to the thermostat’s programmed temperature changes.
Note: The allowable temperature ranges are between 60 and 85°F. Once a time in the temperature been added to the schedule, they cannot be removed. If two items are added to the schedule with the same time selected, the most recent time/desired temperature selection is used.</p>
<h3>Section IIII: Usage Statistics</h3>
<p align="left">Once you navigate to the My Private Life homepage, click on the usage statistics button at the top of the screen.
This page allows you to see a graph of your thermostat usage over a period of time. To use this feature, you must select the starting date for the temperatures that you’d like to see. Then you must select the time. The you’d like to see this temperatures over in the drop-down below the date selection. The time period choices or day, week, month, year. 
If you select day, the average temperature of the thermostat over an hour is displayed for 24 hour time period, on the day the previously selected. 
If you select a week, the date you selected is the starting date for the graph and it ends exactly a week later. In this instance, the temperature will be averaged over 24 hour periods for a whole week. For example, if you selected 03/22/ 19 the graph will display average temperature statistics, in 12 hour periods, between 03/22/19 to 03/29/19.  
If you select month, the whole month will be displayed for the date you selected, and the temperatures will be averaged over a day. For example, if you selected the date 12/17/19 the graph display average temperature statistics, in daily periods between 12/01/2019 through 12/31/2019.
If you select year, the whole year will be displayed for the date you selected, and the temperatures will be averaged over a month. For example, if you selected the date 12/17/19 the graph display average temperature statistics, in monthly periods between 01/01/2019 through 12/31/2019.
Note: You may not select a date that is later than the present day.</p>
<h3>Section IIIII: Accessibility</h3>
<p align="left">Once you navigate to the My Private Life homepage, click on the accessibility button at the top right of the screen. This will open a page that allows you to fully customize background and text colors, as well as display a list of keyboard shortcuts for navigating and interacting with the website.</p>
  </b-col>
  <b-col class="col-md-2"></b-col>
  </b-row>
  </div>
</template>

<script>
// @ is an alias to /src
export default {
  name: "user-manual",
  components: {
  }
};
</script>
