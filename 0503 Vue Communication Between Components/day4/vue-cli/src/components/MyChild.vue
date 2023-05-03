<template>
  <div>
    <h3>This is child component</h3>
    <p>{{ staticProps }}</p>
    <p>{{ MyProps }}</p>
    <button @click="childToParent">클릭!</button>
    <input type="text" v-model="childInputData" @keyup.enter="childInput">
  </div>
</template>

<script>
export default {
  name: 'MyChild',
  data: function () {
    return {
      childInputData: null,
    }
  },
  props: {
    staticProps: String,
    MyProps: String,
  },
  methods: {
    childToParent : function () {
      this.$emit('child-to-parent', 'child Data')
    },
    childInput: function () {
      this.$emit('child-input', this.childInputData)
      this.childInputData = "" // 엔터치고나면 다시 빈 문자열로
    },
  },
}
</script>

<style>
  
</style>
