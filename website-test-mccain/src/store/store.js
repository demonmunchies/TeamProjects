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
      addToSchedule(state) {
        state.schedule.push({time: state.scheduleTime, temp: state.scheduleTemp})
      }
    },
    actions: {
      setScheduleTime: ({commit, state}, newValue) => {
        commit("setScheduleTime", newValue)
        return state.scheduleTime
      },
      addToSchedule({commit}) {
        commit("addToSchedule")
      },
    },
  })