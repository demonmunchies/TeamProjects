import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export const store = new Vuex.Store({
    state: {
      currentTemperature: 72,
      desiredTemperature: 72,
      schedule: [],
      scheduleTime: "",
      scheduleTemp: 72
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
    },
  })