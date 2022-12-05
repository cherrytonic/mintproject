<template>
  <div v-bind:class="flipped ? 'flip-container flipped': 'flip-container'">
    <label>
    <input type="checkbox"/>
    <div class="card">
      <div class="front">
        <div id="rline">
          <div id="container" class="container">
          <div class="row px-1">
            <div class="col"><h1>{{moviedetail.title}}</h1>            
            </div>

          </div>
          <br>
          <div class="row justify-content-between align-items-center w-100">
          <div class="col-3">
            <span>Release</span>
          </div>
          <div class="col-6">
            <span>{{moviedetail.release_date}}</span>
          </div>
        </div>
        <br>
        <div class="row justify-content-between align-items-center w-100">
          <div class="col-3">
            <span>Rating</span>
          </div>
          <div class="col-6">
            <i class="bi bi-star-fill" style="color: #ffdf2c;"  v-for="a in reviewInfo.rate" :key="a"></i>
          </div>
        </div>
        <br>
        <div class="row justify-content-between align-items-center w-100">
          <div class="col-3">
            <span>Review Title</span>
          </div>
          <div class="col-6">
            <span>{{ reviewInfo.title }}</span>
          </div>
        </div>
        <br>
        <div class="row justify-content-between align-items-center w-100">
          <div class="col-3">
            <span>Review Content</span>
          </div>
          <div class="col-6">
            <span>{{ reviewInfo.content }}</span>
          </div>
        </div>
        <br>
        <div class="row justify-content-between align-items-center w-100">
          <div class="col-3">
            <span>Reviewed By</span>
          </div>
          <div class="col-6 ">
            <span>{{ nickname }}</span>
          </div>
        </div>
        <br>
        <div v-if="checkLogin && isAuthor">
          <button id="editbtn" class="btn btn"  @click="updateReview">수정</button>
          <button id="delbtn" class="btn btn"  @click="deleteReview">삭제</button>
        </div>
        </div>
        </div>
      </div>
      
        <div class="back"><img :src="'https://image.tmdb.org/t/p/original/'+moviedetail.poster_path" class="img" alt=""></div>
      </div>
    </label>
  </div>

</template>


<script>
import axios from "axios";
export default {
  name: "ReviewDetailView",
  data: function () {
    return {
      reviewId: this.$route.params.review_pk,
      reviewInfomation: {'user':9755412121212},
      userPK: this.$route.params.pk,
      nickname:'',
      username: '',
      moviedetail:[],
      user:{'id':0},
      flipped: false
    };
  },

  computed: {
    reviewInfo() {
      // console.log(this.reviewInfomation);
      return this.reviewInfomation;
    },
    nowUser() {
      return JSON.parse(localStorage.getItem("userdata")).pk;
    },
    checkLogin() {
      return this.$store.getters.checkLogin;
    },
    isAuthor(){
      // console.log(this.user.id,this.reviewInfomation.user);
      if(this.user.id===this.reviewInfomation.user){
        return true
      } else{
        return false
      }

    }
  },
  methods: {
    deleteReview() {
      axios({
        method: "delete",
        url: `http://127.0.0.1:8000/reviews/${this.reviewId}/`,
      })
        .then(() => {
          // console.log(res);
          this.$router.push({ name: "ReviewListView" });
        })
        .catch((err) => {
          console.log(err);
        });
    },
    updateReview(review) {
      this.$router.push({
        name: "ReviewUpdateView",
        params: { review: review },
      });
    },
  },
  created() {
    axios({
      method: "get",
      url: "http://127.0.0.1:8000/reviews/",
    }).then((res) => {
      // console.log(res.data);
      const review = res.data.filter((review) => {
        // console.log(review.id, this.$route.params.review_pk);
        return review.id == this.$route.params.review_pk;
      })
      this.reviewInfomation = review[0];
      axios({
        method:'get',
        url:`http://127.0.0.1:8000/movies/detail/${review[0].movie}`
      })
      .then(res=>{
        this.moviedetail=res.data
      })
      axios({
        method: "get",
      url: `http://127.0.0.1:8000/accounts/user/${review[0].user}`,
    })
      .then((res) => {
        // console.log(1,res);
        this.user=JSON.parse(localStorage.getItem('userdata'))
        // console.log(this.user);
        this.nickname = res.data.nickname;
        this.username = res.data.username;
      })
      .catch((err) => {
        console.log(err);
      })
    });
  },
};
</script>

<style type='text/css' scoped>
body {
background: #F17563;
font-family: Open Sans;
font-size: 50px;
color: #222;
}

label {
-webkit-perspective: 1000px;
perspective: 1000px;
-webkit-transform-style: preserve-3d;
transform-style: preserve-3d;
display: block;
width: 22.5rem;
height: 40rem;
position: absolute;
left: 50%;
top: 60%;
-webkit-transform: translate(-50%, -50%);
transform: translate(-50%, -50%);
cursor: pointer;

}

.card {
position: relative;
height: 100%;
width: 100%;
-webkit-transform-style: preserve-3d;
transform-style: preserve-3d;
-webkit-transition: all 600ms;
transition: all 600ms;
z-index: 20;
background-color: rgba(0,0,0,0);
border: 0;

}

.card > div {
position: absolute;
height: 100%;
width: 100%;
background: #FFF;
text-align: center;
-webkit-backface-visibility: hidden;
backface-visibility: hidden;
border-radius: 2px;
background-color:white;
  --m:
    conic-gradient(from -45deg at bottom,#0000,#000 1deg 89deg,#0000 90deg) bottom/40px 51% repeat-x,
    conic-gradient(from 135deg at top   ,#0000,#000 1deg 89deg,#0000 90deg) top   /40px 51% repeat-x;
  -webkit-mask: var(--m);
          mask: var(--m);
}

.card .back {

-webkit-transform: rotateX(180deg);
transform: rotateX(180deg);
background-image: url(../../assets/60835_31273_2948.jpg);
  --m:
    conic-gradient(from -45deg at bottom,#0000,#000 1deg 89deg,#0000 90deg) bottom/40px 51% repeat-x,
    conic-gradient(from 135deg at top   ,#0000,#000 1deg 89deg,#0000 90deg) top   /40px 51% repeat-x;
  -webkit-mask: var(--m);
          mask: var(--m);
}

label:hover .card {
-webkit-transform: rotateX(20deg);
transform: rotateX(20deg);

}

input {
display: none;
}

:checked + .card {
transform: rotateX(180deg);
-webkit-transform: rotateX(180deg);
}

label:hover :checked + .card {
transform: rotateX(160deg);
-webkit-transform: rotateX(160deg);
box-shadow: 0 20px 20px rgba(255,255,255,.2);
}


.img {
  width:100%;
  height: 100%;
  object-fit: cover;
}

#rline {
  width: 90%;
  height: 85%;
  margin: 0 auto;
  margin-top: 45px;
  border: #000 solid 1px;
}

#container > * > * > *{
  display: flex; 
  color: black;
  background-color: white;
}
#container > * > *{
  display: flex; 
  color: black;
  background-color: white;
}
#container > * {
  display: flex; 
  color: black;
  background-color: white;
}
</style>