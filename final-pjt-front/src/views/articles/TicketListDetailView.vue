<template>
  <div>
    <div class="wrapper">
      <div class="main_card">
        <div class="card_left">
          <div class="card_datails">
            <h3>{{ title }}</h3>
            <div style="text-align:right">
            <span>작성자 : </span>
            <button class="btns" @click="toProfile(user)"> {{ user.nickname }}</button>
            </div>
            <br>
            <div class="card_cat scrollbar">
              <h4 >리스트 소개</h4>
              <p class="px-3">{{ content }}</p>
              <!-- <p>{{tickets}}</p> -->
              <br>
              <h4>리뷰와 영화 정보 보기</h4>
              <div v-for="ticket in tickets" :key="ticket.id">
                <button class="btn ticketbtn">
                  <button id="reviewname" class="btn" @click="toReviewDetail(ticket)">{{ ticket.title }}</button>
                  <button id="moviename" class="btn" @click="toMovieDetail(ticket)">{{ ticket.movietitle }}</button>
                </button>
                
               </div>
            </div>
            <div v-if="checkLogin && isAuthor">
              <button class="btns" @click="updateTicketList">수정</button>
              <button class="btns" @click="deleteTicketList">삭제</button>
            </div>
            <br>
            <br>
            <h3 style="color:black;">이 리스트의 추천 영화</h3>
          <button class="btns" v-for="movie in recommended_list" :key="movie.id" @click="toRecommendedMovieDetail(movie)">{{movie.title}}</button>
          </div>
        </div>
        <div class="card_right">
          <h3 style="color:black;">Comments</h3>
          <div class="commentbox">
            <div id="commentinput" class="row g-3 mx-0 d-flex justify-content-between">
              <div class="col-8">
                <input
                  type="text"
                  class="form-control"
                  v-model="comment"
                  placeholder="댓글을 입력해주세요."
                  @keyup.enter="addComment"
                />
              </div>
              <div class="col-4">
                <button id="commentbtn" class="btns" @click="addComment">
                  댓글 추가
                </button>
              </div>
            </div>
          </div>
          <div class="commentlistbox scrollbar" v-if="commentList" >
            <hr style="color:black">
            <div v-for="comment in commentList" :key="comment.id">
              <div class="d-flex align-items-center">
                <span class="px-2" style="color:black; background-color: white;">{{ comment.nickname }}</span>
                <span class="px-2" style="text-align: left;">{{ comment.content }}</span>
                <button v-if="isCommentAuthor(comment)" class="btn ms-auto px-2" @click="deleteComment(comment)">삭제</button>
              </div>
              <hr style="color:black">
            </div>
          </div>
          
        </div>
      </div>
    </div> 
  </div>
</template>

<script>
import axios from "axios";
import _ from "lodash";

