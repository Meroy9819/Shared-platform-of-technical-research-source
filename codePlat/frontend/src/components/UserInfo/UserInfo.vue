<template>
    <div>
        <HeaderNoLogin></HeaderNoLogin>


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
                <div style="margin-top:40px">
                    <el-button v-if="!isexpert" @click="renzheng" style="display:block;margin:0 auto" class="btn btn-success">申请认证专家</el-button><br>
                    
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
                <el-tab-pane label="站内信">
                    <div style="width:90%;margin:0 auto">
                        暂无
                    </div>
                </el-tab-pane>
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




                
                
            </el-tabs>

        </div>

       



    </div>
</template>

<script>
import HeaderNoLogin from './HeaderNoLogin.vue'
import SystemMess from './SystemMess.vue'

export default {
    components:{HeaderNoLogin,SystemMess},
    data() {
        return {
            username:"",
            status:"",
            isexpert:true,
            userID:"",
            gender:"",
            email:""
        }
    },
    methods: {
        renzheng() {
            this.$router.replace('/Certificate')
        },
        manageexpert() {
            
            this.$router.replace('/ExpertInfo')
            
        }
    }

}



</script>


