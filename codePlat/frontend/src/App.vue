<template>
  <div id="app" style="position:absolute;height:100%;width:100%;overflow-y: scroll">
    <router-view/>
  </div>
</template>

<script>
import Paperview from '@/components/Paperview'
import Header from '@/components/Header'
import SearchResult from '@/components/SearchResult'
import indexx from '@/components/indexx'
import test from '@/components/test'

export default {
  name: 'App',
  components:{
    Paperview,
    Header,
    SearchResult,
    indexx,
    test
  }
}
</script>

<style>
#app {
  margin-top: 0%;
}
</style>
