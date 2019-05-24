<template>
    <el-container>
        
        <v-header></v-header>
         <el-container class="main-con1">
            <el-main width="60%">
              <el-row :gutter="20">
                <el-col :span="10">
                    <el-input placeholder="请输入检索内容" prefix-icon="el-icon-search" v-model="input2"></el-input>
                </el-col>
                <el-col :span="1">
                    <el-button type="primary" @click="search" icon="el-icon-search"></el-button>
                </el-col>
                <el-col :span="2" :offset="1">
                    <el-button type="primary" @click="advsearch" icon="el-icon-s-fold">高级检索</el-button>
                </el-col>
              </el-row>
              <el-divider></el-divider>
            </el-main>
         </el-container>
         
        <el-container class="main-con">
            <el-main width="60%">
              <el-row  v-for="paper in paperlist" :key="paper.index">
              <el-card class="box-card" shadow="always">
              <el-row >
                <el-col :span="16" class="grid-content bg-purple-light">
                   <el-link href="https://element.eleme.io" target="_blank"><h2>{{paper.title}}</h2></el-link>
                </el-col>
                <el-col :span="1" class="grid-content bg-purple-light" :offset="7">
                    <el-button type="warning" icon="el-icon-star-off" circle @click="star" size="small"></el-button>
                </el-col>
              </el-row>
              

                <el-row>
                    <el-col :span="3" class="grid-content bg-purple-light">作者：</el-col>
                    <el-col :span="21">
                      <div class="grid-content bg-purple-light">
                              <el-link href="https://element.eleme.io" target="_blank"  v-for="au in paper.aulist" :key="au.index" class="aulink">
                                {{ au.name }}
                                 <el-divider direction="vertical"></el-divider>
                              </el-link>
                              
                      </div>
                    </el-col>
                </el-row>
                <el-row>
                    <el-col :span="3" class="grid-content bg-purple-light">关键词:</el-col>
                    <el-col :span="21">
                      <div class="grid-content bg-purple-light">
                        <el-tag v-for="tag in paper.taglist" :key="tag.index" class="tagg">
                           {{ tag.text }}
                        </el-tag>
                      </div>
                      </el-col>
                </el-row>
                 <el-row>
                    <el-col :span="3" class="grid-content bg-purple-light"><i class="el-icon-link"> 被引量:</i></el-col>
                    <el-col :span="3"><div class="grid-content bg-purple-light">{{ paper.refcnt }}</div></el-col>
                    
                    <el-tooltip placement="bottom">
                      <div slot="content">我们如何定义“阅读量”？<br/><br/>一次“阅读”行为是……</div>
                      <el-col :span="3" :offset="1" class="grid-content bg-purple-light"><i class="el-icon-view"> 阅读量:</i></el-col>
                    </el-tooltip>
                    
                    <el-col :span="3"><div class="grid-content bg-purple-light">{{ paper.readcnt }}</div></el-col>
                </el-row>
                </el-card>
                <el-divider></el-divider>
              </el-row>
            </el-main>

            <el-aside width="25%">
                
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
        paperlist:[{
        index:'1',
        title:"多层弹性半空间中的地震波(一)",
        aulist: [
        { index:'1',name: 'author1' },
        { index:'2',name: 'author2' },
        { index:'3',name: 'author3' },
      ],
        taglist: [
        { index:'1',text: 'tag1' },
        { index:'2',text: 'tag2' },
        { index:'3',text: 'tag3' },
      ],
        refcnt:"99",
        readcnt:"999",
      },

      {
        index:'2',
        title:"Ad Hoc Positioning System (APS)",
        aulist: [
        { index:'1',name: 'author1' },
        { index:'2',name: 'author2' },
        { index:'3',name: 'author3' },
      ],
        taglist: [
        { index:'1',text: 'tag1' },
        { index:'2',text: 'tag2' },
        { index:'3',text: 'tag3' },
      ],
        refcnt:"66",
        readcnt:"666",
      }
      ],
        // 评论列表
        commlist:[],

        //用户名
        username:"uname",
        //检索内容
        input2: '',
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
      
      //检索
      search() {
        console.log('search!');
      },
      //高级检索（待定）
      advsearch() {
        console.log('advsearch!');
      }
    }
}
</script>

<style scoped>

.main-con1{
  width:80%;
  margin:0 auto;
}

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