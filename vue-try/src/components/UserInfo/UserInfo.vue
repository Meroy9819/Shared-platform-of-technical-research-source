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


                    <el-button v-if="!isexpert" @click="renzheng = true" style="display:block;margin:0 auto" class="btn btn-success">申请认证专家</el-button><br>
                    
                    <div class="modal" v-bind:class="{'is-active':renzheng}" >
                        <el-dialog title="认证专家信息" :visible.sync="renzheng">
                            <el-form :model="form" style="text-align:center">
                                <el-form-item>
                                    <span>真实姓名：</span>
                                    <el-input v-model="realname" style="float:right;margin-right:80px;width:160px" placeholder="请输入真实姓名"></el-input>
                                </el-form-item>
                                <el-form-item>
                                    <span>所属机构：</span>
                                    <el-input v-model="institution" style="float:right;margin-right:80px;width:160px" placeholder="请输入所属机构"></el-input>
                                </el-form-item>
                                <el-form-item>
                                    <span>署名成果名称：</span>
                                    <el-input v-model="papertitle" style="float:right;margin-right:80px;width:160px" placeholder="请输入已出版署名成果名称"></el-input>
                                </el-form-item>
                                <el-form-item>
                                    <span>成果出版时间：</span>
                                    <el-input v-model="paperpublishedtime" style="float:right;margin-right:80px;width:160px" placeholder="请输入出版时间"></el-input>
                                </el-form-item>
                                <el-form-item>
                                    <span>所属研究领域：</span>
                                    <el-input v-model="area" style="float:right;margin-right:80px;width:160px" placeholder="请输入所属研究领域"></el-input>
                                </el-form-item>
                                <el-form-item>
                                    <el-button type="primary" round style="float:left;margin-left:130px;text-align:center" @click="submitrenzheng">提交</el-button>
                                    <el-button type="primary" round style="float:right;margin-right:80px;text-align:center" @click="renzheng = false">取消</el-button>
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
                        <h4>性别：{{gender}}</h4>
                        <h4>邮箱：{{email}}</h4>
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
                                    <!-- <patent></patent> -->
                                </div>
                                <div>
                                    <div class="block">
                                    <el-pagination
                                        layout="prev, pager, next"
                                        :total="40">
                                    </el-pagination>
                                    </div>
                                </div>
                            </el-tab-pane>
                        </el-tabs>
                    </div>
                </el-tab-pane>

                <el-tab-pane label="收藏列表">
                    <div style="width:90%;margin:0 auto">
                        暂无
                    </div>
                </el-tab-pane>
                <!-- <el-tab-pane label="站内信">
                    <div style="width:90%;margin:0 auto">
                        暂无
                    </div>
                </el-tab-pane> -->
                <el-tab-pane label="举报信息">
                    <div style="width:90%;margin:0 auto">
                        暂无
                    </div>
                </el-tab-pane>
                <el-tab-pane label="评论信息">
                    <div style="width:90%;margin:0 auto">
                        暂无
                    </div>
                </el-tab-pane>
                <el-tab-pane label="访问记录">
                    <div style="width:90%;margin:0 auto">
                        暂无
                    </div>
                </el-tab-pane>

                <el-tab-pane label="修改信息">
                    <div style="width:90%;margin:0 auto">
                        <el-tabs :tab-position="left" >
                            <el-tab-pane label="头像设置">
                                <div>
                                    <!-- 设置换头像 -->
                                    <!-- <div>
                                        <span>上传自定义头像</span>
                                    </div>
                                    <div>
                                        <el-upload class="upload-demo" drag action="https://jsonplaceholder.typicode.com/posts/" multiple>
                                            <i class="el-icon-upload"></i>
                                            <div class="el-upload__text">将文件拖到此处，或<em>点击上传</em></div>
                                            <div class="el-upload__tip" slot="tip">只能上传jpg/png文件，且不超过500kb</div>
                                        </el-upload>
                                    </div> -->

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
                            <el-tab-pane label="邮箱设置">
                                <div>
                                    <el-form :model="form" style="width:60%;text-align:center;margin-top:30px">
                                        <el-form-item>
                                            <span>新邮箱：</span>
                                            <el-input v-model="newemail" type="text" style="float:right;margin-right:80px;width:200px" placeholder="请输入新邮箱"></el-input>
                                        </el-form-item>
                                        <el-form-item>
                                            <el-button type="primary" round style="float:left;margin-left:160px;text-align:center" @click="submitchangeemail">提交</el-button>
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

export default {
    components:{Header,SystemMess},
    data() {
        return {
            username:"",
            status:"",
            isexpert:true,
            userID:"",
            gender:"",
            email:"",
            renzheng:false,


            // for renzheng
            realname:"",
            institution:"",
            papertitle:"",
            paperpublishedtime:"",
            area:"",

            //for change info
            newpassword1:"",
            newpassword2:"",
            newemail:""

        }
    },
    methods: {
        // renzheng() {
        //     this.$router.replace('/Certificate')
        // },
        manageexpert() {
            
            //this.$router.replace('/ExpertInfo')
            this.$router.push({
                name:'ExpertInfo',
                params:{
                    username:this.username
                }
            })
            
        },
        submitrenzheng() {
            this.renzheng = false;
            alert('todo提交认证了');
        },
        submitchangepass() {
            alert('todo提交新密码了');
        },
        submitchangeemail() {
            alert('todo提交新邮箱了');
        },
        submitchangeimg() {
            alert('todo要同步头像了');
        }
        
    }

}



</script>


