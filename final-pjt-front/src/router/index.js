import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import SignUp from '@/views/accounts/SignUp'
import LogIn from '@/views/accounts/LogIn'
import LogOut from '@/views/accounts/LogOut'
import MovieListView from '@/views/movies/MovieListView'
import ProfileView from '@/views/accounts/ProfileView'
import MovieDetailView from '@/views/movies/MovieDetailView'
import SearchView from '@/views/movies/SearchView'
import ReviewListView from '@/views/reviews/ReviewListView'
import ReviewCreateView from '@/views/reviews/ReviewCreateView'
import ReviewDetailView from '@/views/reviews/ReviewDetailView'
import ReviewUpdateView from '@/views/reviews/ReviewUpdateView'
import ticketListView from '@/views/articles/ticketListView'
import createTicketList from '@/views/articles/createTicketList'
import TicketListDetailView from '@/views/articles/TicketListDetailView'
import updateTicketList from '@/views/articles/updateTicketList'
import Not_Found_404 from '@/views/Not_Found_404'

Vue.use(VueRouter)

// const isLoggedIn=window.localStorage.getItem('jwt')? true:false

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/accounts/signup',
    name: 'SignUp',
    component: SignUp,
  },
  {
    path: '/accounts/login',
    name: 'LogIn',
    component: LogIn,
    // beforeEnter(to,from,next){
    //   if(isLoggedIn===true) {
    //     next({name:'home'})
    //   } else{
    //     next()
    //   }
    // }
  },
  {
    path: '/accounts/logout',
    name: 'LogOut',
    component: LogOut,
    // beforeEnter(to,from,next){
    //   if(isLoggedIn===true) {
    //     next()
    //   } else{
    //     next({name:'LogIn'})
    //   }
    // }
  },
  {
    path: '/accounts/:username',
    name: 'ProfileView',
    component: ProfileView,
    // beforeEnter(to,from,next){
    //   if(isLoggedIn===true) {
    //     next()
    //   } else{
    //     next({name:'LogIn'})
    //   }
    // }
  },
  {
    path: '/movies',
    name: 'MovieListView',
    component: MovieListView,
  },
  {
    path: '/movies/moviedetail/:movie_pk',
    name: 'MovieDetailView',
    component: MovieDetailView,
  },
  {
    path: '/reviews',
    name: 'ReviewListView',
    component: ReviewListView,
  },
  {
    path: '/search',
    name: 'SearchView',
    component: SearchView,
  },
  {
    path: '/reviews/:movie_id/create',
    name: 'ReviewCreateView',
    component: ReviewCreateView,
    // beforeEnter(to,from,next){
    //   if(isLoggedIn===true) {
    //     next()
    //   } else{
    //     next({name:'LogIn'})
    //   }
    // }
  },
  {
    path: '/reviews/reviewdetail/:review_pk',
    name: 'ReviewDetailView',
    component: ReviewDetailView,
  },
  {
    path: '/reviews/reviewupdate/:review_pk',
    name: 'ReviewUpdateView',
    component: ReviewUpdateView,
    // beforeEnter(to,from,next){
    //   if(isLoggedIn===true) {
    //     next()
    //   } else{
    //     next({name:'LogIn'})
    //   }
    // }
  },
  {
    path: '/ticketLists/',
    name: 'ticketListView',
    component: ticketListView,
  },
  {
    path: '/ticketLists/create',
    name: 'createTicketList',
    component: createTicketList,
    // beforeEnter(to,from,next){
    //   if(isLoggedIn===true) {
    //     next()
    //   } else{
    //     next({name:'LogIn'})
    //   }
    // }
  },
  {
    path: '/ticketLists/:ticketlist_pk',
    name: 'TicketListDetailView',
    component: TicketListDetailView,
  },
  {
    path: '/ticketLists/:ticketlist_pk/update',
    name: 'updateTicketList',
    component: updateTicketList,
  },
  {
    path: '*',
    name: 'Not_Found_404',
    component: Not_Found_404,
  },
  
]


const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
