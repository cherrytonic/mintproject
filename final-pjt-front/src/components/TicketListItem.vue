<template>
  <div>
    <div class="box">
    <div class="book">
      <div class="bookback"></div>
      <div class="page2">
        
        <i class="bi bi-heart-fill"  v-if="is_liked" @click="LikeFunc"></i>
        <i class="bi bi-heart"  v-else @click="LikeFunc"></i>
        <br>
        <span>{{like_count}}명이 이 리스트를 좋아합니다.</span>
        <br>
        <br>
        <button @click="toDetail" class="btn">ToDetail</button> 
      </div>
      <div class="page1">
        <div class="pagecontent" v-if="ticketlist_review_computed">
          <div class="ticketimage" v-for="ticket in ticketlist_review_computed" :key="ticket.id">
          <!-- <img src="../assets/오리지널 티켓 바탕핑크.png" alt=""> -->
          <!-- <p>{{ticket}}</p> -->
          <span>{{ticket.review_title}}</span>
          <br>
          <p style="padding-right: 2px; padding-left: 2px; color:black; font-size: 12px;">{{ticket.movie}}</p>
          </div>
        </div>
        
      </div>
      <div class="bookfront">
        <h2 style="background-color: rgb(186, 186, 251, 0); color: white;">{{ticketlist.title}}</h2>
        <br>
        <span class="card-text" v-if="user">작성자 : {{user}}</span>
      </div>
    </div>
  </div>
  </div>


</template>

<script>
import axios from 'axios'

export default {
    name: 'TicketListItem',
    props: {
        ticketlist: Object,
        reviewlist: Array,
        movielist: Array,
    },
    data() {
      return {
        user:'',
        is_liked:false,
        ticketlist_reviews:[],
        like_count:'',
      }
    },
    computed:{
      ticketlist_review_computed(){
        const t_reviews=this.reviewlist.filter(review=>{
          // console.log(JSON.parse(this.ticketlist.tickets),review);
          if(JSON.parse(this.ticketlist.tickets).includes(review.id)){
            return review
          }
        })
        const newdata=t_reviews.map(review=>{
          for(const movie of this.movielist){
            if(movie.id===review.movie){
              return {
                'id':review.id,
                'movie':movie.title,
                'review_title':review.title,
              }
            }
          }
        })
        // console.log(newdata);
        if(newdata.includes(undefined)){
          return ''
        }
        else{
          return newdata
        }
      }
    },
    methods: {
      toDetail(){
        // console.log(this.ticketlist);
        this.$router.push({name: 'TicketListDetailView', params: { ticketlist_pk:this.ticketlist.id, user:this.user }})
      },
      LikeFunc(){
        axios({
          method:'post',
          url:`http://127.0.0.1:8000/ticketLists/${this.ticketlist.id}/likes/`,
          data:{
            user:JSON.parse(localStorage.getItem('userdata')).id
          }
        })
        .then(res=>{
          // console.log(res.data);
          this.is_liked=res.data.is_liked
          this.like_count=res.data.like_count
        })
      }
      
  },
  created(){
    axios({
      method:'get',
      url:`http://127.0.0.1:8000/accounts/user/${this.ticketlist.user}`
    })
    .then(res=>{
      // console.log(res);
      this.user=res.data.nickname
    })
    .catch(err=>{
      console.log(err);
    })
    // console.log(this.ticketlist.id);
    axios({
          method:'get',
          url:`http://127.0.0.1:8000/ticketLists/${this.ticketlist.id}/getlikes/${localStorage.getItem('username')}`,
        })
        .then(res=>{
          // console.log(res.data);
          this.is_liked=res.data.is_liked
          this.like_count=res.data.like_count
        })
        .catch(err=>{
          console.log(err);
          // this.$router.go()
          // this.$emit('update')
        }
        )
  }
}
</script>

<style scoped>

.card-text {
  background-color: rgba(0, 0, 0, 0);
}
.box {
  display: flex;
  justify-content: center;
  align-items: center;
  perspective: 1200px;
  
}

.bi {
  margin-top:5rem;
  background-color: #efefef;
  color: rgb(243, 130, 158);
  font-size: 5rem;
}

.book {
  margin: 2rem;
  transform-style: preserve-3d;
  position: relative;
  height: 300px;
  cursor: pointer;
  backface-visibility: visible;
  
  
}

.bookfront, .bookback, .page1, .page2, .page3, .page4, .page5, .page6 {
  transform-style: preserve-3d;
  position: absolute;
  width: 350px;
  height: 100%;
  top: 0; left: 0;
  transform-origin: left center;
  transition: transform .5s ease-in-out, box-shadow .35s ease-in-out;
}

.bookfront, .bookback {
  display: flex;
  flex-direction: column;
  border-bottom-right-radius: .5em;
  border-top-right-radius: .5em;
  background: rgb(186, 186, 251);
  box-shadow: 0 1em 3em 0 rgba(0, 0, 0, .2);
  padding: 30px
}

.front, .page1 {
  border-bottom-right-radius: .5em;
  border-top-right-radius: .5em;
  
}

.back, .page2{
  border-bottom-right-radius: .5em;
  border-top-right-radius: .5em;
}

.page1 { 
  background: #efefef;
  border-top-right-radius: .5em;

  padding: 10px
}
.pagecontent {
  display: flex;
  flex-wrap: wrap-reverse;
  justify-content: center;
  align-items: center;
  transform: scaleX(-1);
  background-color: #efefef;
}
.ticketimage {
  margin-right : 10px;
  margin-bottom : 10px;
  background-color: #efefef;
  background-image: url(../assets/오리지널\ 티켓\ 바탕핑크.png);
  background-size:120px 60px;
  width:120px;
  height: 60px;
}
.ticketimage > span {
  color:black;
  background-color: rgba(0, 0, 0, 0);
  font-size: 10px;
}
.pagecontent > span {
  color:black;
  background-color: #efefef;
  font-size: 10px;

}

.pagecontent > img {
  width:50%;
  background: #efefef;
  display: flex;
  justify-content: center;
  align-items: center;

}
.page2 {
  background: #efefef;
  padding: 10px;
  padding-top: 30px
}
.page2 > span {
  background: #efefef;
  color:black;

}

.book:hover .bookfront {
  transform: rotateY(-160deg) scale(1.1);
  box-shadow: 0 1em 3em 0 rgba(0, 0, 0, .2);
}

.book:hover .page1 {
  transform: rotateY(-150deg) scale(1.1);
  box-shadow: 0 1em 3em 0 rgba(0, 0, 0, .2);
}

.book:hover .page2 {
  transform: rotateY(-30deg) scale(1.1);
  box-shadow: 0 1em 3em 0 rgba(0, 0, 0, .2);
}

.book:hover .page3 {
  transform: rotateY(-140deg) scale(1.1);
  box-shadow: 0 1em 3em 0 rgba(0, 0, 0, .2);
}

.book:hover .page4 {
  transform: rotateY(-40deg) scale(1.1);
  box-shadow: 0 1em 3em 0 rgba(0, 0, 0, .2);
}

.book:hover .page5 {
  transform: rotateY(-130deg) scale(1.1);
  box-shadow: 0 1em 3em 0 rgba(0, 0, 0, .2);
}

.book:hover .page6 {
  transform: rotateY(-50deg) scale(1.1);
  box-shadow: 0 1em 3em 0 rgba(0, 0, 0, .2);
}

.book:hover .back {
  transform: rotateY(-20deg) scale(1.1);
}
</style>