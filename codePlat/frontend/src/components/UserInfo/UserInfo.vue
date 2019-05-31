<template>
    <div>
        <Header></Header>


        <div style="margin-top:35px;width:80%;height:240px;margin:0 auto">
            <el-col :span="7">
                    <div style="margin-top:10px">
                        <img src="../../assets/头像.png" width="70%" style="min-height:70%!important">
                    </div>
            </el-col>
            <el-col :span="11" style="margin-top:17px">
                <div>
                    <h2>用户名{{username}}</h2><br>
                </div>
                <div>
                    <h4>用户身份{{status}}</h4>
                </div>
            </el-col>
            <el-col :span="6" style="margin-top:30px">
                <div style="margin-top:30px">
                    <!-- <el-button @click="editinfo" style="display:block;margin:0 auto">修改个人信息</el-button><br> -->


                    <el-button v-if="!isexpert" @click="certificate = true" style="display:block;margin:0 auto" class="btn btn-success">申请认证专家</el-button><br>

                    <div class="modal" v-bind:class="{'is-active':certificate}" >
                        <el-dialog title="认证专家信息" :visible.sync="certificate">
                            <el-form :model="form" >
                                <el-form-item>
                                    <span>真实姓名：</span>
                                    <el-input v-model="realname" style="float:right;margin-right:50px;width:230px" placeholder="请输入真实姓名"></el-input>
                                </el-form-item>
                                <el-form-item>
                                    <span>所属机构：</span>
                                    <el-input v-model="institution" style="float:right;margin-right:50px;width:230px" placeholder="请输入所属机构"></el-input>
                                </el-form-item>

                                <el-form-item v-for="(au, index) in form.paperlist"
                                    :label="'署名成果及出版年份' + (index+1) + ':'"  :key="au.key"
                                    :prop="'paperlist.' + index + '.papernamewithyear'" :label-width="formLabelWidth">
                                        <el-col :span="12" :offset="1">
                                            <el-input v-model="au.papernamewithyear" style="float:right;margin-right:50px;width:230px" placeholder="请输入成果及年份"></el-input>
                                        </el-col>
                                        <el-col :span="1" :offset="0">
                                            <el-button @click.prevent="removepaper(au)">删除</el-button>
                                        </el-col>
                                </el-form-item>
                                <el-form-item :label-width="formLabelWidth">
                                    <el-button @click="addpaper" style="width:100px">添加成果</el-button><br>
                                </el-form-item>

                                <!-- <el-form-item>
                                    <span>署名成果及出版年份：</span>
                                    <el-input v-model="papertitle" style="float:right;margin-right:80px;width:160px" placeholder="请输入已出版署名成果名称"></el-input>
                                </el-form-item> -->

                                <el-form-item>
                                    <span>所属研究领域：</span>
                                    <el-input v-model="area" style="float:right;margin-right:50px;width:230px" placeholder="请输入所属研究领域"></el-input>
                                </el-form-item>
                                <el-form-item>
                                    <span>上传正面手持身份证图像：</span>
                                </el-form-item>
                                <el-form-item>
                                    <el-upload class="upload-demo" drag action="https://jsonplaceholder.typicode.com/posts/" multiple>
                                        <i class="el-icon-upload"></i>
                                        <div class="el-upload__text">将文件拖到此处，或<em>点击上传</em></div>
                                        <div class="el-upload__tip" slot="tip">只能上传jpg/png文件，且不超过500kb</div>
                                    </el-upload>
                                </el-form-item>
                                <el-form-item>
                                    <el-button type="primary" round style="float:left;margin-left:130px;text-align:center" @click="submitcertificate">提交</el-button>
                                    <el-button type="primary" round style="float:right;margin-right:80px;text-align:center" @click="certificate = false">取消</el-button>
                                </el-form-item>
                                </el-form>
                        </el-dialog>
                    </div>

                    <el-button v-if="isexpert" @click="manageexpert" style="display:block;margin:0 auto" class="btn btn-success">管理专家页面</el-button><br>


                </div>
            </el-col>
        </div>



        <div style="margin-top:45px;width:75%;margin:0 auto">
            <el-tabs type="border-card" >
                <el-tab-pane label="个人信息">
                    <div style="width:90%;margin:0 auto">
                        <h4>ID：{{userID}}</h4>
                        <h4>性别：{{sex}}</h4>
                        <h4>邮箱：{{email}}</h4>
                        <h4>个人简介：{{introduction}}</h4>
                    </div>
                </el-tab-pane>

                <el-tab-pane label="新信息">
                    <div style="width:90%;margin:0 auto">
                        <el-tabs :tab-position="left" >
                            <el-tab-pane label="系统通知">
                                <div>
                                    <SystemMess></SystemMess><br>
                                    <SystemMess></SystemMess>
                                </div>
                                <div>
                                    <div class="block">
                                    <el-pagination
                                        layout="prev, pager, next"
                                        :total="20">
                                    </el-pagination>
                                    </div>
                                </div>
                            </el-tab-pane>
                            <el-tab-pane label="收藏信息">
                                <div>
                                    <collmess></collmess>
                                    <collmess></collmess>
                                </div>
                            </el-tab-pane>
                        </el-tabs>
                    </div>
                </el-tab-pane>

                <el-tab-pane label="收藏列表">
                    <div style="width:90%;margin:0 auto">
                        <el-tabs :tab-position="left" >
                            <el-tab-pane label="论文">
                                <div>
                                    <collpaper></collpaper>
                                </div>
                            </el-tab-pane>
                            <el-tab-pane label="专家">
                                <div>
                                    <collexpert></collexpert>
                                    <collexpert></collexpert>
                                </div>
                            </el-tab-pane>
                        </el-tabs>
                    </div>
                </el-tab-pane>
                <el-tab-pane label="举报信息">
                    <div style="width:90%;margin:0 auto">
                        <el-collapse v-model="activeNames" @change="handleChange">
                            <report></report>
                            <report></report>
                            <report></report>
                            <report></report>
                        </el-collapse>

                    </div>
                </el-tab-pane>
                <el-tab-pane label="评论信息">
                    <div style="width:90%;margin:0 auto">
                        <el-collapse v-model="activeNames" @change="handleChange">
                            <comment></comment>
                            <comment></comment>
                            <comment></comment>
                        </el-collapse>
                    </div>
                </el-tab-pane>
                <el-tab-pane label="访问记录">
                    <div style="width:90%;margin:0 auto">

                        <el-collapse v-model="activeNames" @change="handleChange">
                            <browsinghis></browsinghis>
                            <browsinghis></browsinghis>
                            <browsinghis></browsinghis>
                            <browsinghis></browsinghis>
                        </el-collapse>

                    </div>
                </el-tab-pane>

                <el-tab-pane label="修改信息">
                    <div style="width:90%;margin:0 auto">
                        <el-tabs :tab-position="left" >
                            <el-tab-pane label="头像设置">
                                <div>
                                    <el-form :model="form" style="width:60%;text-align:left;margin-left:50px;margin-top:30px">
                                        <el-form-item>
                                            <span>上传自定义头像：</span>
                                        </el-form-item>
                                        <el-form-item>
                                            <el-upload class="upload-demo" drag action="https://jsonplaceholder.typicode.com/posts/" multiple>
                                                <i class="el-icon-upload"></i>
                                                <div class="el-upload__text">将文件拖到此处，或<em>点击上传</em></div>
                                                <div class="el-upload__tip" slot="tip">只能上传jpg/png文件，且不超过500kb</div>
                                            </el-upload>
                                        </el-form-item>
                                        <el-form-item>
                                            <el-button type="primary" round style="float:left;margin-left:110px;text-align:center" @click="submitchangeimg">提交</el-button>
                                        </el-form-item>
                                    </el-form>

                                </div>
                            </el-tab-pane>
                            <el-tab-pane label="密码设置">
                                <div>
                                    <el-form :model="form" style="width:60%;text-align:center;margin-top:30px">
                                      <el-form-item>
                                            <span>原密码：</span>
                                            <el-input v-model="oldpassword" type="password" style="float:right;margin-right:80px;width:200px" placeholder="请输入原密码"></el-input>
                                        </el-form-item>
                                      <el-form-item>
                                            <span>新密码：</span>
                                            <el-input v-model="newpassword1" type="password" style="float:right;margin-right:80px;width:200px" placeholder="请输入密码"></el-input>
                                        </el-form-item>
                                        <el-form-item>
                                            <span>重复密码：</span>
                                            <el-input v-model="newpassword2" type="password" style="float:right;margin-right:80px;width:200px" placeholder="请重复密码"></el-input>
                                        </el-form-item>
                                        <el-form-item>
                                            <el-button type="primary" round style="float:left;margin-left:160px;text-align:center" @click="submitchangepass">提交</el-button>
                                        </el-form-item>
                                    </el-form>
                                </div>
                            </el-tab-pane>
                            <el-tab-pane label="简介设置">
                                <div>
                                    <el-form :model="form" style="width:60%;text-align:center;margin-top:30px">
                                        <el-form-item>
                                            <span>新简介：</span>
                                            <el-input v-model="newbrief" type="textarea" :rows="5" style="float:right;margin-right:80px;width:200px" placeholder="请输入个人简介"></el-input>
                                        </el-form-item>
                                        <el-form-item>
                                            <el-button type="primary" round style="float:left;margin-left:160px;text-align:center" @click="submitchangebrief">提交</el-button>
                                        </el-form-item>
                                    </el-form>
                                </div>
                            </el-tab-pane>
                        </el-tabs>
                    </div>
                </el-tab-pane>

            </el-tabs>

        </div>
    </div>
