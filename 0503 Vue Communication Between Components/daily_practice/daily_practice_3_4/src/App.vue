<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
    <!-- <HelloWorld msg="Welcome to Your Vue.js App"/> -->
    <br><br>
    <div class="outer-box">
      <h1>소득세 계산기</h1>
      <Income />
    </div>
  </div>
</template>

<script>
// import HelloWorld from './components/HelloWorld.vue'
import Income from './components/Income.vue'

export default {
  name: 'App',
  components: {
    // HelloWorld,
    Income,
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
.outer-box {
  width: 400px;
  margin: auto;
}
</style>
