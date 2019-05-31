<template>
    <el-card style="height:50px;margin-top:1px">
        <div style="height:50px;vertical-align:middle;">
            <el-row >
                <el-col :span="14">
                    名称：{{exname}}
                </el-col>
                <el-col :span="8">
                    机构：{{exins}}
                </el-col>
            </el-row>
        </div>
    </el-card>
</template>


<script>

export default {
    data() {
        return {
            exname:"",
            exins:""

        }
    },
    methods:{
        
    }
}
</script>
