// App.vue

<template>
  <div id="app">
    <p>Counter: {{ counter }}</p>
    <p>Counter x2: {{ counterDouble }}</p>
    <p></p>
    <button @click="increase">increase +</button>
    <button @click="decrease">decrease -</button>
  </div>
</template>

<script>
export default {
  name: 'App', 
  data: function() {
    return {
      // counter: 0,
    }
  },
  methods: {
    increase: function () {
      // this.counter += 1
      this.$store.dispatch('increaseCounter')
    },
    decrease: function () {
      // this.counter -= 1
      this.$store.dispatch('decreaseCounter')
    },
  },
  computed: {
    // counterDouble: function () {
    //   return this.counter * 2
    // },
    counterDouble() {
      return this.$store.getters.counterDouble
    },
    counter() {
      return this.$store.state.counter
    },
  },
}
</script>

<style>
</style>