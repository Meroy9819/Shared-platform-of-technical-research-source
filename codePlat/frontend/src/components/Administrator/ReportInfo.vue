<template>
    <div>
        <el-collapse-item title="举报-xx">
            <div>举报人：{{jubaoname}}</div>
            <div>举报内容：{{jubaocontent}}</div>
            <div>举报时间：{{jubaotime}}</div>
            <el-row >
                <el-col :span="18"><div><p></p></div></el-col>
                <el-col :span="2">
                    <el-button style="float: right; padding-right: 9px " type="text">查看详情</el-button>
                </el-col>
                <el-col :span="2">
                    <el-button style="float: right; padding-right: 6px " type="text">驳回举报</el-button>
                </el-col>
                <el-col :span="2">
                    <el-button @click="showdealmodel = true" style="float: right; padding-right: 3px " type="text">认可举报</el-button>


                    <div class="modal" v-bind:class="{'is-active':showdealmodel}">
                        <el-dialog title="处理举报" :visible.sync="showdealmodel">
                            <el-form v-if="jubaotype == '1'">
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

                            <el-form v-if="jubaotype == '2'">
                                <el-form-item>
                                    要发送系统通知给专家呀//sth to do
                                </el-form-item>
                            </el-form>

                            <el-form v-if="jubaotype == '3'">
                                <el-form-item>
                                    确定删除此评论？//sth to do
                                </el-form-item>
                            </el-form>


                            <div slot="footer" class="dialog-footer">
                                <el-button @click="showdealmodel = false">取 消</el-button>
                                <el-button type="primary" @click="submitdeal">确 定</el-button>
                            </div>
                        </el-dialog>
                </div>

                </el-col>
            </el-row>
        </el-collapse-item>


    </div>
</template>


<script>

export default {
    data() {
        return {
            jubaoname:"",
            jubaocontent:"",
            jubaotime:"",
            jubaotype:'1',

            showdealmodel:false,

            radio:'',


        }
    },
    methods:{
        submitdeal() {
            this.showdealmodel = false;
            alert('jubaochulichenggongla');
        }
    }
}
</script>
