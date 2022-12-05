<template>
  <div>
    <h1>TicketList</h1>
    <br>
    <button id="ticketcreatebtn" class="btn" @click="createList">티켓리스트 만들기</button>
    <div v-if="ticketlists">
      <br>
      <TicketListItem
        v-for="list in checkticketlists"
        :key="list.id"
        :ticketlist="list"
        :reviewlist="reviewlist"
        :movielist="movielist"
      />
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import TicketListItem from '@/components/TicketListItem'

export default {
  name:'ticketListView',
  components:{
    TicketListItem,
  },
  data(){
    return{
      ticketlists:[],
      reviewlist:[],
      movielist:[],
    }
  },
  computed:{
    checkLogin() {
      return this.$store.getters.checkLogin;
    },
    checkticketlists(){
      return this.ticketlists
    }
  },
  methods:{
    update(){
      this.$router.go()
    },
    createList(){
      this.$router.push({name:'createTicketList'})
    },
    whencreate() {
      axios({
      method:'get',
      url:'http://127.0.0.1:8000/ticketLists/'
    })
    .then(res=>{
      console.log(res.data);
      this.ticketlists=res.data
    })
    }
  },
  created(){
    console.log('created');
    axios({
      method:'get',
      url:'http://127.0.0.1:8000/ticketLists/'
    })
    .then(res=>{
      console.log(res.data);
      this.ticketlists=res.data
    })
    axios({
      method:'get',
      url:'http://127.0.0.1:8000/reviews/'
    })
    .then(res=>{
      // console.log(res.data);
      this.reviewlist=res.data
    })
    axios({
      method:'get',
      url:'http://127.0.0.1:8000/movies/'
    })
    .then(res=>{
      // console.log(res.data);
      this.movielist=res.data
    })
  },

}
</script>

<style>
#ticketcreatebtn {
  background-color: white; 
  color: #a0e7ca;
}
</style>