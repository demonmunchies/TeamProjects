import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export const store = new Vuex.Store({
    state: {
      currentTemperature: 72,
      desiredTemperature: 72,
      schedule: [],
      scheduleTime: -1,
      scheduleTemp: 72
    },
    mutations: {
      incrementDesiredTemperature(state) {
        state.desiredTemperature++
      },
      decrementDesiredTemperature(state) {
        state.desiredTemperature--
      },
      addToSchedule(state) {
        console.log(state.schedule)
        state.schedule.push({time: state.scheduleTime, temp: state.scheduleTemp})
      }
    },
    actions: {
      addToSchedule({commit}) {
        commit("addToSchedule")
      }
    }
  })