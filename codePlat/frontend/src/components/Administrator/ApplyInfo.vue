<template>
            <el-collapse-item title="申请-xx">
                <div>用户名：{{applyname}}</div>
                <div>认证类型：{{applytype}}</div>
                <div>申请时间：{{applytime}}</div>
                <div>认证信息：（一大坨/一张图）</div>
                <el-row>
                    <el-col :span="20"><div><p></p></div></el-col>
                    <el-col :span="2">
                        <el-button style="float: right; padding-right: 6px " type="text">驳回申请</el-button>
                    </el-col>
                    <el-col :span="2">
                        <el-button style="float: right; padding-right: 3px " type="text">统一申请</el-button>
                    </el-col>
                </el-row>
            </el-collapse-item>    
</template>


<script>

export default {
    data() {
        return {
            applyname:"",
            applytype:"认领",
            applycontent:"",
            applytime:"",




        }
    },
    methods:{
        
    }
}
</script>
