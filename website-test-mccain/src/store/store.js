import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export const store = new Vuex.Store({
    state: {
      currentTemperature: 60, 
      desiredTemperature: 72,
      schedule: [],
      scheduleTime: "",
      scheduleTemp: 72,
      backgroundColor: '#ffffff',
      textColor: '#2c3e50',
      range: -1,
      day: "",
      month: "",
      year: "",
      activationKey: "",
      password: "",
      graphComponentKey: 0,
      activated: false
    },
    mutations: {
      incrementGraphComponentKey(state) {
        state.graphComponentKey++
      },
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
            state.schedule[index].tempemperature = state.scheduleTemp
            found = true
          }
        } 
        if(found == false)
        {
          state.schedule.push({time: state.scheduleTime, temperature: state.scheduleTemp})
        }
      },
      initializeSchedule(state, newValue) {
        state.schedule = newValue
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
      setDay(state, newValue) {
        state.day = newValue
      },
      setMonth(state, newValue) {
        state.month = newValue
      },
      setYear(state, newValue) {
        state.year = newValue
      },
      setCurrentTemperature(state, newValue) {
        state.currentTemperature = newValue
      },
      setCurrentActivationKey(state, newValue) {
        state.activationKey = newValue
      },
      setActivated(state, newValue) {
        state.activated = newValue
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
      initializeSchedule: ({commit, state}, newValue) => {
        commit("initializeSchedule", newValue)
        return state.schedule
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
      setDay: ({commit, state}, newValue) => {
        commit("setDay", newValue)
        return state.day
      },
      setMonth: ({commit, state}, newValue) => {
        commit("setMonth", newValue)
        return state.month
      },
      setYear: ({commit, state}, newValue) => {
        commit("setYear", newValue)
        return state.year
      },
      setCurrentTemperature: ({commit, state}, newValue) => {
        commit("setCurrentTemperature", newValue)
        return state.currentTemperature
    },
    setCurrentActivationKey: ({commit, state}, newValue) => {
      commit("setCurrentActivationKey", newValue)
      return state.activationKey
  },
  setActivated: ({commit, state}, newValue) => {
    commit("setActivated", newValue)
    return state.activated
}
}
})