<template>
  <div id="app">
   <post-blog/>
   <get-blog/>
  </div>
</template>

<script>

import PostBlog from './components/postBlog.vue'
import GetBlog from './components/getBlog.vue'
export default {
  name: 'App',
components: {
  PostBlog,
  GetBlog
}
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
