<template>
  <div>
    <h1>SignUp</h1>
    <br>
    <div class="out">
    <form @submit.prevent="signup" class="in">
      <div class="row g-3 align-items-center">
        <div class="col-auto">
          <label for="username">username : </label>
        </div>
      </div>
      <div id="usernamerow" class="row">
        <div class="col-11">
          <input class="form-control" type="text" id="username" v-model="username">
        </div>
        <div class="col-1">
          <button class="btn signup " @click.self.prevent="usernamecheckFunc">✔</button>
          <br>
        </div>
        <span v-if="usernamecheck">사용가능한 username입니다.</span>
      </div>
      <br>
      <div class="row g-3 align-items-center">
        <div class="col-auto">
          <label for="password1"> password : </label>
        </div>
      </div>
      <div class="row g-1 align-items-center">
        <div class="col">
          <input class="form-control" type="password" id="password1" v-model="password1"><br>
        </div>
      </div>

      <div class="row g-3 align-items-center">
        <div class="col-auto">
          <label for="password2">password confirm : </label>
        </div>
      </div>
      <div class="row g-3 align-items-center">
        <div class="col">
          <input class="form-control" type="password" id="password2"  v-model="password2"><br>
        </div>
      </div>
     
      <div class="row g-3 align-items-center">
        <div class="col-auto">
          <label for="nickname">nickname : </label>
        </div>
      </div>
        <div class="row g-3 align-items-center">
        <div class="col">
          <input class="form-control" type="text" id="nickname" v-model="nickname"><br>
        </div>
      </div>

      <div class="row g-3 align-items-center">
        <div class="col-auto">
          <label for="genre_preference">선호 장르 : </label>
        </div>
      </div>
      <div class="row g-3 align-items-center">
        <div class="col">
          <div type="button" id="genrebtn" class="btn btn-outline-light mx-1 my-1" v-for="genre in genre_list" :key="genre.id" @click="select_genre(genre)" :class={selected:genre.selected}>{{genre.name}}</div>
        </div>
      </div>
      <br>
      <button type="submit" class="btn" style="background-color: white; color: #a0e7ca;">SignUp</button>
      
      </form>
  
  </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'SingUp',
  data: function () {
    return {
      username : '',
      password1 : '',
      password2 : '',
      nickname : '',
      genre_preference : [],
      genre_list:[],
      usernamecheck:false
    }
  },
  methods: {
    signup: function () {
      if(!this.usernamecheck){
        alert('Username 검사를 먼저 진행해 주세요')
        return
      }
      const num = this.password1.search(/[0-9]/g)
      const eng = this.password1.search(/[a-z]/ig)

      if(this.password1.length<8) {
        alert('8자 이상으로 생성해주세요.')
        return
      } else if(this.password1.search(/\s/) != -1){
        alert("비밀번호는 공백 없이 입력해주세요.");
        return
      } else if(num < 0 || eng < 0){
        alert("영어 소문자 및 숫자를 혼합하여 입력해주세요.");
        return
      } else if (this.genre_preference.length < 3) {
        alert("선호 장르를 3개 이상 선택해주세요.");
        return 
      } else if(this.password1!=this.password2){
        alert("입력하신 비밀번호와 비밀번호 확인이 다릅니다.")
        return
      } else {
        alert("가입 성공! 환영합니다👋");
      }

      const payload = {
        username:this.username,
        password1:this.password1,
        password2:this.password2,
        nickname:this.nickname,
        genre_preference:JSON.stringify(this.genre_preference),
      }

      axios({
        method:'post',
        url:'http://127.0.0.1:8000/accounts/signup/',
        data:payload
      })
      .then(()=>{
        // console.log(res);
        this.$router.push({name:'LogIn'})
      })
      .catch(err=>{
        console.log(err);
      })
    },
    select_genre(genre){
      genre.selected=!genre.selected
      if(this.genre_preference.includes(genre.id)){
        this.genre_preference.pop(genre.id)
      } else{
        this.genre_preference.push(genre.id)
      }
      // console.log(this.genre_preference);
    },
    usernamecheckFunc(){
      if(this.username.length<5){
        alert('username은 5자 이상이어야 합니다.')
        return
      }

      axios.get('http://127.0.0.1:8000/accounts/user/all/')
      .then(res=>{
        console.log(res.data);
        const usernames=res.data.map(res=>{
          return res.username
        })
        if(usernames.includes(this.username)){
          this.usernamecheck=false
          alert('중복된 username입니다.')
          return
        }
        else{
          this.usernamecheck=true
        }
      })
    }
  },
  created(){
    axios({
      method:'get',
      url:'http://127.0.0.1:8000/movies/genres/'
    })
    .then(res=>{
      const genres=res.data.map(genre=>{
        genre['selected']=false
        return genre
      })
      // console.log(genres);
      this.genre_list=genres
    })
  }
}
</script>

<style scoped>
.out {
  display: flex;
  justify-content: center;
}

#usernamerow {
  display: flex;
  justify-content: space-between;

}
.in {
  margin-right: 10vh;
  margin-left: 10vh;
}

.selected{
  background-color: white; 
  color: #a0e7ca;
}

#genrebtn:hover {
  background-color: white !important;
  color: #a0e7ca !important;
}


.signup {
  color: #a0e7ca;
  background-color: white;
}
</style>
