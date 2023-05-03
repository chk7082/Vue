<template>
  <div>
    <hr>
    <h2>결정세액 : {{ result }} 만원</h2>
  </div>
</template>

<script>
export default {
  name: "FinalTax",
  props: {
    exemption: Number,
    calculatedTaxAmount: Number,
  },
  data: function () {
    return {
      result: null,
    }
  },
  methods: {
    calculateResult: function () {
      // console.log(this.calculatedTaxAmount)
      // console.log(this.exemption)
      return this.calculatedTaxAmount - this.exemption
    }
  },
  watch: {
    exemption: function () {
      this.result = this.calculateResult()
    },
    CalculatedTaxAmount: function () {
      this.result = this.calculateResult()
    },
  },
}
</script>

<style>

</style>