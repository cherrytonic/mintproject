<template>
  <div>
    <br>
    <div class="profileticket">
      <br>
      <div class="row">
        <div id="leftcol" class="col ms-5 pt-5 pb-4 " >
          <h1>{{ nowNickname }}님의 Profile</h1>
        <div>
          <br>
          <hr style="height: 3px; background: white">
          <div>
            <span>Followings {{ following }}</span>
            <br>
            <span>Followers {{ follower }}</span>
          </div>
          <br>
          <div v-show="username!=nowUser" @click="followfunc">
            <button class="btn" v-if="is_followed">Unfollow</button>
            <button class="btn" v-else>Follow</button>
          </div>
        </div>
      </div>
      <div id="rightcol" class="col me-5 py-5">
        <div>
          <h3>{{nowNickname}}님의 Reviews</h3>
      <div class="reviewbox scrollbar" v-if="myReviews">
        <br>
        <p v-for="review in myReviews" :key="review.id">{{review.title}}   </p>
      </div>
      <hr style="height: 3px; background: white">
      </div>
      <h3>{{nowNickname}}님의 Ticket Lists</h3>
      <div class="listbox scrollbar" v-if="myTicketlists">
        <br>
        <p v-for="list in myTicketlists" :key="list.id">{{list.title}}   </p>
      </div>
    </div>
    </div>
      
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
    name:'ProfileView',
    data(){
      return{
        username:this.$route.params.username,
        nickname:'',
        following:0,
        follower:0,
        is_followed:false,
        myReviews:[],
        myTicketlists:[]
      }
    },
    methods:{
      followfunc(){
        axios({
          method:'post',
          url:`http://127.0.0.1:8000/accounts/follow/${this.username}/`,
          headers: { 'Authorization': `Bearer ${localStorage.getItem('jwt')}`}
        })
        .then(res=>{
          const data=res.data
          this.is_followed=data.is_followed
          this.following=data.followings_count
          this.follower=data.followers_count
        })
      }

    },
    computed:{
      nowUser(){
        return JSON.parse(localStorage.getItem('userdata')).username
      },
      nowNickname(){
        return this.nickname
      },
      checkLogin() {
      return this.$store.getters.checkLogin;
    },
      // is_followed(){
      //   return this.is_followed
      // }
    },
    created(){
      axios({
        method:'get',
        url:`http://127.0.0.1:8000/accounts/getUserdata/${this.username}/`,
      })
      .then(res =>{
        // console.log(res,localStorage.getItem('userdata'))
        const data=res.data
        // console.log(res.data.is_followed);
        // console.log(data);
        this.is_followed=data.follow_list.includes(localStorage.username) ? true:false
        this.following=data.followings_count
        this.follower=data.followers_count
        this.nickname=res.data.nickname
        // console.log(1,data.is_followed);
        axios.get('http://127.0.0.1:8000/reviews')
        .then(res=>{
          // console.log(res.data);
          const myReviews=res.data.filter(review=>{
            if(review.user==data.id){
              return review
            }
          })
          this.myReviews=myReviews
          axios.get('http://127.0.0.1:8000/ticketLists')
          .then(res=>{
            // console.log(res.data);
            const myTicketlists=res.data.filter(list=>{
              if(list.user==data.id){
                return list
              }
            })
            this.myTicketlists=myTicketlists
          })
        })
      })
      .catch(err=>{
        console.log(err);
        this.$router.push({name:'Not_Found_404'})
      })
    },
    beforeRouteUpdate(to,from,next){
      console.log(to);
      this.username=to.params.username
      next()
     }
}
</script>

<style scoped>
.profileticket {
  margin:0 auto;
  background-image: url(../../assets/오리지널\ 티켓\ 바탕핑크.png);
  background-size:50rem 25rem;
  width: 50rem;
  height: 25rem;
}

#leftcol {
  border-style: solid; border-right-style: dashed;
  width: 35rem;
  height:22rem;
}
#rightcol {
  border-style: solid; border-left-style: none;
  width: 35rem;
  height:22rem;
}

.reviewbox {
  height: 5rem;
  overflow-y:scroll; 
  overflow-x:hidden;
  scroll-behavior: smooth;
  padding-right: 2rem;
  padding-left: 2rem;
}
.listbox {
  height: 5rem;
  overflow-y:scroll; 
  overflow-x:hidden;
  scroll-behavior: smooth;
  padding-right: 2rem;
  padding-left: 2rem;
}
.scrollbar::-webkit-scrollbar-track
{
	-webkit-box-shadow: inset 0 0 6px rgba(0,0,0,0.3);
	border-radius: 10px;
	background-color: white
}

.scrollbar::-webkit-scrollbar
{
	width: 12px;
	background-color: rgb(0, 0, 0, 0)
}

.scrollbar::-webkit-scrollbar-thumb
{
	border-radius: 10px;
	-webkit-box-shadow: inset 0 0 6px rgba(0,0,0,.3);
	background-color: #a0e7ca;
}

p {
  background-color: rgb(0, 0, 0, 0);
  font-size:23px
}
span {
  background-color: rgb(0, 0, 0, 0);
  font-size:23px
}

.btn {
  color: #a0e7ca;
  background-color: white;
  font-size:25px
}
</style>