<template>
    <div id="header" class="container" style="background:#66CDAA;color:#fff">
        <span><h2>科技专家资源共享平台</h2></span>
        <div id="card" class="container" >
          <el-card class="box-card" >


            <el-form :model="ruleForm2" status-icon :rules="rules2" ref="ruleForm2" class="demo-ruleForm">
              <el-form-item>
                <span>用户名：</span>
                <el-input v-model="user.username" style="float:right;margin-right:80px;width:160px" placeholder="请输入用户名"></el-input>
              </el-form-item>
              <el-form-item>
                <span>密码：</span>
                <el-input v-model="user.password" style="float:right;margin-right:80px;width:160px" placeholder="请输入密码" show-password="false"></el-input>
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
  import Axios from 'axios'
export default {
    data() {
      return {
        user:{
          username:'',
          password:'',
        }

      }
    },
    methods :{
      signIn:function() {
        if (!this.user.username) {
          this.$message.error('请输入用户名');
          return;
        }
        if (!this.user.password) {
          this.$message.error('请输入密码');
          return;
        }
        let _this = this;
        var login_form = new FormData();
        login_form.append('username', this.user.username);
        login_form.append('password', this.user.password);
        let config = {
          headers: {
            'Content-Type': 'multipart/form-data'
          }
        };
        Axios.post(
          _this.$url + 'user_login/', login_form, config
      ).then(function (response) {
          console.log('get response');
          switch (response.data.message){
            case '登录成功':
              _this.$message.success('登录成功，即将跳转到登录前页面');
              setTimeout(function () {
                  _this.$router.push({path:'../paperview/'});
              }, 2500);
              break;
            case '该用户还未通过邮件确认':
              _this.$message.error('该用户未通过邮箱验证，不可登录');
              break;
            // case '密码不正确':
            //   _this.$message.error('密码不正确');
            //   break;
            // case '用户不存在':
            //   _this.$message.error('用户不存在');
            //   break;
            default:
              _this.$message.error('用户名或密码错误');
          }
          // _this.$router.push({path:'paperview/'});
          console.log(response)
        }).catch(function (response) {
          console.log('gg');
          console.log(response)
        })

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

