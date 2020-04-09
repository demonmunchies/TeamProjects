<template>
    <b-button variant="secondary" class="btn-primary" v-on:click="addToSchedule" v-shortkey="['ctrl', 'alt', 'a']" @shortkey="addToSchedule">Add To Schedule</b-button>
</template>

<script>
export default {
    methods: {
        addToSchedule() {
            if(this.$store.state.activated == true && this.$store.state.scheduleTime.localeCompare("") != 0)
            {
                this.$store.dispatch("addToSchedule");
                this.addScheduleToDatabase()
            }
        },
        addScheduleToDatabase()
        {
            var url = 'http://127.0.0.1:5000/update_schedule';
            var xhr = new XMLHttpRequest();
            xhr.open("POST", url, true);
            xhr.setRequestHeader("Content-Type", "application/json")
            xhr.onerror = function(err)
            {
                console.warn(err);
            }

            let json = JSON.stringify({
            schedule: this.$store.state.schedule
            });
            xhr.send(json)
        }
    }
};
</script>