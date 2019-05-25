<template>
    <div id="mostheader" class="container" style="background:#66CDAA;color:#fff;">
        <div style="vertical-align: middle;width:100%">
            <el-row style="width:100%;">
                <el-col :span="20">
                    <div class="text" style="text-align:left;margin-left:20px;">
                        <span><h2>科技专家资源共享平台</h2></span>
                    </div>
                </el-col>
                <el-col :span="2">
                    <el-button style="floating:right;margin-top:15px" @click="gotologin" class="btn btn-success">登录</el-button>
                </el-col>
                <el-col :span="2">
                    <el-button style="floating:right;margin-top:15px">注销</el-button>
                </el-col>
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
        
      }
    },
    methods: {
      gotologin() {
        this.$router.replace('/Login')
      },
      
    }

}

</script>

<style scoped>


</style>
