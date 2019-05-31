<template>
    <div>

        <!-- <HeaderNoLogin></HeaderNoLogin> -->
        <HeaderForAdmin></HeaderForAdmin>
        
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
                    <el-button @click="release = true" style="display:block;margin:0 auto" class="btn btn-success">发布通知</el-button><br>
                
                    <div class="modal" v-bind:class="{'is-active':release}">
                        <el-dialog title="发布通知" :visible.sync="release">
                            <el-form >
                                <el-form-item label="通知内容" :label-width="formLabelWidth">
                                <el-input type="textarea" :rows="3" v-model="reason" placeholder="请输入通知内容" autocomplete="off" clearable></el-input>
                                </el-form-item>
                            </el-form>
                            <div slot="footer" class="dialog-footer">
                                <el-button @click="release = false">取 消</el-button>
                                <el-button type="primary" @click="releaseinfo">确 定</el-button>
                            </div>
                        </el-dialog>
                    </div>

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
                                    <el-collapse v-model="activeNames1" @change="handleChange">
                                        <ApplyInfo></ApplyInfo>
                                        <ApplyInfo></ApplyInfo>
                                    </el-collapse>
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
                                    
                                    <el-tabs :tab-position="left" >
                                        <el-tab-pane label="论文">
                                            <!-- 成果页添加仅管理员可见的编辑按钮 -->
                                            <el-collapse v-model="activeNames2" @change="handleChange">
                                                <ReportInfo></ReportInfo>
                                                <ReportInfo></ReportInfo>
                                                <ReportInfo></ReportInfo>
                                            </el-collapse>
                                        </el-tab-pane>
                                        <el-tab-pane label="专家">
                                            <!-- 给专家发系统通知 -->
                                            <el-collapse v-model="activeNames3" @change="handleChange">
                                                <ReportInfo></ReportInfo>
                                            </el-collapse>
                                        </el-tab-pane>
                                        <el-tab-pane label="评论">
                                            <!-- 删除评论 -->
                                            <el-collapse v-model="activeNames4" @change="handleChange">
                                                <ReportInfo></ReportInfo>
                                                <ReportInfo></ReportInfo>
                                            </el-collapse>
                                        </el-tab-pane>
                                    </el-tabs>

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

                <el-tab-pane label="已处理信息">
                    <div style="width:90%;margin:0 auto">
                        <el-collapse v-model="activeNames5" @change="handleChange">
                            <ReadyHandle></ReadyHandle>
                            <ReadyHandle></ReadyHandle>
                        </el-collapse>
                    </div>
                </el-tab-pane>
                




                
                
            </el-tabs>

        </div>


    </div>
</template>

<script>
import HeaderForAdmin from './HeaderForAdmin'
import ReportInfo from './ReportInfo'
import ApplyInfo from './ApplyInfo'
import ReadyHandle from './ReadyHandle'

export default {
    components:{HeaderForAdmin,ReportInfo,ApplyInfo,ReadyHandle},
    data() {
        return {
            adminID:"",
            release:false,

        }
    },
    methods: {
        releaseinfo() {
            
            this.release = false;
            alert('releaseinformation');
        }
    }

}
</script>
