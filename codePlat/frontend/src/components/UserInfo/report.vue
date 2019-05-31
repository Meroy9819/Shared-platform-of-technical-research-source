<template>
    <div>
        <el-collapse-item title="举报-xx">
            <div>举报对象：{{objname}}</div>
            <div>举报内容：{{jubaocontent}}</div>
            <div>举报时间：{{jubaotime}}</div>
            <div>举报状态：{{jubaostates}}</div>
        </el-collapse-item>
    </div>
</template>


<script>

export default {
    data() {
        return {
            objname:"",
            jubaocontent:"",
            jubaotime:"",
            jubaostates:""


        }
    },
    methods:{
        
    }
}
</script>
