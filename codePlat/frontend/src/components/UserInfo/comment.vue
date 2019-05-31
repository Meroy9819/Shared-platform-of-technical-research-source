<template>
    <div>
        <el-collapse-item title="评论-xx">
            <div>评论对象：{{objname}}</div>
            <div>评论内容：{{comcontent}}</div>
            <div>评论时间：{{comtime}}</div>
            <el-button style="float: right; padding-right: 9px " type="text">删除</el-button>
        </el-collapse-item>
    </div>
</template>


<script>

export default {
    data() {
        return {
            objname:"",
            comcontent:"",
            comtime:""


        }
    },
    methods:{
        
    }
}
</script>
