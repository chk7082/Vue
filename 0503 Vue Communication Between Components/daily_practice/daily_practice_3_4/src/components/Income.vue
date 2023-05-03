<template>
  <div> 
    <p>연봉 입력 (만원): <input v-model.number="salary" type="number"></p>
    <p>세액감면액 (만원): <input v-model.number="exemption" type="number"></p>

    <hr>

    <h2>종합소득금액 : {{ salary }} 만원</h2>
    <h2>종합소득공제 : (-) 150 만원</h2>
    <h2>과세표준 : {{ taxBase }} 만원</h2>

    <Taxrate :tax-base="taxBase" :exemption="exemption"/>
  </div>
</template>

<script>
import Taxrate from '@/components/Taxrate.vue'

export default {
  name: 'Income',
  components: {
    Taxrate,
  },
  data: function () {
    return {
      salary: null,
      exemption: null,
      taxBase: null,
    }
  },
  watch: {
    salary: function (num) {
      this.taxBase = Math.max(num - 150, 0)
    },
  }
}
</script>

<style>

</style>