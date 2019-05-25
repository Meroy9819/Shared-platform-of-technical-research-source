<template>
    <div id="paper">
    <table  >

        <tr class="header">

        </tr>

        <tr v-for="item in paperList" :key="item"  >
           <!--td><input type="checkbox"  :value="item.serviceId" /></td-->
            <td>{{item.name}}</td>
          <td>a</td>

             <!--a href="#" v-on:click="updateu(item)">更新</a-->

        </tr>
    </table>

 </div>
</template>
<div>{{data}}</div>
<script>
    export default {
      data(){
          return{
            paperList:[],
          }
      },
      methods:{
        init:function(){
        let _this = this;
        this.$http.request({
          url:_this.$url + 'paperview',
          method:'get',
        }).then(function (response) {
          _this.sciachi = response.data;
          console.log('heihei');
          console.log(response)
        }).catch(function (response) {
          console.log('gg');
          console.log(response)
        })
      }
      },
      mounted:function () {
      this.init()
    }
    }
</script>

<style scoped>

</style>
