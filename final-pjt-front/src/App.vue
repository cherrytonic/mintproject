<template>
  <div id="app">
    <nav v-if="checkLogin">
      <div class="row justify-content-between">
        <div class="col-3 mx-3">
          <router-link to="/">
            <img id="logo" src="./assets/whitelogo.png" alt="" />
          </router-link>
        </div>
        <div class="col-5 mt-5">
          <router-link :to="{ name: 'MovieListView' }">Movies</router-link> |
          <router-link :to="{ name: 'ReviewListView' }">Reviews</router-link> |
          <router-link :to="{ name: 'ticketListView' }"
            >Ticket List</router-link
          >
          |
          <router-link :to="{ name: 'SearchView' }">Search</router-link>
        </div>
        <div class="col-3 mt-5">
          <button
              class="btn btn-nav"
              style="color: #a0e7ca; background-color: white"
              @click="toMyProfile"
            >
              Profile
            </button>
          <router-link
            :to="{ name: 'LogOut', params: { is_logined: is_logined } }"
            ><button
              class="btn btn-nav"
              style="color: #a0e7ca; background-color: white"
            >
              Logout
            </button></router-link
          >
          <br />
          <br>
          <span v-if="checkLogin">Hello, </span>
          <span v-if="getnickname"> {{ getnickname }}💖</span>
          <span v-if="!getnickname">{{ getlocalnickname }}💖</span>
        </div>
      </div>
    </nav>
    <nav v-else>
      <div class="row justify-content-between">
        <div class="col-3 mx-3">
          <router-link to="/">
            <img id="logo" src="./assets/whitelogo.png" alt="" />
          </router-link>
        </div>
        <div class="col-5 mt-5">
          <router-link :to="{ name: 'MovieListView' }">Movies</router-link> |
          <router-link :to="{ name: 'ReviewListView' }">Reviews</router-link> |
          <router-link :to="{ name: 'ticketListView' }"
            >Ticket List</router-link
          >
          |
          <router-link :to="{ name: 'SearchView' }">Search</router-link>
        </div>
        <div class="col-3 mt-5">
          <router-link :to="{ name: 'SignUp' }">
            <button
              class="btn btn-nav"
              style="color: #a0e7ca; background-color: white"
            >
              Signup
            </button>
          </router-link>
          <router-link :to="{ name: 'LogIn' }">
            <button
              class="btn btn-nav"
              style="color: #a0e7ca; background-color: white"
            >
              Login
            </button>
          </router-link>
        </div>
      </div>
    </nav>
    <br>
    <transition :name="transitionName">
      <router-view @login="login" @logout="logout" />
    </transition>
  </div>
</template>

<script>
export default {
  name: "App",
  data: function () {
    return {
      is_logined: false,
      username: null,
      transitionName: "",
      nickname:''
    };
  },
  watch: {
    $route(to, from) {
      if (to.meta.page == null || from.meta.page == null) {
        this.transitionName = "fade";
        console.log(this.transitionName);
      }
    },
  },
  computed: {
    checkLogin() {
      return this.$store.getters.checkLogin;
    },
    getnickname(){
      return this.$store.getters.getNickname
    },
    getlocalnickname(){
      return JSON.parse(localStorage.getItem('userdata')).nickname
    }
  },
  methods: {
    toMyProfile(){
      this.$router.push({name:'ProfileView', params:{username:localStorage.getItem('username')}})
    },
    logined() {
      if (!this.is_logined) {
        this.is_logined = true;
      }
      console.log(this.is_logined);
    },
    is_authenticated() {
      if (window.localStorage.getItem("jwt")) {
        this.is_logined = true;
        this.username = localStorage.getItem("username");
        this.nickname=JSON.parse(localStorage.getItem('userdata')).nickname
        this.$store.dispatch("changeLoginState", "login");
      } else {
        this.is_logined = false;
      }
    },
    login() {
      this.username = localStorage.getItem("username");
      console.log('login');
      // this.$forceUpdate();
      // this.$router.go()
    },
    logout() {
      this.is_logined = false;
      this.username = null;
    },
  },
  created() {
    this.is_authenticated();
    // this.getnickname()
    // this.nickname=JSON.parse(localStorage.getItem('userdata')).nickname
  },
  updated(){
    // this.getnickname
  }
};
</script>

<style>
@font-face {
  font-family: "Ycomputer-Regular";
  src: url("https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_11-01@1.0/Ycomputer-Regular.woff2")
    format("woff2");
  font-weight: normal;
  font-style: normal;
}

html {
  background-color: #a0e7ca;
}
.fade-enter-active,
.fade-leave {
  transition: opacity 0.8s;
}
.fade-enter,
.fade-leave-to {
  opacity: 0;
}

.col-10 mt-5 {
  justify-content: end;
}

#app {
  background-color: #a0e7ca;
  font-family: "Ycomputer-Regular";
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #f8f8f8;
}

#logo {
  width: 10rem;
  height: 8rem;
  padding: 1rem;
}
nav {
  /* padding: 30px; */
  align-content: space-around;
}

nav a {
  /* font-weight: bold; */
  color: #ffffff;
  text-decoration: none;
  font-size: 20px;
}

nav a:hover {
  /* font-weight: bold; */
  color: #99532a;
  text-decoration: none;
  font-size: 20px;
}

nav a.router-link-exact-active {
  color: #99532a;
  font-weight: bold;
  font-size: 20px;
}

.btn-nav {
  color: #a0e7ca;
  background-color: white;
  margin-right: 10px;
}
</style>
