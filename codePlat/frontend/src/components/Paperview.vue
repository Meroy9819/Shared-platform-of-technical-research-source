<template>
    <el-container>

        <v-header></v-header>
        <el-container class="main-con">
            <el-main width="60%">
              <el-row>
                <el-col :span="12">
                   <el-link href="https://element.eleme.io" target="_blank"><h2>{{sciachi.name}}</h2></el-link>
                </el-col>
                <el-col :span="3" class="bt">
                    <el-button type="primary" icon="el-icon-star-on" >收藏</el-button>
                </el-col>
                <el-col :span="3" class="bt">
                    <el-button type="primary" icon="el-icon-warning">报错</el-button>
                </el-col>
                <el-col :span="3" class="bt">
                    <el-popover
                      placement="top"
                      width="160"
                      trigger="hover"
                      v-model="visible2">
                      <p>分享方式blabla</p>
                      <div style="text-align: right; margin: 0">
                        <el-button type="primary" size="mini" icon="el-icon-eleme"></el-button>
                        <el-button type="primary" size="mini" icon="el-icon-eleme"></el-button>
                      </div>
                      <el-button slot="reference" icon="el-icon-share" type="primary">分享</el-button>
                    </el-popover>
                </el-col>
              </el-row>
              <el-card class="box-card" shadow="hover">

                <el-row>
                    <el-col :span="3">作者：</el-col>
                    <el-col :span="21">
                      <div class="grid-content bg-purple-light">
                              <el-link href="https://element.eleme.io" target="_blank"  v-for="au in aulist" key="au" class="aulink">
                                {{ au.name }}
                                 <el-divider direction="vertical"></el-divider>
                              </el-link>
                      </div>
                    </el-col>
                </el-row>
                <el-row>
                    <el-col :span="3">摘要:</el-col>
                    <el-col :span="21">
                      <div class="grid-content bg-purple-light">
                        <p>{{sciachi.abstract}}</p>
                      </div>
                    </el-col>
                </el-row>
                <el-row>
                    <el-col :span="3">关键词:</el-col>
                    <el-col :span="21">
                      <div class="grid-content bg-purple-light">
                        <el-tag v-for="tag in sciachi.keywordSeq" key="au" class="tagg">
                           {{ tag }}
                        </el-tag>
                      </div>
                      </el-col>
                </el-row>
                 <el-row>
                    <el-col :span="3">被引量:</el-col>
                    <el-col :span="21"><div class="grid-content bg-purple-light">{{ sciachi.refCount }}</div></el-col>
                </el-row>

                </el-card>
            </el-main>

            <el-aside width="25%">
                <el-card class="box-card2">
                    <div slot="header" class="clearfix">
                        <span>评论区</span>
                        <el-button style="float: right; padding: 3px 0" type="text" @click="open" icon="el-icon-edit">添加评论</el-button>
                    </div>
                    <div v-for="o in 4" :key="o" class="text item">
                        {{'评论内容 ' + o }}
                        <el-divider></el-divider>
                    </div>
                </el-card>
            </el-aside>
        </el-container>

        <el-footer>Footer</el-footer>
    </el-container>
</template>


<script>
import Header from '@/components/Header'
import Axios from 'axios'
export default {
    data() {
      return {
        // name: "",
        aulist: [
          {name: 'author1'},
        ],
        // abs: "",
        // taglist: [
        //   {text: 'tag1'},
        // ],
        // refcnt: "99",
        sciachi : {}
      }
    },
    components:{
        'v-header':Header
    },
    methods: {
      open() {
        this.$prompt('请输入评论内容', '添加评论', {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          inputErrorMessage: 'Invalid'
        }).then(({ value }) => {
          this.$message({
            type: 'success',
            message: '评论成功'
          });
        }).catch(() => {
          this.$message({
            type: 'info',
            message: '取消输入'
          });
        });
      },
      init:function(){
        let _this = this;
        this.$http.request({
          url:_this.$url + 'paperview',
          method:'get',
          params: {resource_id: 1,"contentType": "application/json;charset=utf-8"}
        }).then(function (response) {
          _this.sciachi = response.data[0];
          console.log('heihei');
          console.log(response)
        }).catch(function (response) {
          console.log('gg');
          console.log(response)
        })
      }
    },
    mounted:function () {
      this.init()
    }
}
</script>

<style scoped>
.main-con{
  height:600px;
  width:80%;
  margin:0 auto;
}
/* Container布局容器 */
  .el-footer {
    background-color: #66CDAA;
    color: #fff;
    text-align: left;
    line-height: 60px;
    /* vertical-align: middle;  */
  }
  .el-aside {
    /* background-color: #D3DCE6; */
    color: #333;
    text-align: center;
    line-height: auto;
    margin-left: 30px;
    margin-right: 30px;
  }
  .el-main {
    /* background-color: #E9EEF3; */
    color: #333;
    text-align: left;
    line-height: auto;
    margin-left: 20px;
  }
  body > .el-container {
    margin-bottom: 40px;
  }
  .el-container:nth-child(5) .el-aside,
  .el-container:nth-child(6) .el-aside {
    line-height: 260px;
  }
  .el-container:nth-child(7) .el-aside {
    line-height: 320px;
  }
/* 分栏 */
.el-row {
    margin-bottom: 10px;
  }
  p:last-child {
      margin-bottom: 0;
    }
  .el-col {
    border-radius: 4px;
    line-height:30px;
  }
  .bg-purple-light {
    background: #FCFCFC;
  }
  .grid-content {
    border-radius: 4px;
    min-height: 36px;
  }
  .row-bg {
    padding: 10px 0;
    background-color: #f9fafc;
  }
  /* 卡片组件 */
  .text {
    font-size: 14px;
  }
  .item {
    margin-bottom: 18px;
  }
  .clearfix:before,
  .clearfix:after {
    display: table;
    content: "";
  }
  .clearfix:after {
    clear: both
  }
  .box-card {
    margin-top: 15px;
  }
  .box-card2 {
    width: auto;
    margin-top: 18px;
  }
  .aulink {
    color:#0080FF;
  }
  .tagg {
    margin-right: 20px;
  }
  .bt{
    margin-right: 20px;
  }
</style>
