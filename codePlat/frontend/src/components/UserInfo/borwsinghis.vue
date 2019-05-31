<template>
    <div>
        <el-collapse-item title="浏览-time">
            <div>浏览对象：{{objname}}</div>    
            <!-- 这里应该有链接跳转的 -->
            <div>历史时间：{{histime}}</div>
        </el-collapse-item>
    </div>
</template>


<script>

export default {
    data() {
        return {
            objname:"",//the name of the paper or the expert
            histime:""


        }
    },
    methods:{
        
    }
}
</script>
