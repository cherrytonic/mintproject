<template>
  <div class="row d-flex justify-content-center">
    <div class="row col-10">

    <MovieListItem
    v-for="movie in movieList"
    :movie="movie"

    :key="movie.id"
    class="col-sm-6 col-lg-4 ti"
    :genre_list="genre_list"
    />
    
    <!-- {{movieList}} -->
  

    </div>

   
    
  </div>
</template>

<script>
import axios from 'axios'
import MovieListItem from '@/components/MovieListItem'
export default {
    name:'MovieListView',
    components: {
        MovieListItem,
    },

    data(){
        return{
            list:null,
            genre_list:null,
        }
    },
    methods:{
        getMovieList(){
            axios({
                method:'get',
                url:'http://127.0.0.1:8000/movies/'
            })
            .then((res) =>{
                console.log(res)
                this.$store.commit('PUSH_MOVIES', res.data)
            })
            .catch((err) => {
                console.log(err)
            })
        }
    },
    computed: {
        movieList() {
            return this.$store.state.movieList
        },
    checkLogin() {
      return this.$store.getters.checkLogin;
    },
    },
    created: function() {
    this.getMovieList()
    
    },

}
</script>

<style>

</style>