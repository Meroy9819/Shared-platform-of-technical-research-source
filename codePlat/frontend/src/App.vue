<template>
  <div id="app" v-if="isRouterAlive" style="position:absolute;height:100%;width:100%;overflow-y: scroll">
    <router-view/>
  </div>
</template>

<script>
import Paperview from '@/components/Paperview'
import Header from '@/components/Header'
import SearchResult from '@/components/SearchResult'
import indexx from '@/components/indexx'
// import test from '@/components/test'

export default {
  name: 'App',
  components:{
    Paperview,
    Header,
    SearchResult,
    indexx,
    //test
  },
  provide(){
    return {
      reload: this.reload
    }
  },
  data(){
    return{
      isRouterAlive : true
    }
  },
  methods:{
    reload(){
      this.isRouterAlive=false;
      this.$nextTick(function () {
        this.isRouterAlive =true
      })
    }
  }
}
</script>

<style>
#app {
  margin-top: 0%;
}
</style>
