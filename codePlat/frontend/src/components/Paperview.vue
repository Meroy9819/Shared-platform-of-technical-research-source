Skip to content

Search or jump to…

Pull requests
Issues
Marketplace
Explore

@Meroy9819
 Watch 0
 Star 2  Fork 1 Meroy9819/Shared-platform-of-technical-research-source
 Code  Issues 0  Pull requests 0  Projects 0  Wiki  Security  Insights  Settings
Branch: frontend
Shared-platform-of-technical-research-source/vue-try/src/components/Paperview.vue
Find file Copy path
@billzhaox billzhaox working on indexx
38b4fe0 2 days ago
1 contributor
318 lines (282 sloc)  9.44 KB
RawBlameHistory

<template>
    <el-container class="tot">

        <v-header></v-header>
        <el-container class="main-con">
            <el-main width="60%">
              <el-row :gutter="20">
                <el-col :span="12">
                   <el-link href="https://element.eleme.io" target="_blank"><h2>{{title}}</h2></el-link>
                </el-col>
                <el-col :span="3" class="bt">
                    <el-button type="warning" icon="el-icon-star-on" @click="star">收藏</el-button>
                </el-col>
                <el-col :span="3"  :offset="1" class="bt">
                    <el-button type="danger" icon="el-icon-warning" @click="wrong">报错</el-button>
                </el-col>
                <el-col :span="3" :offset="1" class="bt">
                    <el-popover
                      placement="top"
                      width="160"
                      trigger="hover"
                      >
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
                    <el-col :span="3" class="grid-content bg-purple-light">作者：</el-col>
                    <el-col :span="21">
                      <div class="grid-content bg-purple-light">
                              <el-link href="https://element.eleme.io" target="_blank"  v-for="au in aulist" :key="au.index" class="aulink">
                                {{ au.name }}
                                 <el-divider direction="vertical"></el-divider>
                              </el-link>

                      </div>
                    </el-col>
                </el-row>
                <el-row>
                    <el-col :span="3" class="grid-content bg-purple-light">摘要:</el-col>
                    <el-col :span="21">
                      <div class="grid-content bg-purple-light">
                        {{abs}}
                      </div>
                    </el-col>
                </el-row>
                <el-row>
                    <el-col :span="3" class="grid-content bg-purple-light">关键词:</el-col>
                    <el-col :span="21">
                      <div class="grid-content bg-purple-light">
                        <el-tag v-for="tag in taglist" :key="tag.index" class="tagg">
                           {{ tag.text }}
                        </el-tag>
                      </div>
                      </el-col>
                </el-row>
                 <el-row>
                    <el-col :span="3" class="grid-content bg-purple-light"><i class="el-icon-link"> 被引量:</i></el-col>
                    <el-col :span="3"><div class="grid-content bg-purple-light">{{ refcnt }}</div></el-col>

                    <el-tooltip placement="bottom">
                      <div slot="content">我们如何定义“阅读量”？<br/><br/>一次“阅读”行为是……</div>
                      <el-col :span="3" :offset="1" class="grid-content bg-purple-light"><i class="el-icon-view"> 阅读量:</i></el-col>
                    </el-tooltip>

                    <el-col :span="3"><div class="grid-content bg-purple-light">{{ readcnt }}</div></el-col>
                </el-row>

                </el-card>
            </el-main>

            <el-aside width="25%">
                <el-card class="box-card2">
                    <div slot="header" class="clearfix">
                        <span>评论区</span>
                        <el-button style="float: right; padding: 3px 0" type="text" @click="addcomm" icon="el-icon-edit">添加评论</el-button>
                    </div>
                    <div v-for="item in commlist" :key="item" class="text item">
                      <el-row class="comm">
                        <el-col :span="8" class="grid-content bg-purple-light">
                        <img
                        style="width: 50px; height: 50px"
                        src="../assets/timg.jpg"
                        ></img>
                        </el-col>
                        <el-col :span="16" class="grid-content bg-purple-light">
                        <el-link href="https://element.eleme.io" target="_blank">{{ username }}</el-link>
                        </el-col>
                      </el-row>
                      <el-row class="comm">
                        <el-col :span="24" class="grid-content bg-purple-light">{{ item }}</el-col>
                      </el-row>
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
export default {
    data() {
      return {
        // 成果信息
        title:"多层弹性半空间中的地震波(一)",
        aulist: [
        { index:'1',name: 'author1' },
        { index:'2',name: 'author2' },
        { index:'3',name: 'author3' },
      ],
        abs:"引言 地震面波的频散性质、地震波辐射的方向性等特性已经广泛地用于地壳和上地幔结构以及震源机制的研究中,并且取得了许多有用的成果.研究地震波如何从震源辐射出来、如何在实际介质中传播和衰减的这一问题,对于利用地震波确定地壳和上地幔结构以及震源的参数,是很有必要的.关于这一问题的研究,已经作过许多工作。已往的工作中,为了分析方便,往往采用简单的地壳—上地幔模型或简单的震源模型,或两者都相",
        taglist: [
        { index:'1',text: 'tag1' },
        { index:'2',text: 'tag2' },
        { index:'3',text: 'tag3' },
      ],
        refcnt:99,
        readcnt:999,
        // 评论列表A
        commlist:[],
        //用户名
        username:"uname",
      }

    },
    components:{
        'v-header':Header
    },
    methods: {
      //点击收藏按钮触发：
      star(){
        console.log("点击收藏");
        this.$message({
          message: '收藏成功',
          type: 'success'
        });
      },
      //点击添加评论触发
      addcomm() {
        this.$prompt('请输入评论内容', '添加评论', {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          inputErrorMessage: 'Invalid'
        }).then(({ value }) => {
          this.$message({
            type: 'success',
            message: '评论成功'
          });
          console.log(value); //value为评论内容
          this.commlist.push(value);
        }).catch(() => {
          this.$message({
            type: 'info',
            message: '取消输入'
          });
        });
      },
      //点击报错按钮触发
      wrong(){
        this.$prompt('请输入报错内容', '报错', {
          confirmButtonText: '提交反馈',
          cancelButtonText: '取消',
          inputErrorMessage: 'Invalid'
        }).then(({ value }) => {
          this.$message({
            type: 'success',
            message: '报错成功'
          });
          console.log(value); //value为报错内容
          // this.commlist.push(value);
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
          params: {resource_id: 1}
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
.tot{
    height:100%;
}
.main-con{
  /* height:600px; */
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
    margin-bottom: 15px;

  }
  /* p:last-child {
      margin-bottom: 0;
    } */
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
  /* .bt{
    margin-right: 20px;
  } */
  /* 评论row */
.comm{
  margin-bottom: 5px;
  text-align: left;
}
</style>
