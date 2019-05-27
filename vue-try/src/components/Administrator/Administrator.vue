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
                    <h2>管理员ID{{adminID}}</h2><br>
                </div>
            </el-col>
            <el-col :span="6" style="margin-top:30px">
                <div style="margin-top:40px">
                    <el-button @click="release" style="display:block;margin:0 auto" class="btn btn-success">发布通知</el-button><br>
                </div>
            </el-col>
        </div>


        <div style="margin-top:45px;width:75%;margin:0 auto">
            <el-tabs type="border-card" >

                <el-tab-pane label="未处理消息">
                    <div style="width:90%;margin:0 auto">
                        <el-tabs :tab-position="left" >
                            <el-tab-pane label="申请信息">
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
                            <el-tab-pane label="举报信息">
                                <div>
                                    <patent></patent>
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

                <el-tab-pane label="已处理信息？？">
                    <div style="width:90%;margin:0 auto">
                        暂无
                    </div>
                </el-tab-pane>
                




                
                
            </el-tabs>

        </div>


    </div>
</template>

<script>
import HeaderNoLogin from '@/components/UserInfo/HeaderNoLogin'


export default {
    components:{HeaderNoLogin},
    data() {
        return {
            adminID:"",

        }
    },
    methods: {
        release() {
            alert("i dont know how to release a info")
        }
    }

}
</script>
