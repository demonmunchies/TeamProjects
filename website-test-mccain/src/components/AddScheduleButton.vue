<template>
    <b-button variant="secondary" class="btn-primary" v-on:click="addToSchedule" v-shortkey="['ctrl', 'alt', 'a']" @shortkey="addToSchedule">Add To Schedule</b-button>
</template>

<script>
export default {
    methods: {
        addToSchedule() {
            this.$store.dispatch("addToSchedule");
        }
    }
}
</script>