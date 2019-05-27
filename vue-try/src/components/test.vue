<template>
    <div>
        <!-- Form -->
        <el-button type="primary" @click="dialogFormVisible = true">上传资源</el-button>

        <el-dialog title="上传资源" :visible.sync="dialogFormVisible">
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
            <el-button @click="dialogFormVisible = false">取 消</el-button>
            <el-button type="primary" @click="onSubmit">发 布</el-button>
        </div>
        </el-dialog>

    </div>
    <!-- 标题 作者姓名（多个作者，字符串存储，逗号隔开），关键词，引用数，发表年份，摘要，附件 -->
</template>

<script>
export default {
    data() {
      return {
        dialogFormVisible: false,

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

        formLabelWidth: '120px',

        
      };
    },

    methods: {
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
            this.dialogFormVisible = false;
            // console.log(this.form.pubyear);
            console.log(this.form);
        },
    }
}
</script>

<style scoped>

</style>

