<template>
  <div>
    <h1>점심메뉴</h1>
    <button @click="pickLunchMenu">Pick Lunch</button>
    <p v-text="pickedMenu"></p>
    <br>
    <h2>로또를 뽑아보자</h2>
    <button @click="PickLotto">Pick Lotto</button>
  </div>
</template>

<script>
import _ from "lodash"

export default {
  name: 'LunchView',
  data() {
    return {
      menuList: ["치킨", "피자", "햄버거", "규카츠", "파스타", "샐러드",],
      pickedMenu: null,
    }
  },
  methods: {
    pickLunchMenu() {
      this.pickedMenu = _.sample(this.menuList)
    },
    PickLotto() {
      this.$router.push({name: 'lotto'})
    },
  },
}
</script>

<style>

</style>