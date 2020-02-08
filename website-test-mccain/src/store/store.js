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
      textColor: '#2c3e50'
    },
    mutations: {
      incrementDesiredTemperature(state) {
        state.desiredTemperature++
      },
      decrementDesiredTemperature(state) {
        state.desiredTemperature--
      },
      setScheduleTime(state, newValue) {
        state.scheduleTime = newValue
      },
      setScheduleTemp(state, newValue) {
        state.scheduleTemp = newValue
      },
      setBackgroundColor(state, newValue) {
        state.backgroundColor = newValue
      },
      setTextColor(state, newValue) {
        state.textColor = newValue
      },
      addToSchedule(state) {
        state.schedule.push({time: state.scheduleTime, temp: state.scheduleTemp})
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
      }
    }
  })