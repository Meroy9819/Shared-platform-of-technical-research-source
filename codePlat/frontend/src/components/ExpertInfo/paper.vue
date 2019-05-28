<template>
    <el-card class="box-card">
        <div slot="header" class="clearfix">
            <span>论文题目</span>
            <el-button style="float: right; padding: 3px 0" type="text">操作按钮</el-button>
        </div>
        <div >作者：</div>
        <div >发表时间：</div>
        <div >摘要：</div>
        <div >售价：</div>
    </el-card>
</template>


<script>

export default {
    data() {
        return {
            papertitle:"",
            paperauthors:"",
            paperpublishtime:"",
            paperabstract:"",
            paperprice:""

        }
        
    }
}

</script>
