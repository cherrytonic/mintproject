<template>
  <div>
  <div class="container">
  
  <div class="item">
    <div class="item-right">
      <span>{{title}}</span>
      
      <span class="up-border"></span>
      <span class="down-border"></span>
    </div> <!-- end item-right -->
    <div class="item-left">
      <p class="event">{{review.title}}</p>
      <span v-if="user">작성자 : {{user}}</span>
      <br>
      <button @click="toDetail" class="btn" style="margin-top: 0.5rem; font-size: 1.5rem; color: white;
  background-color: #a0e7ca;">티켓 보기</button>
    </div> <!-- end item-right -->
  </div> <!-- end item -->
  
  
  </div>

  </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'ReviewListItem',
    props: {
        review: Object,
        movie: Object
    },
    data() {
      return {
        user:'',
        title:'',
      }
    },
    methods: {
      toDetail() {
        // console.log(this.review);
        this.$router.push({name: 'ReviewDetailView', params: {review_pk:this.review.id}})
    }
  },
  computed:{
    checkLogin() {
      return this.$store.getters.checkLogin;
    },
  },
  created(){
    axios({
      method:'get',
      url:`http://127.0.0.1:8000/accounts/user/${this.review.user}`
    })
    .then(res=>{
      // console.log(res);
      this.user=res.data.nickname
    })
    .catch(err=>{
      console.log(err);
    })
    axios({
      method:'get',
      url:`http://127.0.0.1:8000/movies/detail/${this.review.movie}`
    })
    .then(res=>{
      // console.log(res);
      this.title=res.data.title
    })
  }

}
</script>

<style scoped>


/* * {
  box-sizing: border-box;
  margin:0;
  padding:0;
}
body {
  background:#DDD;
  font-family: 'Inknut Antiqua', serif;
  font-family: 'Ravi Prakash', cursive;
  font-family: 'Lora', serif;
  font-family: 'Indie Flower', cursive;
  font-family: 'Cabin', sans-serif;
} */
div.container {
  max-width: 1350px;
  margin: 0 auto;
  overflow: hidden
  
}
.container .item {
  width: 48%;
  float: left;
  padding: 0px;
  background: #fff;
  overflow: hidden;
  margin: 10px;
  box-shadow: 0 15px 30px 0 rgba(0, 0, 0, 0.11),
    0 5px 15px 0 rgba(0, 0, 0, 0.08);
  
}
.container .item-right, .container .item-left {
  float: left;
  padding: 20px 
}
.container .item-right {
  padding: 30px;
  margin-right: 20px;
  width: 25%;
  position: relative;
  background: #fff;
  height: 286px;
  display: flex;
  align-items: center;
  text-align: center;
}
.container .item-right .up-border, .container .item-right .down-border {
    padding: 14px 15px;
    background-color: #ddd;
    border-radius: 50%;
    position: absolute
}
.container .item-right .up-border {
  top: -8px;
  right: -35px;
}
.container .item-right > span {
  color: #555;
  font-size: 30px;
  background-color: white;
  margin-bottom: 9px;
  
}
.container .item-left > span {
  color: #555;
  font-size: 30px;
  background-color: white;
  margin-bottom: 9px;
}
.container .item-right .down-border {
  bottom: -13px;
  right: -35px;
}
.container .item-right .day, .container .item-left .event {
  color: #555;
  font-size: 60px;
  background-color: white;
  margin-bottom: 9px;
}
.container .item-left {
  width: 71%;
  padding: 34px 36px 34px 46px;
  border-left: 3px dotted #999;
  background: #fff;
} 

@media only screen and (max-width: 1150px) {
  .container .item {
    width: 100%;
    margin-right: 40px
  }
  div.container {
    margin: 0 10px auto
  }
}

</style>
