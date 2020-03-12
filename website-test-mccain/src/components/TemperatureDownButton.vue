<template>
   <b-button class="mb-2">
      <b-icon icon="chevron-down" v-on:click="decrementDesiredTemperature" v-shortkey="['ctrl', 'arrowdown']" @shortkey="decrementDesiredTemperature"></b-icon>
    </b-button>
</template>

<script>

export default {
    name: "temperature-down-button",
  components: {
  },
  methods: {
      decrementDesiredTemperature() {
        this.$store.commit("decrementDesiredTemperature");
      }
    }
}
</script>