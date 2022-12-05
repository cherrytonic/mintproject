<template>
  <div class="home">
    <img
      alt="Vue logo"
      src="../assets/whitelogotitle.png"
      v-if="checkLogin === false"
    />
    <div v-if="checkLogin">
      <!-- <span v-if="nowmovie">{{nowmovie}}</span> -->
      <h3>👋어서오세요, {{ getUserNickname }}님!</h3>
      <br />
      <div class="d-flex">
        <div class="container" v-if="getRecommendedListPosterPath">
          <h5>🎬{{ getUserNickname }}님께 추천하는 영화🎬</h5>
          <div class="thing">
            <div class="carousel">
              <ul class="slides">
                <input
                  ref="start"
                  type="radio"
                  name="radio-buttons"
                  id="img-1"
                  value="1"
                  v-model="nowmovie"
                />
                <li class="slide-container">
                  <div class="slide-image">
                    <img
                      v-if="recommended_list"
                      :src="
                        'https://image.tmdb.org/t/p/original/' +
                        getRecommendedListPosterPath[1]
                      "
                      alt="Sample 1"
                    />
                  </div>
                  <div class="carousel-controls">
                    <label for="img-3" class="prev-slide">
                      <span style="background-color: rgba(0, 0, 0, 0)"
                        >&lsaquo;</span
                      >
                    </label>
                    <label for="img-2" class="next-slide">
                      <span style="background-color: rgba(0, 0, 0, 0)"
                        >&rsaquo;</span
                      >
                    </label>
                  </div>
                </li>
                <input
                  type="radio"
                  name="radio-buttons"
                  id="img-2"
                  value="0"
                  v-model="nowmovie"
                />
                <li class="slide-container">
                  <div class="slide-image">
                    <img
                      v-if="recommended_list"
                      :src="
                        'https://image.tmdb.org/t/p/original/' +
                        getRecommendedListPosterPath[0]
                      "
                      alt="Sample 1"
                    />
                  </div>
                  <div class="carousel-controls">
                    <label for="img-1" class="prev-slide">
                      <span style="background-color: rgba(0, 0, 0, 0)"
                        >&lsaquo;</span
                      >
                    </label>
                    <label for="img-3" class="next-slide">
                      <span style="background-color: rgba(0, 0, 0, 0)"
                        >&rsaquo;</span
                      >
                    </label>
                  </div>
                </li>
                <input
                  type="radio"
                  name="radio-buttons"
                  id="img-3"
                  value="2"
                  v-model="nowmovie"
                />
                <li class="slide-container">
                  <div class="slide-image">
                    <img
                      v-if="recommended_list"
                      :src="
                        'https://image.tmdb.org/t/p/original/' +
                        getRecommendedListPosterPath[2]
                      "
                      alt="Sample 1"
                    />
                  </div>
                  <div class="carousel-controls">
                    <label for="img-2" class="prev-slide">
                      <span style="background-color: rgba(0, 0, 0, 0)"
                        >&lsaquo;</span
                      >
                    </label>
                    <label for="img-1" class="next-slide">
                      <span style="background-color: rgba(0, 0, 0, 0)"
                        >&rsaquo;</span
                      >
                    </label>
                  </div>
                </li>
                <div class="carousel-dots">
                  <label
                    for="img-1"
                    class="carousel-dot"
                    id="img-dot-1"
                  ></label>
                  <label
                    for="img-2"
                    class="carousel-dot"
                    id="img-dot-2"
                  ></label>
                  <label
                    for="img-3"
                    class="carousel-dot"
                    id="img-dot-3"
                  ></label>
                </div>
              </ul>
            </div>
          </div>
          <br />
          <button
            class="btn"
            style="color: #a0e7ca; background-color: white"
            @click="toDetail"
          >
            영화 정보 보기
          </button>
        </div>
      <div class="container" v-if="getLatestMovie">
          <h5>🎬최고 평점 영화🎬</h5>
          <!-- {{getLatestMovie}} -->
          <div class="thing">
              <ul class="slides">
                <li class="slide-container">
                  <div>
                    <img
                      id="latest"
                      v-if="recommended_list"
                      :src="
                        'https://image.tmdb.org/t/p/original' +
                        getLatestMovie.poster_path
                      "
                      alt="Sample 1"
                    />
                  </div>
                </li>
              </ul>
          </div>
          <br/>
          <button
            class="btn"
            style="color: rgba(0, 0, 0, 0); background-color: none"
          >
            영화
          </button>
        </div>
      </div>

    </div>
    <div v-else>
      <button
        class="btn"
        @click="toLogin"
        style="background-color: white; color: #a0e7ca"
      >
        Login
      </button>
    </div>
  </div>
</template>


<script>
import axios from "axios";
import _ from "lodash";

