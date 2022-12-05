import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    movieList: null,
    reviewList: [],
    isLogined:false,
    nickname:''
  },
  getters: {
    checkLogin(state){
      // console.log(state.isLogined);
      return state.isLogined
    },
    getMovieList(state){
      return state.movieList
    },
    getNickname(state){
      return state.nickname
    }
  },
  mutations: {
    PUSH_MOVIES(state, movieList) {
      state.movieList = movieList
    },
    PUSH_REVIEWS(state, reviewList) {
      state.reviewList = reviewList
    },
    CHANGE_LOGIN_STATE(state,condition){
      if(condition==='login' && state.isLogined===false){
        state.isLogined=true
      } else if(condition==='logout' && state.isLogined===true){
        state.isLogined=false
      }
    },
    SAVE_NICKNAME(state,nickname){
      state.nickname=nickname
    }
    // CREATE_REVIEW(state, payload) {
    //   state.reviewList.push(payload)
    //   state.reviewList.id += 1
    //   console.log(state.reviewList)
    // }
  },
  actions: {
    // createReview(context, payload) {
    //   const review = {
    //     title: payload.title,
    //     content: payload.content
    //   }
    //   context.commit('CREATE_REVIEW', review)
    //   console.log(payload)
    // }
    changeLoginState(context,condition){
      context.commit('CHANGE_LOGIN_STATE',condition)
    }
  },
  modules: {
  }
})
