<template>
    <div>
        <HeaderNoLogin></HeaderNoLogin>

        <div id="card" class="container" >
          <el-card class="box-card" style="text-align: center;">

            <el-form :model="ruleForm2" status-icon :rules="rules2" ref="ruleForm2" class="demo-ruleForm">
              <el-form-item>
                <span>真实姓名：</span>
                <el-input v-model="realname" style="float:right;margin-right:80px;width:160px" placeholder="请输入真实姓名"></el-input>
              </el-form-item>
              <el-form-item>
                <span>所属机构：</span>
                <el-input v-model="institution" style="float:right;margin-right:80px;width:160px" placeholder="请输入所属机构"></el-input>
              </el-form-item>
              <el-form-item>
                <span>署名成果名称：</span>
                <el-input v-model="papertitle" style="float:right;margin-right:80px;width:160px" placeholder="请输入已出版署名成果名称"></el-input>
              </el-form-item>
              <el-form-item>
                <span>成果出版时间：</span>
                <el-input v-model="paperpublishedtime" style="float:right;margin-right:80px;width:160px" placeholder="请输入出版时间"></el-input>
              </el-form-item>
              <el-form-item>
                <span>所属研究领域：</span>
                <el-input v-model="area" style="float:right;margin-right:80px;width:160px" placeholder="请输入所属研究领域"></el-input>
              </el-form-item>
              <el-form-item>
                <el-button type="primary" round style="float:left;margin-left:60px;text-align:center" @click="submit">提交</el-button>
                <el-button type="primary" round style="float:right;margin-right:80px;text-align:center"
                @click="gotouserhome" class="btn btn-success">取消</el-button>
              </el-form-item>
            </el-form>



          </el-card>
        </div>


        



    </div>
</template>

<script>
import HeaderNoLogin from '../UserInfo/HeaderNoLogin'

export default {
    components:{HeaderNoLogin},
    data() {
        return {
            realname:"",
            institution:"",
            papertitle:"",
            paperpublishedtime:"",
            area:""
        }
    },
    methods: {
        submit() {

        },
        gotouserhome() {
            this.$router.replace('/UserInfo')
        }

    }

}

</script>


<style scoped>
.box-card {
    width: 480px;
    height:400px;
    margin:0 auto;
    margin-top:20px;
  }
</style>
