<template>
    <el-card style="height:50px;margin-top:1px">
        <div style="height:50px;vertical-align:middle;">
            <el-row >
                <el-col :span="13">
                    名称：{{paname}}
                </el-col>
                <el-col :span="8">
                    作者：{{paau}}
                </el-col>
            </el-row>
        </div>
    </el-card>
</template>


<script>

export default {
    data() {
        return {
            paname:"",
            paau:""

        }
    },
    methods:{
        
    }
}
</script>
