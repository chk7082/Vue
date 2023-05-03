<template>
  <div>
    <h1>AppParent</h1>
    <input type="text" v-model="parentData" @input="parentToRoot">
    <p>appData : {{ appData }}</p>
    <p>childData : {{ childData }}</p>

    <AppChild 
    :app-data="appData" 
    :parent-data="parentData"
    @child-to-parent="parentGetEvent"
    />
  </div>
</template>

<script>
import AppChild from '@/components/AppChild.vue'

export default {
  name: "AppParent",
  props: {
    appData: String,
  },
  components: {
    AppChild,
  },
  data: function () {
    return {
      parentData: null,
      childData: null,
    }
  },
  methods: {
    parentGetEvent: function (childData) {
      // console.log(childData)
      this.childData = childData
      this.$emit('child-to-root', this.childData)
    },
    parentToRoot: function () {
      this.$emit('parent-to-root', this.parentData)
    }
  },
}
</script>

<style>

</style>