import Vue from 'vue'
import App from './App.vue'
import store from './store'
import router from './router'
import axios from 'axios'
import "bootstrap/dist/css/bootstrap.min.css"
import "bootstrap-icons/font/bootstrap-icons.css";
import VueSplide from '@splidejs/vue-splide';


Vue.config.productionTip = false

new Vue({
  store,
  router,
  axios,
  VueSplide,
  render: h => h(App)
}).$mount('#app')
