<template>
   <b-button class="mb-2">
      <b-icon icon="chevron-up" v-on:click="incrementDesiredTemperature"></b-icon>
    </b-button>
</template>

<script>

export default {
    name: "temperature-up-button",
  components: {
  },
  methods: {
      incrementDesiredTemperature() {
        this.$store.commit("incrementDesiredTemperature");
      }
    }
}
</script>