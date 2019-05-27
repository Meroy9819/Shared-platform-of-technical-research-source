<template>
    <div id="header" class="container" style="background:#66CDAA;color:#fff">
        <span><h2>科技专家资源共享平台</h2></span>
        <div id="card" class="container" >
          <el-card class="box-card" >


            <el-form :model="ruleForm2" status-icon :rules="rules2" ref="ruleForm2" class="demo-ruleForm">
              <el-form-item>
                <span>用户名：</span>
                <el-input v-model="username" style="float:right;margin-right:80px;width:160px" placeholder="请输入用户名"></el-input>
              </el-form-item>
              <el-form-item>
                <span>密码：</span>
                <el-input v-model="password" style="float:right;margin-right:80px;width:160px" placeholder="请输入密码"></el-input>
              </el-form-item>
              <el-form-item>
                <el-button type="primary" round style="float:left;margin-left:60px;text-align:center" @click="signIn">登录</el-button>
                <el-button type="primary" round style="float:right;margin-right:80px;text-align:center"
                @click="gotoregister" class="btn btn-success">注册</el-button>
              </el-form-item>
            </el-form>



          </el-card>
        </div>

    </div>
</template>

<script>

export default {
    components:{},
    data() {
      return {
        username:"",
        password:""
      }
    },
    methods: {
      gotoregister() {
        this.$router.replace('/Register')
      },
      signIn:function() {
        if(this.username.length==0||this.password.length==0) {
          //alert("null");
          
          this.$alert('字段不能为空', '', {
          confirmButtonText: '确定',
          callback: action => {
            this.$message({
              type: 'info',
              message: `action: ${ action }`
            });
          }
          });
          
        }
        return;
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

