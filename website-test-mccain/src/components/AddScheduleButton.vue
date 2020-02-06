<template>
    <b-button variant="secondary" class="btn-primary" v-on:click="addToSchedule">Add To Schedule</b-button>
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