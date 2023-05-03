<template>
  <div>
    <hr>
    <h2>산출세액 : {{ calculatedTaxAmount }} 만원</h2>
    <h2>세액감면 : {{ exemption }} 만원</h2>

    <FinalTax 
    :exemption="exemption" 
    :calculated-tax-amount="calculatedTaxAmount"
    />
    
  </div>
</template>

<script>
import FinalTax from '@/components/FinalTax.vue'

export default {
  name: "Taxrate",
  components: {
    FinalTax,
  },
  props: {
    taxBase: Number,
    exemption: Number,
  },
  data: function () {
    return {
      calculatedTaxAmount: null,
    }
  },
  methods: {
    calculateTax: function () {
      if (this.taxBase <= 1200) {
        return Math.round(this.taxBase * 0.06)
      } else if (this.taxBase > 1200 && this.taxBase <= 4600) {
        return Math.round(this.taxBase * 0.15 - 108)
      } else if (this.taxBase > 4600 && this.taxBase <= 8800) {
        return Math.round(this.taxBase * 0.24 - 522)
      } else if (this.taxBase > 8800 && this.taxBase <= 15000) {
        return Math.round(this.taxBase * 0.35 - 1490)
      } else if (this.taxBase > 15000 && this.taxBase <= 30000) {
        return Math.round(this.taxBase * 0.38 - 1940)
      } else if (this.taxBase > 30000 && this.taxBase <= 50000) {
        return Math.round(this.taxBase * 0.4 - 2540)
      } else if (this.taxBase > 50000 && this.taxBase <= 100000) {
        return Math.round(this.taxBase * 0.42 - 3540)
      } else {
        return Math.round(this.taxBase * 0.45 - 6540)
      }
    },
  },
  watch: {
    taxBase: function () {
      this.calculatedTaxAmount = this.calculateTax()
    },
  }
}
</script>

<style>

</style>