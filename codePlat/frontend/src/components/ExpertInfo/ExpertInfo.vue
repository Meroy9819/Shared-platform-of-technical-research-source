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
                    <el-button @click="jubaomodel = true" style="display:block;margin:0 auto" class="btn btn-success">举报</el-button><br>

                    <div class="modal" v-bind:class="{'is-active':jubaomodel}">
                        <el-dialog title="举报信息" :visible.sync="jubaomodel">
                            <el-form >
                                <el-form-item label="举报理由" :label-width="formLabelWidth">
                                <el-input type="textarea" :rows="3" v-model="reason" placeholder="请输入举报理由" autocomplete="off" clearable></el-input>
                                </el-form-item>
                            </el-form>
                            <div slot="footer" class="dialog-footer">
                                <el-button @click="jubaomodel = false">取 消</el-button>
                                <el-button type="primary" @click="submitjubao">确 定</el-button>
                            </div>
                        </el-dialog>
                    </div>

                    <el-button @click="renlingmodel = true" style="display:block;margin:0 auto" class="btn btn-success">认领</el-button><br>
                
                    <div class="modal" v-bind:class="{'is-active':renlingmodel}">
                        <el-dialog title="认领专家" :visible.sync="renlingmodel">
                            <el-form :model="form" style="width:60%;text-align:left;margin-left:50px;height:300px">
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
                                    </el-form>
                            <div slot="footer" class="dialog-footer">
                                <el-button @click="renlingmodel = false">取 消</el-button>
                                <el-button type="primary" @click="submitrenling">确 定</el-button>
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
                                <div> 
                                    <el-row>
                                    <el-col :span="14" v-if="isexpert">

                                        <el-button  @click="upload = true" type="primary" style="floating:right;margin:0 auto" class="btn btn-success">上传资源</el-button>
                                        <!-- 标题 作者姓名（多个作者，字符串存储，逗号隔开），关键词，引用数，发表年份，摘要，附件 -->
                                        <div class="modal" v-bind:class="{'is-active':upload}">
                                            <el-dialog title="上传资源" :visible.sync="upload">
                                                <el-form :model="form">
                                                    <el-form-item label="标题" :label-width="formLabelWidth" :rules="{
                                                        required: true, message: '标题不能为空', trigger: 'blur'
                                                        }">
                                                    <el-input v-model="form.title" autocomplete="off"></el-input>
                                                    </el-form-item>

                                                    <el-form-item
                                                        v-for="(au, index) in form.aulist"
                                                        :label="'作者' + (index+1)"
                                                        :key="au.key"
                                                        :prop="'aulist.' + index + '.auname'"
                                                        :label-width="formLabelWidth"
                                                    >
                                                    <el-col :span="12">
                                                        <el-input v-model="au.auname"></el-input>
                                                    </el-col>
                                                    <el-col :span="2" :offset="1">
                                                        <el-button @click.prevent="removeAuthor(au)">删除</el-button>
                                                    </el-col>
                                                    </el-form-item>
                                                    <el-form-item :label-width="formLabelWidth">
                                                        <el-button @click="addAuthor">添加作者</el-button>
                                                    </el-form-item>

                                                    <el-form-item
                                                        v-for="(tag, index) in form.taglist"
                                                        :label="'关键词' + (index+1)"
                                                        :key="tag.key"
                                                        :prop="'taglist.' + index + '.tagname'"
                                                        :label-width="formLabelWidth"
                                                    >
                                                    <el-col :span="12">
                                                        <el-input v-model="tag.tagname"></el-input>
                                                    </el-col>
                                                    <el-col :span="2" :offset="1">
                                                        <el-button @click.prevent="removeTag(tag)">删除</el-button>
                                                    </el-col>
                                                    </el-form-item>
                                                    <el-form-item :label-width="formLabelWidth">
                                                        <el-button @click="addTag">添加关键词</el-button>
                                                    </el-form-item>

                                                    <el-form-item label="发表年份" :label-width="formLabelWidth">
                                                        <el-date-picker
                                                            v-model="form.pubyear"
                                                            type="year"
                                                            placeholder="选择年"
                                                            value-format="yyyy">
                                                        </el-date-picker>
                                                    </el-form-item>

                                                    <el-form-item label="摘要" :label-width="formLabelWidth">
                                                        <el-input
                                                            type="textarea"
                                                            :rows="6"
                                                            v-model="form.abs">
                                                        </el-input>
                                                    </el-form-item>

                                                    <el-form-item label="引用数" :label-width="formLabelWidth">
                                                        <el-input  v-model="form.refcnt"></el-input>
                                                    </el-form-item>

                                                    <el-form-item label="上传附件" :label-width="formLabelWidth">
                                                        <el-upload
                                                            class="upload-demo"
                                                            drag
                                                            :multiple="false"
                                                            :limit="1"
                                                            :before-upload="precheck"
                                                            action="https://jsonplaceholder.typicode.com/posts/"  >
                                                            <i class="el-icon-upload"></i>
                                                            <div class="el-upload__text">将文件拖到此处，或<em>点击上传</em></div>
                                                        </el-upload>
                                                    </el-form-item>

                                                
                                                </el-form>
                                                <div slot="footer" class="dialog-footer">
                                                    <el-button @click="upload = false">取 消</el-button>
                                                    <el-button type="primary" @click="onSubmit">发 布</el-button>
                                                </div>
                                                </el-dialog>

                                        </div>
                                    </el-col>
                                    <el-col :span="14" v-if="!isexpert"><div><h6></h6></div>
                                    </el-col>
                                    <el-col :span="10" >

                                        <div style="floating:right;margin-right:0px">

                                            <!-- <button>ok</button>         -->

                                            <el-col :span="20">
                                                <el-input placeholder="快速检索" prefix-icon="el-icon-search" v-model="input2"></el-input>
                                            </el-col>
                                            <el-col :span="2">
                                                <el-button type="primary" icon="el-icon-search"></el-button>
                                            </el-col>
                                        </div>
                                    </el-col>
                                    </el-row>
                                </div>
                                <br>
                                <div>
                                    <el-collapse v-model="activeNames" @change="handleChange">
                                        <paper></paper>
                                        <paper></paper>
                                    </el-collapse>
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
import Header from '@/components/Header'
import paper from './paper.vue'
import wordcloud from 'vue-wordcloud'


