<template>
      <div>
          <i @click="isShow =! isShow" class="far fa-trash-alt"></i>
          <div v-if="isShow">
              <button @click="deleteBlog()"> Delete Blog!</button>
          </div>
      </div>

</template>

<script>
import axios from 'axios'
    export default {
        props: {
            blogid: {
                type: Number,
                required: true
            }
        },
        data() {
            return {
                isShow: false
            }
        },
        methods: {
            deleteBlog: function(){
                axios.request({
                    url: 'http://nuradinsblog.ml/api/blogpostings'
                }).then((response) =>{
                    console.log(response)
                }).catch((error) => {
                    console.log(error)
                })
            }
        }
    }
</script>

<style scoped>

</style>