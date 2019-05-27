<template>
    <el-card class="box-card">
        <div slot="header" class="clearfix">
            <span>系统通知的题目{{SMtitle}}</span>
            <el-button style="float: right; padding: 3px 0" type="text">操作按钮</el-button>
        </div>
        <div >内容（不知系统通知是啥样，那就这样吧）{{SMcontent}}</div>
        <div>发送时间{{SMsendtime}}</div>

    </el-card>
</template>



<script>

export default {
    data() {
        return {
            SMtitle:"",
            SMcontent:"",
            SMsendtime:""

        }
        
    }
}

</script>