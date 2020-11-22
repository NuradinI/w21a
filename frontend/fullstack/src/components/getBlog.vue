<template>
  <div>
    <button @click="getBlogs()">Get Blogs!</button>
    <!-- the database contents is an array, the "key" is the id in your database which has the index of 2, the description you set has the index of 0, and created at the index of 1-->
    <div v-for="blog in blogs" :key="blog[2]">
      <p> {{ blog[0] }}</p>
      <!-- so we access the description by refrecning to the loops "blog" then access the description by going to look at our database and finding what the index of description is -->
      <h6> {{blog[1]}} </h6>
      <!-- when updating we look for the id, the id is what we set above so we also set it to that -->
      <update-blog :blogid="blog[2]"/>
      <delete-blog :blogid="blog[2]"/>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import UpdateBlog from './updateBlog.vue'
import DeleteBlog from './deleteBlog.vue'
export default {
  data() {
    return {
      blogs: []
    };
  },
  components: {
      UpdateBlog,
      DeleteBlog
  },
  methods: {
    getBlogs: function() {
      axios
        .request({
          url: "http://nuradinsblog.ml/api/blogpostings",
          method: 'GET'
        })
        .then(response => {
            console.log(response)
            this.blogs = response.data
        })
        .catch(error => {
            console.log(error)
        });
    }
  }
};
</script>

<style scoped>
</style>