export default {
  name: "HomeView",
  components: {},
  data() {
    return {
      isLogined: false,
      userNickname: "",
      recommended_list: [],
      nowmovie: 1,
      latest_movie: [],
    };
  },

  computed: {
    getUserNickname() {
      if (localStorage.userdata) {
        // console.log(JSON.parse(localStorage.userdata).genre_preference);
        return JSON.parse(localStorage.userdata).nickname;
      } else {
        return "";
      }
    },
    checkLogin() {
      return this.$store.getters.checkLogin;
    },
    getMovieList() {
      return this.$store.getters.getMovieList;
    },
    getnowmovie() {
      return this.nowmovie;
    },
    getRecommendedListPosterPath() {
      const posterPath = this.recommended_list.map((list) => {
        return list.poster_path;
      });
      return posterPath;
    },
    getLatestMovie() {
      return this.latest_movie;
    },
  },
  methods: {
    toLogin() {
      this.$router.push({ name: "LogIn" });
    },
    check() {
      console.log("working");
    },
    toDetail() {
      console.log(this.recommended_list[this.nowmovie]);
      this.$router.push({
        name: "MovieDetailView",
        params: { movie_pk: this.recommended_list[this.nowmovie].id },
      });
    },
  },
  created() {
    if (localStorage.userdata) {
      this.$store.dispatch("changeLoginState", "login");
      axios({
        method: "get",
        url: "https://api.themoviedb.org/3/movie/top_rated?api_key=6926066b36f74d1dcd318f8bffc059c1&language=ko-KR&page=1",
      }).then((res) => {
        console.log(res.data.results[0].poster_path);
        this.latest_movie = res.data.results[0];
      });

      axios({
        method: "get",
        url: "http://127.0.0.1:8000/movies/",
      })
        .then((res) => {
          // console.log(res.data)
          this.$store.commit("PUSH_MOVIES", res.data);
          const recommended = res.data.filter((movie) => {
            // console.log(1,movie.genre_ids,JSON.parse(JSON.parse(localStorage.userdata).genre_preference))
            for (const id of JSON.parse(
              JSON.parse(localStorage.userdata).genre_preference
            )) {
              if (movie.genre_ids.includes(id)) {
                return movie;
              }
            }
          });
          // for(const movie of recommended){
          //   console.log(movie.title);
          // }
          this.recommended_list = _.sampleSize(recommended, 3);
          // console.log(this.recommended_list[1]);
        })
        .catch((err) => {
          console.log(err);
        });
    }
  },
};
</script>

<style>
.container {
  margin: 20px;
  display: flex;
  background-color: rgba(255, 255, 255, 0);
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.thing {
  padding: 1rem;
  width: 420px;
  box-shadow: 0 15px 30px 0 rgba(0, 0, 0, 0.11),
    0 5px 15px 0 rgba(0, 0, 0, 0.08);
  background-color: rgba(255, 255, 255);
  border-radius: 0.5rem;

  border-left: 0 solid #00ff99;
  transition: border-left 300ms ease-in-out, padding-left 300ms ease-in-out;
}

.thing:hover {
  padding-left: 0.5rem;
  border-left: 0.5rem solid #00ff99;
}

.thing > :first-child {
  margin-top: 0;
}

.thing > :last-child {
  margin-bottom: 0;
}

.heading {
  color: #fff;
}

.btn:hover {
  background-color: #99532a !important;
  color: white !important;
}

.detailbtn {
  background-color: #99532a !important;
  color: white !important;
}

.cbox {
  height: 100%;
  width: 100%;
  margin: 0 auto;
}

ul.slides {
  display: block;
  position: relative;
  height: 600px;
  margin: 0;
  padding: 0;
  overflow: hidden;
  list-style: none;
}

.slides * {
  user-select: none;
  -ms-user-select: none;
  -moz-user-select: none;
  -khtml-user-select: none;
  -webkit-user-select: none;
  -webkit-touch-callout: none;
}

ul.slides input {
  display: none;
}

.slide-container {
  display: block;
}

.slide-image {
  display: block;
  position: absolute;
  width: 100%;
  height: 100%;
  top: 0;
  opacity: 0;
  transition: all 0.7s ease-in-out;
}

.slide-image img {
  width: auto;
  min-width: 100%;
  height: 100%;
}

.carousel-controls {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  z-index: 999;
  font-size: 100px;
  line-height: 600px;
  color: #fff;
}

.carousel-controls label {
  display: none;
  position: absolute;
  padding: 0 20px;
  opacity: 0;
  transition: opacity 0.2s;
  cursor: pointer;
}

.slide-image:hover + .carousel-controls label {
  opacity: 0.5;
}

.carousel-controls label:hover {
  opacity: 1;
}

.carousel-controls .prev-slide {
  width: 49%;
  text-align: left;
  left: 0;
  background-color: rgba(0, 0, 0, 0);
}

.carousel-controls .next-slide {
  width: 49%;
  text-align: right;
  right: 0;
  background-color: rgba(0, 0, 0, 0);
}

.carousel-dots {
  position: absolute;
  left: 0;
  right: 0;
  bottom: 20px;
  z-index: 999;
  text-align: center;
  background-color: rgba(0, 0, 0, 0);
}

.carousel-dots .carousel-dot {
  display: inline-block;
  width: 30px;
  height: 30px;
  border-radius: 50%;
  background-color: #fff;
  opacity: 0.5;
  margin: 10px;
}

input:checked + .slide-container .slide-image {
  opacity: 1;
  transform: scale(1);
  transition: opacity 1s ease-in-out;
}

#latest{
  max-width:388px;
  max-height:600px;
}

input:checked + .slide-container .carousel-controls label {
  display: block;
}

input#img-1:checked ~ .carousel-dots label#img-dot-1,
input#img-2:checked ~ .carousel-dots label#img-dot-2,
input#img-3:checked ~ .carousel-dots label#img-dot-3,
input#img-4:checked ~ .carousel-dots label#img-dot-4,
input#img-5:checked ~ .carousel-dots label#img-dot-5,
input#img-6:checked ~ .carousel-dots label#img-dot-6 {
  opacity: 1;
}

input:checked + .slide-container .nav label {
  display: block;
}
</style>