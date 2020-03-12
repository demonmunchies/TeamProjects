<template>
    <b-card no-body class="text-center" title="Current Temperature">
      <div class="bg-primary text-light">
        <div> Temperature: {{$store.state.currentTemperature}} </div>
        <div> Desired Temperature: {{$store.state.desiredTemperature}} </div>
      </div>
    </b-card>
</template>

<script>
export default {
}
</script>
