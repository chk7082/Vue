<template>
  <div>
    <h1>로또</h1>
    <button @click="getLuckyNumbers">Get Lucky Numbers</button>
    <p v-text="lottoNums"></p>
  </div>
</template>

<script>
import _ from "lodash"

export default {
  name: "LottoView",
  data() {
    return {
      lottoNums: null,
      possibleCandidates: _.range(1, 47)
    }
  },
  methods: {
    getLuckyNumbers() {
      this.lottoNums = _.sampleSize(this.possibleCandidates, 6)
    },
  },
}
</script>

<style>

</style>