export default {
  name: "TicketListDetailView",
  data() {
    return {
      title: "",
      content: "",
      user: "",
      tickets: [],
      comment: "",
      commentList: [],
      recommended_list:[],
    };
  },
  computed: {
    checkLogin() {
      return this.$store.getters.checkLogin;
    },
    isAuthor(){
      // console.log(this.user.id,JSON.parse(localStorage.getItem('userdata')).id);
      if(this.user.id===JSON.parse(localStorage.getItem('userdata')).id){
        return true
      } else{
        return false
      }
    },
  },
  methods: {
    isCommentAuthor(comment){
      if(comment.user===JSON.parse(localStorage.getItem('userdata')).id){
        return true
      } else{
        return false
      }
    },
    deleteComment(comment){
      axios({
        method:'delete',
        url:`http://127.0.0.1:8000/ticketLists/${this.$route.params.ticketlist_pk}/comment/${comment.id}`
      })
      .then(()=>{
        // console.log(res);
        this.getComment();
      })
    },
    toProfile(user) {
      // console.log(user);
      this.$router.push({
        name: "ProfileView",
        params: { username: user.username },
      });
    },
    toReviewDetail(ticket) {
      // console.log(ticket);
      this.$router.push({
        name: "ReviewDetailView",
        params: { review_pk: ticket.id },
      });
    },
    toMovieDetail(ticket) {
      // console.log(ticket);
      this.$router.push({
        name: "MovieDetailView",
        params: { movie_pk: ticket.movie },
      });
    },
    toRecommendedMovieDetail(movie) {
      // console.log(ticket);
      this.$router.push({
        name: "MovieDetailView",
        params: { movie_pk: movie.id },
      });
    },
    addComment() {
      if(!this.comment){
        alert('댓글을 입력해주세요.')
        return
      } 
      axios({
        method: "post",
        url: `http://127.0.0.1:8000/ticketLists/${this.$route.params.ticketlist_pk}/comment/`,
        data: {
          content: this.comment,
          username: localStorage.getItem("username"),
        },
      }).then(() => {
        // console.log(res.data);
        this.getComment();
      })
      .catch(()=>{
        this.$router.push({name:'LogIn'})

      }
      )
      this.comment = "";
    },
    getComment() {
      axios({
        method: "get",
        url: `http://127.0.0.1:8000/ticketLists/${this.$route.params.ticketlist_pk}/getcomment/`,
      }).then((res) => {
        // console.log(2,res.data);
        const comments = res.data;
        axios({
          method: "get",
          url: "http://127.0.0.1:8000/accounts/user/all/",
        }).then((res) => {
          const users = res.data;
          // console.log(1,users,comments);
          this.commentList = comments.filter((comment) => {
            if (comment.ticketlist == this.$route.params.ticketlist_pk) {
              for (const user of users) {
                if (user.id === comment.user) {
                  comment["nickname"] = user.nickname;
                }
              }
              return comment;
            }
          });
          // console.log(3,this.commentList);
        });
      });
    },
    deleteTicketList() {
      axios({
        method: "delete",
        url: `http://127.0.0.1:8000/ticketLists/${this.$route.params.ticketlist_pk}`,
      })
      .then(()=>{
        // console.log(res);
      })
      .then(()=>{
        this.$router.push({ name: "ticketListView" })
      }
      )
    },
    updateTicketList() {
      this.$router.push({
        name: "updateTicketList",
        params: { ticketlist_pk: this.$route.params.ticketlist_pk },
      });
    },
  },
  created() {
    axios({
      method: "get",
      url: `http://127.0.0.1:8000/ticketLists/${this.$route.params.ticketlist_pk}`,
    })
    .then((res) => {
      // console.log(res.data);
      this.title = res.data.title;
      this.content = res.data.content;
      const author = res.data.user;
      axios({
        method: "get",
        url: "http://127.0.0.1:8000/accounts/user/all/",
      }).then((res) => {
        const users = res.data;
        // console.log(users)
        for (const user of users) {
          // console.log(user);
          if (user.id === author) {
            this.user = user;
          }
        }
      });
      const tickets = JSON.parse(res.data.tickets);
      axios({
        method: "get",
        url: "http://127.0.0.1:8000/reviews/",
      }).then((res) => {
        // console.log(res.data,tickets);
        const reviewlist = res.data;
        axios.get("http://127.0.0.1:8000/movies/").then((res) => {
          // console.log(res.data);
          const movies = res.data;
          const review_genres = [];
          const reviews = reviewlist.filter((review) => {
            if (tickets.includes(review.id)) {
              for (const movie of movies) {
                if (movie.id === review.movie) {
                  // console.log(movie);
                  for (const id of movie.genre_ids) {
                    if (!review_genres.includes(id)) {
                      review_genres.push(id);
                    }
                  }
                  review.movietitle = movie.title;
                }
              }
              return review;
            }
          });
          this.tickets = reviews;
          const recommended = movies.filter((movie) => {
            // console.log(1,movie.genre_ids,JSON.parse(JSON.parse(localStorage.userdata).genre_preference))
            for (const id of review_genres) {
              if (movie.genre_ids.includes(id)) {
                return movie;
              }
            }
          });
          // console.log(review_genres);
          this.recommended_list = _.sampleSize(recommended, 3);
        });
      });
    })
    .catch(err=>{
        console.log(err);
        this.$router.push({name:'Not_Found_404'})
      })

    this.getComment();
  },
};
</script>

<style scoped>
.commentbox {
  display: flex;
  justify-content: center;
}

