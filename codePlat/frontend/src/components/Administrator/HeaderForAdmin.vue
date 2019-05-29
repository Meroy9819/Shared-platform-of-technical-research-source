<template>
    <div id="mostheader" class="container" style="background:#66CDAA;color:#fff;">
        <div style="vertical-align: middle;width:100%">
            <el-row style="width:100%;vertical-align: middle;">
                <el-menu  mode="horizontal"  style="background:#66CDAA;color:#fff;height:100%">
                    <el-col :span="2">
                        <div style="text-align:center;h eight:100%">
                            <router-link class="navbar-item" to="/">
                                <!-- <img src="../../assets/logo.png" width="60%" style="max-height:70%!important"> -->
                                <img src="../../assets/logo-1_W.png" width="120px" height="50px" style="margin-top:5px;vertical-align: middle;">
                            </router-link>
                        </div>
                    </el-col>
                    <el-col :span="20" ><div><h6></h6></div></el-col>
                    <el-col :span="2" style="margin-bottom:10px;floating:right;" >
                        <el-button v-if="!isLogined" style="floating:right;margin-top:10px" @click="gotologin" class="btn btn-success">登录</el-button>
                        <el-button v-if="isLogined" style="floating:right;margin-top:10px" class="btn btn-success">注销</el-button>
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
        isLogined:true
      }
    },
    methods: {
      gotologin() {
        this.$router.replace('/Login')
      }
      
    }

}

</script>

<style scoped>


</style>
