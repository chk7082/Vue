<template>
  <div>
    <hr>
    <p>Todo Form</p>
    <input type="text" v-model.trim="todoTitle" @keyup.enter="createTodo">
  </div>
</template>

<script>

export default {
  name: 'TodoForm',
  data() {
    return {
      todoTitle: null,
    }
  },
  methods: {
    createTodo() {
      if (this.todoTitle) {
        this.$store.dispatch('createTodo', this.todoTitle)
      } else {
        alert('할일을 입력하세요!!!!')
      }
      // console.log(this.todoTitle)
      this.todoTitle = null
    }
  },
}
</script>

<style>

</style>