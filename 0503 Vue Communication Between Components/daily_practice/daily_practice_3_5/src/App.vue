<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
    <!-- <HelloWorld msg="Welcome to Your Vue.js App"/> -->
    <h1>App</h1>
    <input type="text" v-model="appData">
    <p>parentData : {{ parentData }}</p>
    <p>childData : {{ childData }}</p>

    <AppParent 
    :app-data="appData"
    @child-to-root="rootGetChildData"
    @parent-to-root="rootGetParentData"
    />
  </div>
</template>

<script>
// import HelloWorld from './components/HelloWorld.vue'
import AppParent from './components/AppParent.vue'

export default {
  name: 'App',
  components: {
    // HelloWorld
    AppParent,
  },
  data: function () {
    return {
      appData: null,
      childData: null,
      parentData: null,
    }
  },
  methods: {
    rootGetChildData: function (childData) {
      this.childData = childData
    },
    rootGetParentData: function (parentData) {
      this.parentData = parentData
    }
  },
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
</style>
