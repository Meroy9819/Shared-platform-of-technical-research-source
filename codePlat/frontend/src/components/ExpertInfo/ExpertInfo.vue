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
                    <h2>用户名{{username}}</h2>
                </div>
                <div>
                    <h4>所属科研机构{{institution}}</h4><br>
                </div>
                <div>
                    <h4>被引数：{{beiyinshu}}成果数：{{chengguoshu}}H指数：{{Hzhishu}}G指数：{{Gzhishu}}</h4>
                </div>
            </el-col>
            <el-col :span="6" style="margin-top:30px" v-if="isLogined">
                <div>
                    <el-button @click="guanzhu" style="display:block;margin:0 auto" class="btn btn-success">收藏</el-button><br>
                    <el-button @click="dialogFormVisible = true" style="display:block;margin:0 auto" class="btn btn-success">举报</el-button><br>

                    <div class="modal" v-bind:class="{'is-active':dialogFormVisible}">
                        <el-dialog title="举报信息" :visible.sync="dialogFormVisible">
                            <el-form >
                                <el-form-item label="举报理由" :label-width="formLabelWidth">
                                <el-input type="textarea" :rows="3" v-model="reason" placeholder="请输入举报理由" autocomplete="off" clearable></el-input>
                                </el-form-item>
                            </el-form>
                            <div slot="footer" class="dialog-footer">
                                <el-button @click="dialogFormVisible = false">取 消</el-button>
                                <el-button type="primary" @click="dialogFormVisible = false">确 定</el-button>
                            </div>
                        </el-dialog>
                    </div>


                    <el-button @click="sendmess = true" style="display:block;margin:0 auto" class="btn btn-success">站内信</el-button>

                    <div class="modal" v-bind:class="{'is-active':sendmess}">
                        <el-dialog title="站内信" :visible.sync="sendmess">
                            <el-form >
                                <el-form-item label="发送站内信" :label-width="formLabelWidth">
                                <el-input type="textarea" :rows="3" v-model="reason" placeholder="请编辑信件内容" autocomplete="off" clearable></el-input>
                                </el-form-item>
                            </el-form>
                            <div slot="footer" class="dialog-footer">
                                <el-button @click="sendmess = false">取 消</el-button>
                                <el-button type="primary" @click="sendmess = false">确 定</el-button>
                            </div>
                        </el-dialog>
                    </div>


                </div>
            </el-col>
        </div>


        <div style="margin-top:50px;width:75%;margin:0 auto">
            <el-tabs type="border-card" >
                <el-tab-pane label="基本信息">
                    <div style="width:90%;margin:0 auto">
                        <h4>性别：{{gender}}</h4>
                        <h4>邮箱：{{email}}</h4>
                        <h4>领域：{{area}}</h4>
                        <h4>收藏数：{{guanzhushu}}</h4>
                        <h4>粉丝数：{{fensishu}}</h4>
                    </div>
                </el-tab-pane>
                <el-tab-pane label="科技成果">
                    <div style="width:90%;margin:0 auto">
                        <el-tabs :tab-position="left" >
                            <el-tab-pane label="论文">
                                <div v-if="isexpert" > 
                                    <el-button  @click="uploadpaper" type="primary" style="floating:right;margin:0 auto" class="btn btn-success">上传论文</el-button>
                                </div>
                                <br>
                                <div>
                                    <paper></paper><br>
                                    <paper></paper>
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
                            <el-tab-pane label="专利">
                                <div v-if="isexpert" >
                                    <el-button   @click="uploadpatent" type="primary" style="floating:right" class="btn btn-success">上传专利</el-button>
                                </div>
                                <br>
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

            </el-tabs>

        </div>

       


    </div>
</template>

<script>
import Header from './Header.vue'
import paper from './paper.vue'
import patent from './patent.vue'

export default {
    name:'ExpertInfo',
    components:{Header,paper,patent},
    data() {
      return {
        username:"",
        institution:"",
        beiyinshu:"",
        chengguoshu:"",
        Hzhishu:"",
        Gzhishu:"",
        guanzhushu:"",
        fensishu:"",
        gender:"",
        email:"",
        area:"",
        dialogFormVisible:false,
        reason:"",
        sendmess:"",

        isLogined:true,

        isexpert:true
      }
    },
    methods: {
        
        //todo
        guanzhu() {
            alert("guanzhu");
            //this.fensishu=this.fensishu+1;
        },
        uploadpaper() {
            alert("uploadpaper");
        },
        uploadpatent() {
            alert("uploadpatent");
        },
        
      
    }

}

</script>

<style scoped>


</style>
