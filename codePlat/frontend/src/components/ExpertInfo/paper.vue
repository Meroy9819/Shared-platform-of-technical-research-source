<template>

    <div>
        <el-collapse-item title="论文题目">
            <div >作者：{{paperauthors}}</div>
            <div >发表时间：{{paperpublishtime}}</div>
            <div>关键词：{{keywords}}</div>
            <div >摘要：{{paperabstract}}</div>
            <el-button v-if="isexpert" @click="editpaper = true" style="float: right; padding: 3px 0" type="text">编辑本成果</el-button>

                <div class="modal" v-bind:class="{'is-active':editpaper}">
                        <el-dialog title="编辑论文" :visible.sync="editpaper">
                            <el-form >
                                <el-form-item>
                                    <el-radio v-model="radio" label="1">修改</el-radio>
                                    <el-radio v-model="radio" label="2">下架</el-radio>
                                </el-form-item>
                                <el-form-item v-if="radio == '1'" label="请选择修改内容类型">
                                    <el-select v-model="value" clearable placeholder="请选择修改项">
                                        <el-option
                                        v-for="item in options"
                                        :key="item.value"
                                        :label="item.label"
                                        :value="item.value">
                                        </el-option>
                                    </el-select>
                                </el-form-item>
                                <el-form-item v-if="radio == '1'" label="请输入新设定内容">
                                    <el-input type="textarea" :rows="3" v-model="content" placeholder="请输入新设定内容" autocomplete="off" clearable></el-input>
                                </el-form-item>
                            </el-form>
                            <div slot="footer" class="dialog-footer">
                                <el-button @click="editpaper = false">取 消</el-button>
                                <el-button type="primary" @click="submitedit">确 定</el-button>
                            </div>
                        </el-dialog>
                </div>

        </el-collapse-item>


    </div>

</template>


<script>

export default {
    data() {
        return {
            papertitle:"",
            paperauthors:"",
            paperpublishtime:"",
            paperabstract:"",
            keywords:"",

            isexpert:true,
            editpaper:false,
            radio:'',
            content:"",

            options: [{
            value: '选项1',
            label: '标题'
            }, {
            value: '选项2',
            label: '时间'
            }, {
            value: '选项3',
            label: '摘要'
            }, {
            value: '选项4',
            label: '关键词'
            },{
            value: '选项5',
            label: '发表年份'
            }],
            value: ''

        }

    },
    methods:{
        submitedit() {
            this.editpaper = false;
            alert('edit paper over');
        }
    }
}

</script>
