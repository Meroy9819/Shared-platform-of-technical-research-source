<template>
    <div id="header" class="container" style="background:#66CDAA;color:#fff">
        <!-- <span><h2>科技专家资源共享平台</h2></span> -->

        <router-link class="navbar-item" to="/">
            <!-- <img src="../../assets/logo.png" width="60%" style="max-height:70%!important"> -->
            <img src="../../assets/logo-1_W.png" width="120px" height="50px" style="margin-top:5px;vertical-align: middle;">
        </router-link>

        <div id="card" class="container" >
          <el-card class="box-card" >

            <el-form :model="RegisterForm" status-icon :rules="rules" ref="RegisterForm" class="demo-ruleForm">
              <el-form-item prop="username">
                <span>用户名：</span>
                <el-input v-model="RegisterForm.username" style="float:right;width:350px" placeholder="请输入用户名"></el-input>
              </el-form-item>
              <el-form-item  prop="password1">
                <span>密码：</span>
                <el-input v-model="RegisterForm.password1" type="password" style="float:right;width:350px" placeholder="请输入密码"></el-input>
              </el-form-item>
              <el-form-item prop="password2">
                <span>重复密码：</span>
                <el-input v-model="RegisterForm.password2" type="password" style="float:right;width:350px" placeholder="请确认密码"></el-input>
              </el-form-item>
              <el-form-item prop="email">
                <span>邮箱：</span>
                <el-input v-model="RegisterForm.email" style="float:right;width:350px" placeholder="请输入邮箱"></el-input>
              </el-form-item>
              <el-form-item prop="phone">
                <span>手机号：</span>
                <el-input v-model="RegisterForm.phone" style="float:right;width:350px" placeholder="请输入手机号"></el-input>
              </el-form-item>
              <el-form-item >
                <span>性别：</span>

                  <el-radio-group v-model="RegisterForm.sex" style="float:right;width:350px;margin-top: 12px;align-content: center">
                    <el-radio :label="0">男</el-radio>
                    <el-radio :label="1">女</el-radio>
                  </el-radio-group>

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

import Axios from 'axios'
export default {
    components:{},

    data() {
      var validateUsername = (rule, value, callback) => {
        if (value === '') {
          callback(new Error('请输入用户名'));
        }  else {
          callback();
        }
      };
      var validatePass1 = (rule, value, callback) => {
        if (value === '') {
          callback(new Error('请输入密码'));
        }  else {
          callback();
        }
      };
        var validatePass = (rule, value, callback) => {
        if (value === '') {
          callback(new Error('请再次输入密码'));
        } else if (value !== this.RegisterForm.password1) {
          callback(new Error('两次输入密码不一致!'));
        } else {
          callback();
        }
      };
        var validatePhone = (rule, value, callback) => {
        var reg = new RegExp("[0-9\-]"); //正则表达式
        if (value === '') {
          callback(new Error('手机号不能为空!'));
        } else if (value.length!==11||!reg.test(value)) {
          callback(new Error('请填写正确的手机号!'));
        } else {
          callback();
        }
      };
        var validateEmail = (rule, value, callback) =>{
          var regEmail= new RegExp("^[a-z0-9]+([._\\-]*[a-z0-9])*@([a-z0-9]+[-a-z0-9]*[a-z0-9]+.){1,63}[a-z0-9]+$"); //正则表达式
        if (value === '') {
          callback(new Error('请输入邮箱!'));
        }else if(!regEmail.test(value)) {
          callback(new Error('请输入正确的邮箱地址!'));
        }
        else callback();
        };
      return {
        RegisterForm:{
          username:"",
          password1:"",
          password2:"",
          phone:"",
          email:"",
          sex: 0,
        },
        // user: {
        //
        // },
        rules:{
          username:[{
            validator: validateUsername,
            trigger:'blur'
          }],
          password1:[{
            validator: validatePass1,
            trigger:'blur'
          }],
          password2:[{
            validator: validatePass,
            trigger:'blur'
          }],
          email:[{
            validator: validateEmail,
            trigger:'blur'
          }],
          phone:[{
            validator:validatePhone,
            trigger:'blur'
          }]
        },
      }
    },
    methods: {
      gotologin() {
        this.$router.replace('/Login')
      },
      signUp() {
        console.log(this.RegisterForm.sex);
        var count = 0;
        // if(this.validatePassword(this.user.password1, this.user.password2)) count++;
        // if(this.validatePhone(this.user.phone)) count++;
        // if(this.validateEmail(this.user.email)) count++;
        if(this.validatePassword(this.RegisterForm.password1, this.RegisterForm.password2) && this.validatePhone(this.RegisterForm.phone) && this.validateEmail(this.RegisterForm.email))
        {count = 1}
        else this.$message.error('请检查输入的内容');
        if(count === 1)
        {//已经输入了全部所需信息
          let _this = this;
          var register_form = new FormData();
          register_form.append('username', this.RegisterForm.username);
          register_form.append('password1', this.RegisterForm.password1);
          register_form.append('password2', this.RegisterForm.password2);
          register_form.append('email', this.RegisterForm.email);
          if(this.RegisterForm.sex === 0) register_form.append('sex', '男');
          else register_form.append('sex', '女');
          register_form.append('phonenumber', this.RegisterForm.phone);
          let config = {
            headers: {
              'Content-Type': 'multipart/form-data'
            }
          };
          Axios.post(
          _this.$url + 'user_register/', register_form, config
          ).then(function (response) {
            console.log('get response');
            switch (response.data.message){
              case '请先登出':
                _this.$message.error('请注销后再进行注册');
                break;
              case '请前往注册邮箱，进行邮件确认':
                _this.$message.success('注册成功，请前往邮箱确认');
                setTimeout(function () {
                    _this.$router.push({path:'../'});
                    _this.$router.go(0);
                }, 2500);
                break;
              case '两次输入的密码不同':
                _this.$message.error('两次输入的密码不同');
                break;
              case '用户已经存在，请重新选择用户名':
                _this.$message.error('用户名已被占用，请前往登录或重新选择用户名');
                break;
              case '该邮箱地址已被注册，请使用别的邮箱':
                _this.$message.error('该邮箱地址已被注册，请更换邮箱注册');
                break;
              default:
                _this.$message.error('请检查输入的信息是否完整');
            }
          // _this.$router.push({path:'paperview/'});
            console.log(response)
          }).catch(function (response) {
            console.log('gg');
            console.log(response)
          })
        }
      },
      validatePassword(password1, password2) {
        console.log(password1 + password2);
        if(password1.length==0) {
          // this.$message.error('密码不能为空');
          return false;
        }
        else if(password1!=password2)  {
          // this.$message.error('两次输入的密码不一致');
          return false;
        }
        return true;
      },
      validatePhone(phonenum) {
        var reg = new RegExp("[0-9\-]"); //正则表达式
        if(phonenum.length!=11||!reg.test(phonenum)) {
          // this.$message.error('请填写正确的手机号');
          return false;
        }
        return true;
      },
      validateEmail(emailaddr) {
        var regEmail= new RegExp("^[a-z0-9]+([._\\-]*[a-z0-9])*@([a-z0-9]+[-a-z0-9]*[a-z0-9]+.){1,63}[a-z0-9]+$"); //正则表达式
        if(!regEmail.test(emailaddr)) {
          this.$message.error('请填写正确的邮箱地址');
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
    vertical-align: middle;
    line-height: 60px;
}
.box-card {
    width: 480px;
    height:auto;
    margin:0 auto;
    text-align: center;
    margin-top:10px;
  }
</style>