.commentlistbox {
  height: 80%;;
  overflow-y:scroll; 
  overflow-x:hidden;
  scroll-behavior: smooth;
  padding-right: 1rem;
}

#commentbtn {
  color: white;
  background-color: #a0e7ca;
  margin: 0;
}
#commentbtn:hover {
  -webkit-transform: scale(1.1);
  -ms-transform: scale(1.1);
  transform: scale(1.1);
  background-color: #99532a;
}
#commentinput {
  margin-top: 0.1rem
}

.main_card {
  color: #fff;
  border-radius: 10px;
  width: 70rem;
  height: 50rem;
  margin: 50px auto;
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  max-width: 50rem;
  -webkit-box-shadow: 0 0 40px rgba(0, 0, 0, 0.3);
  box-shadow: 0 0 40px rgba(0, 0, 0, 0.3);
}

.card_left {
  border-top-left-radius: 10px;
  border-bottom-left-radius: 10px;
  width: 27rem;
  background-color: #fff;
}

.card_datails {
  background-color: #fff;
  width: 90%;
  padding-top: 30px;
 
  border-top-left-radius: 10px;
  border-bottom-left-radius: 10px;
  margin:0
}
.card_datails h3 {
  font-size: 30px;
  color: black;
  background-color: #fff;
  border-top-left-radius: 10px;
  border-bottom-left-radius: 10px;
}
.card_datails span {
  font-size: 20px;
  color: black;
  background-color: #fff;
  border-top-left-radius: 10px;
  border-bottom-left-radius: 10px;
}
.card_right img {
  height: 350px;
  border-radius: 10px;
  background-color: white;
  box-shadow: 0 0 50px rgba(0, 0, 0, 0.2);
}
.card_right {
  background-color: #fff;
  width:25rem;
  padding-right: 30px;
  padding-top: 30px;
  border-top-right-radius: 10px;
  border-bottom-right-radius: 10px;
}

.scrollbar::-webkit-scrollbar-track
{
	-webkit-box-shadow: inset 0 0 6px rgba(0,0,0,0.3);
	border-radius: 10px;
	background-color: #F5F5F5;
}

.scrollbar::-webkit-scrollbar
{
	width: 12px;
	background-color: #F5F5F5;
}

.scrollbar::-webkit-scrollbar-thumb
{
	border-radius: 10px;
	-webkit-box-shadow: inset 0 0 6px rgba(0,0,0,.3);
	background-color: #99532a;
}

.card_cat {
  background-color: #fff;

  height: 24rem;
  overflow-y:scroll; 
  overflow-x:hidden;
  scroll-behavior: smooth
}
.card_cat > p {
  background-color: #fff;
  color: black;
}

.card_cat > h4 {
  background-color: #fff;
  color: black;
}
span {
  background-color: #fff;
  color: black;
}

a {
  color: darkcyan;
  display: block;
  text-decoration: none;
}
.social-btn {
  background-color: #fff;
}
.btns {
  color: white;
  border: none;
  padding: 10px;
  outline: none;
  font-size: 15px;
  margin-top: 10px;
  margin-left: 10px;
  background: #a0e7ca;
  border-radius: 12px;
  -webkit-box-shadow: 0 0 20px rgba(0, 0, 0, 0.2);
  box-shadow: 0 0 20px rgba(0, 0, 0, 0.2);
  -webkit-transition: 300ms ease-in-out;
  -o-transition: 200ms ease-in-out;
  transition: 200ms ease-in-out;
}

button:hover {
  -webkit-transform: scale(1.1);
  -ms-transform: scale(1.1);
  transform: scale(1.1);
}
.btns:hover {
  -webkit-transform: scale(1.1);
  -ms-transform: scale(1.1);
  transform: scale(1.1);
  background-color: #99532a;
}

.ticketbtn {
  padding: 5px;
  width: 10rem;
  border: #99532a solid 1px;
  margin-top: 1rem;
}
.ticketbtn:hover {
  transform:none;
  background-color: white;
}

#reviewname:hover {
  transform:none;
  background-color: white;
}
#reviewname {
  width:7rem;
  overflow: hidden;
  text-overflow: ellipsis;
}
#moviename:hover {
  transform:none;
}
</style>