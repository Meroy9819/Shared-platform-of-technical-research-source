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
                <el-input v-model="password1" type="password" style="float:right;margin-right:80px;width:160px" placeholder="请输入密码"></el-input>
              </el-form-item>
              <el-form-item>
                <span>重复密码：</span>
                <el-input v-model="password2" type="password" style="float:right;margin-right:80px;width:160px" placeholder="请重复密码"></el-input>
              </el-form-item>
              <el-form-item>
                <span>邮箱：</span>
                <el-input v-model="email" style="float:right;margin-right:80px;width:160px" placeholder="请输入邮箱"></el-input>
              </el-form-item>
              <el-form-item>
                <span>手机号：</span>
                <el-input v-model="phone" style="float:right;margin-right:80px;width:160px" placeholder="请输入手机号"></el-input>
              </el-form-item>
              <el-form-item>
                <span>性别：</span>
                <el-input v-model="gender" style="float:right;margin-right:80px;width:160px" placeholder="请输入性别"></el-input>
              </el-form-item>
              <el-form-item>
                 <el-button type="primary" round style="float:left;margin-left:60px;text-align:center" @click="signUp" class="btn btn-success">注册</el-button>
                <el-button type="primary" round style="float:right;margin-right:60px;text-align:center"
                @click="gotologin" class="btn btn-success">返回登录</el-button>
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
        password1:"",
        password2:"",
        phone:"",
        email:"",
        gender:"",
      }
    },
    methods: {
      gotologin() {
        this.$router.replace('/Login')
      },
      signUp() {
        if(this.validateUsername(this.username)&&this.validatePassword()&&this.validatePhone(this.phone)&&this.validateEmail(this.email))
        {
          alert("OK");
        }
        else {
          alert("NO");
        }
      },
      validateUsername(name) {
        var reg = new RegExp("^(?![0-9]+$)(?![a-zA-Z]+$)[0-9A-Za-z]{12,}$");
        if(!reg.test(name)){
          this.$alert('用户名应为数字字母组合且长度不能小于12', '', {
          confirmButtonText: '确定',
          callback: action => {
            this.$message({
              type: 'info',
              message: `action: ${ action }`
            });
          }
          });
          return false;
        }
        return true;
      },
      validatePassword() {
        if(this.password1.length==0) {
          this.$alert('密码不能为空', '', {
          confirmButtonText: '确定',
          callback: action => {
            this.$message({
              type: 'info',
              message: `action: ${ action }`
            });
          }
          });
          return false;
        }else if(this.password1!=this.password2)  {
          this.$alert('密码不一致', '', {
          confirmButtonText: '确定',
          callback: action => {
            this.$message({
              type: 'info',
              message: `action: ${ action }`
            });
          }
          });
          return false;
        }
        return true; 
      },
      validatePhone(phonenum) {
        var reg = new RegExp("[0-9\-]"); //正则表达式
        if(phonenum.length!=11||!reg.test(phonenum)) {
          this.$alert('手机号应为数字11位', '', {
          confirmButtonText: '确定',
          callback: action => {
            this.$message({
              type: 'info',
              message: `action: ${ action }`
            });
          }
          });
          return false;
        }
        return true;
      },
      validateEmail(emailaddr) {
        var regEmail= new RegExp("^[a-z0-9]+([._\\-]*[a-z0-9])*@([a-z0-9]+[-a-z0-9]*[a-z0-9]+.){1,63}[a-z0-9]+$"); //正则表达式
        if(!regEmail.test(emailaddr)) {
          this.$alert('邮箱应符合邮箱格式', '', {
          confirmButtonText: '确定',
          callback: action => {
            this.$message({
              type: 'info',
              message: `action: ${ action }`
            });
          }
          });
          return false;
        }
        return true;
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
    height:450px;
    margin:0 auto;
  }
</style>

