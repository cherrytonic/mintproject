<template>
  <div>
    <h1>티켓리스트 만들기</h1>
    <div class="outer">
      <form @submit.prevent="makeTicketList" class="inner">
        <div class="row align-items-center">
          <div class="col-auto">
            <label for="ticketListName">TicketList Name : </label>
          </div>
        </div>
        <div class="row g-1 align-items-center">
          <div class="col">
            <input
              class="form-control"
              type="text"
              id="ticketListName"
              v-model="ticketListName"
            /><br />
          </div>
        </div>

        <div class="row g-3 align-items-center">
          <div class="col-auto">
            <label for="content"> content : </label>
          </div>
        </div>
        <div class="row g-1 align-items-center">
          <div class="col">
            <input
              class="form-control"
              type="text"
              id="content"
              v-model="content"
            /><br />
          </div>
        </div>

        <div class="row g-3 align-items-center">
          <div class="col-auto">
            <label for="selectedTickets">Select Tickets : </label>
          </div>
        </div>
        <div class="row g-3 align-items-center">
          <div class="col">
            <div
              type="button"
              class="btn btn-outline-light mx-1 my-1"
              v-for="review in reviews"
              :key="review.id"
              @click="select_tickets(review)"
              :class="{ selected: review.selected }"
            >
              {{ review.title }}
            </div>
          </div>
        </div>
        <br />
        <button
          type="submit"
          data-bs-toggle="modal"
          data-bs-target="#exampleModal"
          class="btn"
          style="background-color: white; color: #a0e7ca"
        >
          Make TicketList
        </button>
      </form>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "createTicketList",
  data() {
    return {
      reviews: [],
      ticketListName: "",
      content: "",
      selectedTickets: [],
    };
  },
  computed:{
    checkLogin() {
      return this.$store.getters.checkLogin;
    },
  },
  methods: {
    select_tickets(review) {
      review.selected = !review.selected;
      if (this.selectedTickets.includes(review.id)) {
        this.selectedTickets.pop(review.id);
      } else {
        this.selectedTickets.push(review.id);
      }
    //   console.log(this.selectedTickets);
    },
    makeTicketList(){
        if(!this.ticketListName){
          alert('제목을 입력해주세요!')
          return
        }
        else if(this.ticketListName.length>18){
          alert('제목은 18자 이내여야합니다.')
          return
        }
        else if(!this.content){
          alert('내용을 입력해주세요!')
          return
        }
        else if(this.selectedTickets.length<2){
            alert('2개 이상의 티켓을 선택해 주세요!')
            return
        } else if (this.selectedTickets.length > 8){
            alert('8개 이하의 티켓을 선택해 주세요!')
            return
        }

        const payload={
            ticketListName:this.ticketListName,
            content:this.content,
            selectedTickets:JSON.stringify(this.selectedTickets),
            username:localStorage.getItem('username')
        }
        axios({
            method:'post',
            url:'http://127.0.0.1:8000/ticketLists/create/',
            data:payload
        })
        .then(res=>{
            console.log(res);
            this.$router.push({name:'ticketListView'})
        }
        )
        .catch(
            // alert('다시 입력해주세요!')
        )
    }
  },
  created() {
    if(!this.checkLogin){
          this.$router.push({name:'LogIn'})
        }
    axios({
      method: "get",
      url: "http://127.0.0.1:8000/reviews/",
    }).then((res) => {
        const reviewlist=res.data
      axios({
        method: "get",
        url: `http://127.0.0.1:8000/accounts/getUserdata/${localStorage.getItem('username')}`,
      }).then((res) => {
        // console.log('user', res.data.id);
        const reviews = reviewlist.filter((review) => {
        // console.log(review.user,res.data.id);
        if (review.user === res.data.id) {
          review["selected"] = false;
          return review;
        }
    });
    this.reviews = reviews;
    // console.log(reviews);
      });
    });
  },
};
</script>

<style>
.outer {
  margin-left: 10rem;
  margin-right: 10rem;
}
.selected{
    background-color: #99532a !important;
    color: white !important;
}
</style>