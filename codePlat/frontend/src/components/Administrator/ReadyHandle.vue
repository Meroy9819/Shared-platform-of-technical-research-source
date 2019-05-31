<template>
    <el-collapse-item title="不知道咋设置更好，todo ">
        <div>用户名：{{username}}</div>
        <div>类型：{{type}}</div>
        <div>时间：{{sendingtime}}</div>
        <div>回复结果：{{result}}</div>
        <div>回复时间：{{backingtime}}</div>
            
    </el-collapse-item>    
</template>


<script>

export default {
    data() {
        return {
            username:"",
            type:"",
            sendingtime:"",
            backingtime:"",
            result:""


        }
    },
    methods:{
        
    }
}
</script>
