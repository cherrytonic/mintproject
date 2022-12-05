<template>
  <div></div>
</template>

<script>
export default {
    name:'LogOut',
    data(){
        return{
            is_logined:this.$route.params.is_logined
        }
    },
    computed:{
        checkLogin(){
            return this.$store.getters.checkLogin
        }
    },
    methods:{
        logout(){
            if(this.checkLogin){
                window.localStorage.removeItem('jwt')
                window.localStorage.removeItem('username')
                window.localStorage.removeItem('userdata')
                this.$store.dispatch('changeLoginState','logout')
                this.$emit('logout')
                this.$router.go()
                // this.$router.push({name:'home'})
            } else {
                this.$router.push({name:'home'})
            }
        }
    },
    created(){
        this.logout()
    }

}
</script>

<style>

</style>