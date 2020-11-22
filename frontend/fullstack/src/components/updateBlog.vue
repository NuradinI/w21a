<template>
  <div>
    <i @click="isShow=!isShow" class="far fa-edit"></i>
    <div v-if="isShow">
        <textarea v-model="blogDescription"></textarea>
        <br>
        <button @click="editBlog()">Update Blog!</button>
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
  props: {
    blogid: {
      type: Number,
      required: true
    }
  },
  methods: {
    editBlog: function() {
      axios
        .request({
          url: "http://nuradinsblog.ml/api/blogpostings",
          method: 'PATCH',
          headers: {
              'Content-Type': 'application/json'
          },
          data: {
              description : this.blogDescription
          }
        })
        .then((response) => {
            console.log(response)
        })
        .catch((error) => {
            console.log(error)
        });
    }
  }
};
</script>

<style scoped>
</style>