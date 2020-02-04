import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export const store = new Vuex.Store({
    state: {
      currentTemperature: 72,
      desiredTemperature: 72
    },
    mutations: {
      incrementDesiredTemperature(state) {
        state.desiredTemperature++
      },
      decrementDesiredTemperature(state) {
        state.desiredTemperature--
      }
    }
  })