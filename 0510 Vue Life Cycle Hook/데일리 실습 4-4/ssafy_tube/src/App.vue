<template>
  <div id="app">
    <!-- <img alt="Vue logo" src="./assets/logo.png"> -->
    <!-- <HelloWorld msg="Welcome to Your Vue.js App"/> -->
    <h1 style="font-weight: bold; color: blue;">SSAFY TUBE</h1>
    <iframe v-if="videoSrc" :src="videoSrc" frameborder="0"></iframe>
    <br>
    <span v-text="videoTitle"></span>
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
      videoSrc: null,
      // videoSrc: 'https://www.youtube.com/embed/cbuZfY2S2UQ',
      videoTitle: null,
    }
  },
  methods: {
    youtubeVideo() {
      // console.log(process.env.VUE_APP_YOUTUBE_API_KEY)

      axios({
        method: 'get',
        url: encodeURI(`https://www.googleapis.com/youtube/v3/search?key=${process.env.VUE_APP_YOUTUBE_API_KEY}&part=snippet&maxResults=1&type=video&q=코딩노래`),
      })
      .then((response) => {
        console.log(response)
        console.log(response.data.items[0].id.videoId)
        this.videoSrc = `https://www.youtube.com/embed/${response.data.items[0].id.videoId}`

        console.log(response.data.items[0].snippet.title)
        this.videoTitle = response.data.items[0].snippet.title
      })
      .catch((error) => {
        console.log(error)
      })
    },
  },
  created() {
    this.youtubeVideo()
  },
}
</script>

<style>
#app {
  font-family: Noto Sans KR, Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

iframe {
  width: 700px;
  height: 400px;
}
</style>
