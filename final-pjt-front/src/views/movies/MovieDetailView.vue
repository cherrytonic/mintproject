<template>
  <div>
    <h1>Detail</h1>
    
    <div class="wrapper">
	<div class="main_card">
		<div class="card_left">
			<div class="card_datails" v-if="movieInfo">
				<h3>{{ movieInfo[0].title }}</h3>
        <br>
				<div class="card_cat">
					<p class="year" v-if="movieInfo[0].release_date">{{ movieInfo[0].release_date }}</p>
					<p class="genre" v-for="genre in genre_list" :key="genre.id">{{ genre }} </p>
				</div>
				<span class="disc" v-if="movieInfo[0].overview">{{movieInfo[0].overview}}</span>
				<!-- <a href="https://www.imdb.com/title/tt4912910/" target="_blank">Read More</a> -->

			</div>
		</div>
		<div class="card_right">
			<div class="img_container" style="background-color: #fff;">
				<img :src="
                'https://image.tmdb.org/t/p/original/' +
                movieInfo[0].poster_path
                " alt="">
				</div>
        <br>
        <div class="social-btn">
        <button
          class="btn"
          @click="createReview(movieInfo[0])"
          style="background-color: #a0e7ca; color: white; font-size:20px">
          Review
        </button>
			</div>	
			</div>
		</div>
	</div>

  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "MovieDetailView",
  data: function () {
    return {
      movieId: this.$route.params.movie_pk,
      movieInfomation: null,
      genre_list: "",
      
    };
  },

  computed: {
    movieInfo() {
      return this.movieInfomation;
    },
    checkLogin() {
      return this.$store.getters.checkLogin;
    },
  },
  created() {
    // console.log(1,this.$route.params.genre_list);
    axios({
      method: "get",
      url: "http://127.0.0.1:8000/movies/",
    }).then((res) => {
      const movie = res.data.filter((movie) => {
        return movie.id == this.$route.params.movie_pk;
      });
      // console.log(movie,this.$store.state.genre_list);
      this.movieInfomation = movie;
      axios({
        method: "get",
        url: "http://127.0.0.1:8000/movies/genres/",
      }).then((res) => {
        console.log(res.data);
        // console.log(this.movieInfomation);

        const genre_list = res.data;
        console.log(1,movie,genre_list);
        const g_list=movie[0].genre_ids.map(g=>{
          for(const genre of genre_list){
            if(genre.id===g){
              return genre.name
            }
          }
        })
        this.genre_list = g_list;
        })
      })
  },
  methods: {
    createReview(movie) {
      this.$router.push({
        name: "ReviewCreateView",
        params: { movie_id: movie.id },
      });
    },
  },
};
</script>

<style scoped>

.main_card {
color: #fff;
border-radius: 10px;
width: 70rem;
height: 35rem;
margin: 50px auto;
display: -webkit-box;
display: -ms-flexbox;
display: flex;
max-width: 770px;
background: #00C9FF; 
background: -webkit-linear-gradient(to right, #92FE9D, #00C9FF);
background: -webkit-gradient(linear, left top, right top, from(#92FE9D), to(#00C9FF));
background: -webkit-linear-gradient(left, #92FE9D, #00C9FF);
background: -o-linear-gradient(left, #92FE9D, #00C9FF);
background: linear-gradient(to right, #92FE9D, #00C9FF); 
-webkit-box-shadow: 0 0 40px rgba(0,0,0,0.3); 
        box-shadow: 0 0 40px rgba(0,0,0,0.3);
}

.card_left {
border-top-left-radius: 10px;
border-bottom-left-radius: 10px;
width: 90%;
background-color: #fff;
}

.card_datails {
background-color: #fff;
width: 90%;
padding-top:30px;
padding-left: 30px;
border-top-left-radius: 10px;
border-bottom-left-radius: 10px;

}
.card_datails  h3 {
font-size: 30px;
color: black;
background-color: #fff;
border-top-left-radius: 10px;
border-bottom-left-radius: 10px;

}
.card_right img {
height: 350px;
border-radius: 10px;
background-color: white;
box-shadow: 0 0 50px rgba(0,0,0,0.2);

}
.card_right {
background-color: #fff;
padding-right: 30px;
padding-top: 30px;
border-top-right-radius: 10px;
border-bottom-right-radius: 10px;
}

.card_cat {
background-color: #fff;
width: 100%;
display: -webkit-box;
display: -ms-flexbox;
display: flex;
-webkit-box-pack: justify;
    -ms-flex-pack: justify;
        justify-content: center;
}

.PG, .year, .genre, .time {
	background-color: #99532a;
	padding: 10px;
	border-radius: 15px;
  color: white;
  margin-right:0.3rem
}


.disc {
	font-weight: 100;
	line-height: 27px;
  color: black;
  background-color: #fff;
}
a {
	color: darkcyan;
	display: block;
	text-decoration: none;
  
}
.social-btn {
  background-color: #fff;
}
button {
color:#a0e7ca;;
border: none;
padding: 20px;
outline: none;
font-size: 12px;
margin-top: 30px;
margin-left: 10px;
background:#a0e7ca;
border-radius: 12px;
-webkit-box-shadow: 0 0 20px rgba(0,0,0,0.2);
        box-shadow: 0 0 20px rgba(0,0,0,0.2);
-webkit-transition: 300ms ease-in-out;
-o-transition: 200ms ease-in-out;
transition: 200ms ease-in-out;
}

button:hover {
-webkit-transform: scale(1.1);
    -ms-transform: scale(1.1);
        transform: scale(1.1);
}

</style>