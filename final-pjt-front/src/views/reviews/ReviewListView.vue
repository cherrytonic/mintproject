<template>
    <div class="row d-flex justify-content-center">
      <!-- <div class="row col-10"> -->
      <ReviewListItem
      v-for="review in reviewList"
      :review="review"
      :key="review.id"
      />
      
    <!-- </div> -->
    </div>
  </template>
  
  <script>
  import axios from 'axios'
  import ReviewListItem from '@/components/ReviewListItem'
  
  export default {
      name:'ReviewListView',
      components: {
          ReviewListItem,
      },
  
      data(){
          return{
              title:null,
              content:null
          }
      },
      methods:{
          getReviewList(){
              axios({
                  method:'get',
                  url:'http://127.0.0.1:8000/reviews/'
              })
              .then((res) =>{
                  // console.log(res)
                  this.$store.commit('PUSH_REVIEWS', res.data)
              })
              .catch((err) => {
                  console.log(err)
              })
          },
          toDetail() {
          // console.log(review);
          // this.$router.push({name: 'ReviewDetailView', params: {review_pk:this.review.id}})
          }
      },
      computed: {
          reviewList() {
              return this.$store.state.reviewList
          },
          checkLogin() {
      return this.$store.getters.checkLogin;
    },
      },
      created: function() {
  
      this.getReviewList();
      
      },
  }
  </script>
  
  <style>
  
  </style>