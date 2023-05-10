<template>
  <div id="app">
    <!-- <img alt="Vue logo" src="./assets/logo.png"> -->
    <!-- <HelloWorld msg="Welcome to Your Vue.js App"/> -->
    <h1>Cat Image</h1>
    <img v-if="imgSrc" :src="imgSrc" alt="">
    <br>
    <br>
    <button @click="getCatImage">Get Cat</button>
  </div>
</template>

<script>
// import HelloWorld from './components/HelloWorld.vue'
import axios from 'axios'

export default {
  name: 'App',
  components: {
    // HelloWorld
  },
  data() {
    return {
      imgSrc: null,
    }
  },
  methods: {
    getCatImage() {
      const catImageSearchURL = 'https://api.thecatapi.com/v1/images/search'

      axios({
        method: 'get',
        url: catImageSearchURL,
      })
      .then((response) => {
        // console.log(response)
        // console.log(response.data)
        // console.log(typeof response.data)
        // console.log(response.data[0].url)
        this.imgSrc = response.data[0].url
      })
    },
  },
  created() {
    this.getCatImage()
  },
  updated() {
    console.log(this.imgSrc)
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
img {
  height: 500px;
}
</style>
