<template>
    <div id="mostheader" class="container" style="background:#66CDAA;color:#fff;margin-top:0px">
        <div style="vertical-align: middle;width:100%">
            <el-row style="width:100%;vertical-align: middle;">
                <el-menu  mode="horizontal"  style="background:#66CDAA;color:#fff;height:100%">
                 <el-col :span="2">
                        <div style="text-align:center;height:100%;vertical-align: middle;">
                            <router-link class="navbar-item" to="/">
                                <img src="../assets/logo-1_W.png" width="120px" height="50px" style="margin-top:5px;vertical-align: middle;">
                            </router-link>
                        </div>
                    </el-col>
                <el-col :span="18" v-if="!searchVisible"><div><h6></h6></div></el-col>
                <el-col :span="18" v-if="searchVisible">
                    <!-- <el-row style="height:1px"><el-col :span="24"><div class="grid-content" ></div></el-col></el-row> -->
                    <el-row :gutter="20" style="height:50px;vertical-align: middle;margin-top:10px">
                        <el-col :span="10" :offset="5" >
                            <el-input placeholder="请输入检索内容" prefix-icon="el-icon-search" v-model="input2"></el-input>
                        </el-col>
                        <el-col :span="1">
                            <el-button type="primary" @click="search" icon="el-icon-search"></el-button>
                        </el-col>
                        <el-col :span="2" :offset="1">
                            <el-button disabled type="primary" @click="advsearch" icon="el-icon-s-fold">高级检索</el-button>
                        </el-col>
                    </el-row>
                </el-col>

                <el-col :span="2">
                        <div style="text-align:center;margin-top:2px" v-if="isLogined">
                            <el-submenu>
                                <template slot="title">
                                    <img src="../assets/timg.jpg" width="60%" style="max-height:70%!important;border-radius:50%">
                                </template>
                                    <el-menu-item>
                                        <router-link v-if="!idenisadmin" to="/UserInfo" style="color:black;text-decoration:none;">个人主页</router-link>
                                        <!-- 如果是管理员的话，Administrator是他的个人主页 -->
                                        <router-link v-if="idenisadmin" to="/Administrator" style="color:black;text-decoration:none;">个人主页</router-link>
                                    </el-menu-item>
                            </el-submenu>
                        </div>
                        <div style="text-align:center;margin-top:2px" v-if="!isLogined">
                            <p></p>
                        </div>
                    </el-col>
                    <el-col :span="2" style="margin-bottom:10px;floating:right;" >
                        <el-button v-if="!isLogined" style="floating:right;margin-top:10px" @click="gotologin" class="btn btn-success">登录</el-button>
                        <el-button v-if="isLogined" style="floating:right;margin-top:10px" @click="logout">注销</el-button>
                    </el-col>
                </el-menu>
            </el-row>
        </div>
        <div>

        </div>
    </div>
</template>

<script>

export default {
    data() {
      return {
        isLogined:true,
        searchVisible:true,
        // name:'我是子组件里面的数据',
        input2:'',
        idenisadmin:false
      }
    },
    methods: {
      gotologin() {
        this.$router.replace('/Login')
      },
      
      //检索
      search() {
        console.log("检索:"+this.input2);
        this.$router.push({
                name:'SearchResult',
                params:{
                    word:this.input2
                }
            })
      },
      //高级检索（待定）
      advsearch() {
        console.log("高级检索:"+this.input2);
      },
      logout() {
          this.isLogined = false;
          alert('退出登录啦');
      }

      
    }

}

</script>

<style scoped>
.grid-content {
    min-height: 16px;
  }


</style>