</template>

<script>
import Header from '@/components/Header'
import SystemMess from './SystemMess.vue'
import Axios from 'axios'
import report from './report'
import comment from './comment'
import collexpert from './collexpert'
import collpaper from './collpaper'
import browsinghis from './borwsinghis'
import collmess from './collmess'
export default {
    components:{Header,SystemMess,report,comment,collexpert,collpaper,browsinghis,collmess},
    data() {
        return {

            username:"",
            status:"",
            isexpert:false,
            userID:"",
            sex:"",
            email:"",
            brief:"",
            certificate:false,

            oldpassword:"",
            newpassword1:"",
            newpassword2:"",
            newbrief:"",


            //表单字段
            form: {
                realname: '',
                institution:'',
                paperlist: [{
                    papernamewithyear: ''
                }],
                area:''
            }
        }
    },
    methods: {
      certificateChange(){
        this.certificate = ~this.certificate;
        this.$router.go(0);
      },
      addpaper() {
            this.form.paperlist.push({
            papernamewithyear: '',
            key: Date.now()
            });
        },
      removepaper(item) {
            var index = this.form.paperlist.indexOf(item)
            if (index !== -1) {
            this.form.paperlist.splice(index, 1)
            }
        },
      manageAchi() {
            //this.$router.replace('/ExpertInfo')
            this.$router.push({
                name:'ExpertInfo',
                params:{
                    username:this.username
                }
            })
        },

        init:function () {
          let _this = this;
          var username = "hhx2";
          // Axios.get(_this.$url + 'user_index/',{
          //   params:{
          //     username:username
          //   }
          // })
          this.$http.request({
          url:_this.$url + 'user_index/',
          method:'get',
          params: {username:username}
        })
            .then(function (response) {
             var data =  response.data.data[0];
             _this.username = data.name;
             // _this.status = data.user_type;
             switch(data.user_type){
               case 1:
                 _this.status = "普通用户";
                 _this.isexpert = false;
                 break;
               case 2:
                 _this.status = "专家用户";
                 _this.isexpert = true;
                 break;
               case 3:
                 _this.status = "管理员用户";
                 _this.isexpert = false;
             }
             _this.userID = data.id;
             // data.sex === "male" ? _this.sex = "男":"女";
              _this.sex = data.sex;
             _this.email = data.email;
             _this.introduction = data.introduction;
             _this.img_src = '../../assets/'+ data.img;//调用本地资源，待解决

          console.log(response)
        }).catch(function (response) {
          console.log('gg');
          console.log(response)
        })
        },
        submitcertificate() {
            this.certificate = false;
            alert('todo提交认证了');
        },
        submitchangepass() {

        },
        submitchangeemail() {
            alert('todo提交新邮箱了');
        },
        submitchangeimg() {
            alert('todo要同步头像了');
        }

    },
    mounted:function () {
      this.init()
    }

}



</script>


