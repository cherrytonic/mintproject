<template>
    <div>
      <h1>리뷰 수정</h1>
      
      <br>
     <div class="outer">
      <form @submit.prevent="updateReview" class="inner">
        <div class="row g-3 align-items-center">
          <label for="title">title </label>
        <input class="form-control" type="text" v-model.trim="title"><br>
      </div>
      <br>
      <div class="row g-3 align-items-center">
          <label for="content">content</label>
        <textarea class="form-control" value="" v-model.trim="content" rows="10"></textarea>
        </div>
        <br>
        <label for="rating">rating</label>
        <br>
        <br>
        <StarRating 
        v-model="rate" id="rate" :rate="parseFloat(10) / 2" :read-only="false" :increment="1" @rating-selected="setRating"
        :border-width="4" border-color="#d8d8d8" :rounded-corners="true" :star-points="[23,2, 14,17, 0,19, 10,34, 7,50, 23,43, 38,50, 36,34, 46,19, 31,17]"
        ></StarRating>
        <br>
        <button type="submit" class="btn" style="background-color: white; color: #a0e7ca;">Submit</button>
      </form>
      
    </div>
    <br>
    <router-link :to="{ name: 'ReviewListView' }" class="link">뒤로가기</router-link>
    </div>
</template>
  
  
  <script>
  import axios from 'axios'
  import StarRating from 'vue-star-rating'

  export default {
    name: 'ReviewUpdateView',
    components: {
      StarRating
    },
    data() {
      return {
        title: null,
        content: null,
        rate: 0,
        reviewId: this.$route.params.review_pk,
        reviewInfomation:null,
      }
    },
    computed:{
      checkLogin() {
      return this.$store.getters.checkLogin;
    },
    },
    methods: {
      setRating: function(rate) {
        this.rate = rate
        
      },
      updateReview() {
        const title = this.title
        const content = this.content
        const rate = this.rate
        const username = localStorage.username
        const movie_id=this.$route.params.movie_id
        const payload = {
          title, content, rate, username, movie_id
        }
        console.log(payload);
        // this.$store.dispatch('createReview', payload)
        // this.title = ''
        // this.content = ''
        axios({
          method: 'put',
          url:`http://127.0.0.1:8000/reviews/${this.reviewId}/`,
          data: payload
        })
        .then(() => {
          console.log('created');
          this.$router.push({name:'ReviewListView'})
        })
        .catch(err => console.log(err))
        
      },
      
      },
      created(){
      axios({
                method:'get',
                url:'http://127.0.0.1:8000/reviews/'
            })
            .then(res=>{
                // console.log(res.data)
                const review=res.data.filter(review=>{
                // console.log(review.id, this.$route.params.review_pk);
                return review.id==this.$route.params.review_pk
              })
              // console.log(3,review);
              // const i = 
              this.title = review[0].title
              this.content = review[0].content
              this.rate = review[0].rate

            })
    }
    }
  
  </script>
  
  
  <style>

  .link {
    color: white;
    text-decoration: none;
  }

    .outer {
    display: flex
  }

  .inner {
    margin: 0 auto
  }

  span {
    background-color: #a0e7ca;
    color: white;
  }
  
  div > span {
    background-color: #a0e7ca;
    color: white;
  }

  </style>