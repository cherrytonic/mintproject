<template>
  <div>

    <div class="card my-1" id="card" @click="toDetail(genre_list)">
      <div class="p-3">
        <img :src="img_url" class="card-img-top" alt="...">
      </div>
      <div class="card-body">
        <span class="card-title">{{movie.title}}</span>
        <br>
        <!-- <span>장르 : </span>
        <span class="card-text" >{{genre_list}}</span> -->
      </div>      
    </div>

    
    <!-- <router-link :to="{name: 'MovieDetail', params: {movieId:movie.id}}"></router-link> -->
  </div>
</template>

<script>
import axios from 'axios'
export default {
    name: 'MovieListItem',
    props: {
        movie:Object,
    },
    data (){
        return {
            img_url : 'https://image.tmdb.org/t/p/original' + this.movie.poster_path,
            detail_url: `http://localhost:8080/movies/moviedetail/${this.movie.id}`,
            genre_list:[]
        }
    },
    computed:{
      checkLogin() {
      return this.$store.getters.checkLogin;
    },
      // genres(){
      //   const genres=this.movie.genre_ids.map(genre=>{
          
      //   })
      //   return 
      // },
    },
    methods: {
      toDetail(genre_list) {
        this.$router.push({name: 'MovieDetailView', params: {movie_pk:this.movie.id, genre_list:genre_list}})
      },
      },
    created(){
      axios({
        method:'get',
        url:'http://127.0.0.1:8000/movies/genres/'
    })
    .then(res=>{
        // console.log(res.data);
        const genre_list=res.data
        const g_list=this.movie.genre_ids.map(genre=>{
          for(const g of genre_list){
            if (genre===g.id){
              return g.name
            }
          }
        })
        this.genre_list=g_list
    })
    }
    }

</script>

<style scoped>

a {
  text-decoration: none;
}

.card-title {
  text-decoration: none;
  color: black;
  background-color: white;
}
.card-body {
  background-color: white;
  border-radius: 10px;
}
.card-text {
  background-color: white;
  color: black
}
.card-body > span {
  background-color: white;
  color: black
}

img {
  border-radius: 10px;
}

.p-3 {
  background-color: white;
  border-radius: 10px;
}

#card {
  border-radius: 10px;
}
</style>