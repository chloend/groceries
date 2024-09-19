<template>
  <div id="app">
    <RecipeList />
  </div>
</template>

<script>
import RecipeList from './views/RecipeList.vue'

export default {
  name: 'App',
  components: {
    RecipeList
  }
}
</script>

<style>
html {
  background-color : black;
}
</style>