export default {
    name:'ExpertInfo',
    components:{Header,paper,wordcloud},
    data() {
      return {
          input2:"",
        username:this.$route.params.username,
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
        jubaomodel:false,
        renlingmodel:false,
        reason:"",
        evidence:"",
        // sendmess:false,

        isLogined:true,

        isexpert:true,
        upload:false,

        //表单字段
        form: {
          title: '',
          aulist: [{
            auname: ''
          }],
          taglist: [{
            tagname: ''
          }],
          pubyear:'',
          abs:'',
          refcnt:''
        },

        formLabelWidth: '120px'


      }
    },
    methods: {
        
        //todo
        guanzhu() {
            alert("guanzhu");
            //this.fensishu=this.fensishu+1;
        },
        addAuthor() {
            this.form.aulist.push({
            auname: '',
            key: Date.now()
            });
        },
        removeAuthor(item) {
            var index = this.form.aulist.indexOf(item)
            if (index !== -1) {
            this.form.aulist.splice(index, 1)
            }
        },
        addTag() {
            this.form.taglist.push({
            tagname: '',
            key: Date.now()
            });
        },
        removeTag(item) {
        var index = this.form.taglist.indexOf(item)
            if (index !== -1) {
            this.form.taglist.splice(index, 1)
            }
        },
        precheck(file){
            const isPDF = file.type === 'pdf';
            if (!isPDF) {
                this.$message.error('请上传 PDF 格式的附件');
            }
            return isPDF;
        },

        //提交表单
        onSubmit() {
            this.upload = false;
            // console.log(this.form);
            console.log(Date.toLocaleDateString());
        },
        submitjubao() {
            this.jubaomodel = false;
            alert('提交举报了');
        },
        submitrenling() {
            this.renlingmodel = false;
            alert('提交renling了');
        }

    }

}

</script>

<style scoped>


</style>
