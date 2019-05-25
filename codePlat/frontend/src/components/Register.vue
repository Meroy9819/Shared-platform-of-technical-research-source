<template>
    <div id="header" class="container" style="background:#66CDAA;color:#fff">
        <span><h2>科技专家资源共享平台</h2></span>
        <div id="card" class="container" >
          <el-card class="box-card" >
            <div class="text item">
              <div>
                <span>用户名：</span>
                <el-input v-model="input" style="float:right;margin-right:80px;width:160px" placeholder="请输入用户名"></el-input>
              </div>
              <div>
                <span>密码：</span>
                <el-input v-model="input" style="float:right;margin-right:80px;width:160px" placeholder="请输入密码"></el-input>
              </div>
              <div>
                <span>邮箱：</span>
                <el-input v-model="input" style="float:right;margin-right:80px;width:160px" placeholder="请输入邮箱"></el-input>
              </div>
              <div>
                <span>手机号：</span>
                <el-input v-model="input" style="float:right;margin-right:80px;width:160px" placeholder="请输入手机号"></el-input>
              </div>
            </div>
            <div>
              <el-button type="primary" round style="text-align:center">注册</el-button>
            </div>
          </el-card>
        </div>
    </div>
</template>

<script>
export default {
    data() {
      return {

      }
    }
}
</script>

<style scoped>
#header {
    margin-top:0px;
    height: 60px;
    text-align: center;
    vertical-align: middle;
    line-height: 60px;
}
.box-card {
    width: 480px;
    height:200px;
    margin:0 auto;
  }
</style>
