import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export const store = new Vuex.Store({
    state: {
      currentTemperature: 72,
      desiredTemperature: 72,
      schedule: [],
      scheduleTime: "",
      scheduleTemp: 72,
      backgroundColor: '#ffffff',
      textColor: '#2c3e50',
      range: "",
      date: ""
    },
    mutations: {
      incrementDesiredTemperature(state) {
        if(state.desiredTemperature < 85)
        {
          state.desiredTemperature++
        }
      },
      decrementDesiredTemperature(state) {
        if(state.desiredTemperature > 60)
        {
          state.desiredTemperature--
        }
      },
      setScheduleTime(state, newValue) {
        state.scheduleTime = newValue
      },
      setScheduleTemp(state, newValue) {
        state.scheduleTemp = newValue
      },
      addToSchedule(state) {
        var found = false
        for(var index = 0; index < state.schedule.length; index++) 
        { 
          if(state.schedule[index].time == state.scheduleTime)
          {
            state.schedule[index].temp = state.scheduleTemp
            found = true
          }
        } 
        if(found == false)
        {
          state.schedule.push({time: state.scheduleTime, temp: state.scheduleTemp})
        }
        console.log(state.schedule)
      },
      setBackgroundColor(state, newValue) {
        state.backgroundColor = newValue
      },
      setTextColor(state, newValue) {
        state.textColor = newValue
      },
      setRange(state, newValue) {
        state.range = newValue
      },
      setDate(state, newValue) {
        state.date = newValue
      }
    },
    actions: {
      setScheduleTime: ({commit, state}, newValue) => {
        commit("setScheduleTime", newValue)
        return state.scheduleTime
      },
      setScheduleTemp: ({commit, state}, newValue) => {
        commit("setScheduleTemp", newValue)
        return state.scheduleTime
      },
      addToSchedule({commit}) {
        commit("addToSchedule")
      },
      setBackgroundColor: ({commit, state}, newValue) => {
        commit("setBackgroundColor", newValue)
        return state.backgroundColor
      },
      setTextColor: ({commit, state}, newValue) => {
        commit("setTextColor", newValue)
        return state.textColor
      },
      setRange: ({commit, state}, newValue) => {
        commit("setRange", newValue)
        return state.range
      },
      setDate: ({commit, state}, newValue) => {
        commit("setDate", newValue)
        return state.date
      }
    }
  })