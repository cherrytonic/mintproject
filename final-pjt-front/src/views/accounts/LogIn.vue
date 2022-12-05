<template>
  <div>
    <h1>Login</h1>
    <br>
    <div class="outer">
    <form @submit.prevent="login" class="inner">
      <div class="row g-3 align-items-center">
        <div class="col-auto">
          <label for="username" style="color: white;">username : </label>
        </div>
      </div>
      <div class="row g-3 align-items-center">
        <div class="col">
          <input class="form-control" type="text" id="username" v-model="username"><br>
        </div>
      </div>
      <div class="row g-3 align-items-center">
        <div class="col-auto">
          <label for="password" style="color: white;"> password : </label>
        </div>
      </div>
      <div class="row g-3 align-items-center">
        <div class="col">
          <input class="form-control" type="password" id="password" v-model="password"><br>
        </div>
      </div>
      <button type="submit"  class="btn" style="background-color: white; color: #a0e7ca;">Login</button>
    </form>
  </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'LogIn',
  data: function () {
    return {
      username:null,
      password:null,
    }
  },
  computed:{
    
  },
  methods: {
    login: function () {
      axios({
        method:'post',
        url:'http://127.0.0.1:8000/api/token/',
        data:{ 
          'username' : this.username,
          'password' : this.password
        }
      })
        .then(res => {
          // console.log(res.data);
          const jwt=res.data.access
          // console.log(jwt);
          window.localStorage.setItem('jwt',jwt)
          window.localStorage.setItem('username',this.username)
          this.$emit('login')
          this.$store.dispatch('changeLoginState','login')
          // console.log('Logined haha');
          axios({
            method:'get',
            url:`http://127.0.0.1:8000/accounts/getUserdata/${this.username}/`
          })
            .then(res=>{
              console.log(1,res.data);
              window.localStorage.setItem('userdata',JSON.stringify(res.data))
              this.$store.commit('SAVE_NICKNAME',res.data.nickname)
            })
            .then(()=>{
              this.$router.push({ name: 'home'})
            })
            .catch(()=>{
              // console.log(err)
              this.$router.push({ name: 'LogIn'})
            })
            
          })
          .catch(() =>{
            // console.log(err);
            alert('아이디와 비밀번호를 확인해주세요')
          })
        },
      // changeLoginState(){
      //   // if()
      //   this.$store.dispatch('changeLoginState','login')
      // }
    
    },
}
</script>

<style>

.outer {
  display: flex
}

.inner {
  margin-right: 10vh;
  margin-left: 10vh;
}
</style>