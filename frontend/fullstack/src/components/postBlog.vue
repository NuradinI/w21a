<template>
  <div>
    <button @click="isShow=!isShow">Post Blog!</button>
    <div v-if="isShow">
      <textarea v-model="blogDescription"></textarea>
      <br>
      <button @click="postBlog()">Post!</button>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      blogDescription: "",
      isShow: false
    };
  },
  methods: {
    postBlog: function() {
      axios
        .request({
          method: "POST",
          url: 'http://nuradinsblog.ml/api/blogpostings',
          headers: {
            "Content-Type": "application/json"
          },
          data: {
            description: this.blogDescription
          }
        })
        .then(response => {
          console.log(response);
        })
        .catch(error => {
          console.log(error);
        });
    }
  }
};
</script>

<style scoped>
</style>