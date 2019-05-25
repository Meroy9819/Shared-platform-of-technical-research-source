<template>
  <div id="app" style="position:absolute;height:100%;width:100%;overflow-y: scroll">
    <router-view/>
  </div>
</template>

<script>
import Login from '@/components/Login'
import Register from '@/components/Register'
import Paperview from '@/components/Paperview'
import Header from '@/components/Header'
import SearchResult from '@/components/SearchResult'
import indexx from '@/components/indexx'

export default {
  name: 'App',
  components:{
    Login,
    Register,
    Paperview,
    Header,
    SearchResult,
    indexx
  }
}
</script>

<style>
#app {
  margin-top: 0%;
}
</style>
