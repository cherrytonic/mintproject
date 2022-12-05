<template>
  <div>
    <MovieSearch @search-text="onSearchEnter" />
    <!-- <span>{{ searchkeyword }}</span> -->
    <br>
    <div class="row d-flex justify-content-center">
      <div class="row col-6" v-if="searched">
        <div v-if="movielist">
          <div v-for="movie in movielist" :key="movie.id">
            <div class="card" id="card" style="margin-bottom: 2rem; background-color: white;">
              <div class="p-3">
                <img
                  :src="
                    'https://image.tmdb.org/t/p/original/' + movie.poster_path
                  "
                  class="card-img-top"
                  alt="..."
                />
              </div>
              <div class="card-body">
                <h3 class="card-title">{{ movie.title }}</h3>
                <button class="btn" style="color: white;
  background-color: #a0e7ca;" @click="toDetail">영화 정보 보기</button>
                <!-- <p>{{movielist[0]}}</p> -->
                <!-- <span>장르 : </span>
        <span class="card-text" >{{genre_list}}</span> -->
              </div>
            </div>
          </div>
        </div>
      </div>
      <div v-else>
        <p>검색결과가 없습니다...🔍</p>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import MovieSearch from "@/components/MovieSearch.vue";
// import MovieListItem from '@/components/MovieListItem'

export default {
  name: "SearchView",
  components: { MovieSearch },
  data() {
    return {
      searchResult: "",
      searchkeyword: "",
      search: "",
      movielist: [],
      searched: false,
    };
  },
  computed: {
    checkLogin() {
      return this.$store.getters.checkLogin;
    },
  },
  methods: {
    // searchInput(keyword) {
    //   console.log(keyword);

    // },
    onSearchEnter(word) {
      axios({
        method: "get",
        url: "http://127.0.0.1:8000/movies/",
      })
        .then((res) => {
          // console.log(res);
          const list = res.data.filter(function (movie) {
            return movie.title.includes(word);
          });
          if(list.length!=0){
            this.movielist = list
            this.searched = true
          }else{
            this.searched =false
          }
          // console.log(this.searched);
        })
        .catch((err) => {
          console.log(err);
        });
    },
    toDetail() {
      this.$router.push({
        name: "MovieDetailView",
        params: { movie_pk: this.movielist[0].id },
      });
    },
  },
};
</script>

<style scoped>
.btn {
  background-color: #99532a;
  color: white;
}
.card {
  background-color: white;
}

.p-3 {
  background-color: rgb(0, 0, 0,0)
}
.card-body {
  background-color: rgb(0, 0, 0,0)
}
.card-title {
  background-color: rgb(0, 0, 0,0);
  color: #000;
}
</style>