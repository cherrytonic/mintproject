<template>
  <div>
  <h1>❓404 Not Found...❓</h1>
  <button class="btn" style="color: #a0e7ca; background-color: white;" @click="toHome">Home</button>
  </div>
</template>

<script>
export default {
    name:'Not_Found_404',
    methods:{
      toHome(){
        this.$router.push({name:'home'})
      }
    }

}
</script>

<style>

</style>