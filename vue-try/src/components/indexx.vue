<template>
    <el-container class="tot">
        
        <v-header></v-header>
         <el-container class="main-con1" >
            <el-main>
              <el-row><el-col :span="24"><div class="grid-content"></div></el-col></el-row>
              <el-row :gutter="20">
                <el-col :span="10" :offset="5" >
                    <el-input placeholder="请输入检索内容" prefix-icon="el-icon-search" v-model="input2"></el-input>
                </el-col>
                <el-col :span="1">
                    <el-button type="primary" @click="search" icon="el-icon-search"></el-button>
                </el-col>
                <el-col :span="2" :offset="1">
                    <el-button disabled type="primary" @click="advsearch" icon="el-icon-s-fold">高级检索</el-button>
                </el-col>
              </el-row>
               <el-row><el-col :span="24"><div class="grid-content"></div></el-col></el-row>
              <el-divider></el-divider>
            </el-main>
         </el-container>
         
        <el-container class="main-con2">
            <el-main>
             <el-carousel type="card" :interval="400" class="flip" >
                <el-carousel-item v-for="paper in topPaperList" :key="paper.index">
                <el-card class="box-card" shadow="always">
              <el-row >
                <el-col :span="21" class="grid-content bg-purple-light">
                   <el-link href="https://element.eleme.io" target="_blank"><h3>{{paper.title}}</h3></el-link>
                </el-col>
                <el-col :span="1" class="grid-content bg-purple-light" :offset="1">
                    <el-button type="warning" icon="el-icon-star-off" circle @click="star" size="small"></el-button>
                </el-col>
              </el-row>
              

                <el-row>
                    <el-col :span="6" class="grid-content bg-purple-light greyfont">作者：</el-col>
                    <el-col :span="18">
                      <div class="grid-content bg-purple-light">
                              <el-link href="https://element.eleme.io" target="_blank"  v-for="au in paper.aulist" :key="au.index" class="aulink">
                                {{ au.name }}
                                 <el-divider direction="vertical"></el-divider>
                              </el-link>
                              
                      </div>
                    </el-col>
                </el-row>
                <el-row>
                    <el-col :span="6" class="grid-content bg-purple-light greyfont">关键词:</el-col>
                    <el-col :span="18">
                      <div class="grid-content bg-purple-light">
                        <el-tag v-for="tag in paper.taglist" :key="tag.index" class="tagg">
                           {{ tag.text }}
                        </el-tag>
                      </div>
                      </el-col>
                </el-row>
                 <el-row>
                    <el-col :span="6" class="grid-content bg-purple-light greyfont"><i class="el-icon-link"> 被引量:</i></el-col>
                    <el-col :span="4"><div class="grid-content bg-purple-light">{{ paper.refcnt }}</div></el-col>
                    
                    <el-tooltip placement="bottom">
                      <div slot="content">我们如何定义“阅读量”？<br/><br/>一次“阅读”行为是……</div>
                      <el-col :span="6" :offset="1" class="grid-content bg-purple-light greyfont"><i class="el-icon-view"> 阅读量:</i></el-col>
                    </el-tooltip>
                    
                    <el-col :span="4"><div class="grid-content bg-purple-light">{{ paper.readcnt }}</div></el-col>
                </el-row>
                </el-card>

                </el-carousel-item>
            </el-carousel>

            <el-divider></el-divider>

            <el-carousel type="card" :interval="400" class="flip" >
                <el-carousel-item v-for="exp in topExpList" :key="exp.index">
                <el-card class="box-card" shadow="always">
                    <el-row >
                      <el-col :span="6" class="grid-content bg-purple-light">
                        <img
                        style="width: 80px; height: 80px; border-radius: 40px"
                        src="../assets/exp.jpg"
                        ></img>
                      </el-col>
                      <el-col :span="15" class="grid-content bg-purple-light">
                        <el-row><el-col :span="24"><div class="grid-content3"></div></el-col></el-row>
                        <el-link href="https://element.eleme.io" target="_blank"><h3>{{exp.name}}</h3></el-link>
                      </el-col>
                      <el-col :span="1" class="grid-content bg-purple-light" :offset="1">
                          <el-button type="warning" icon="el-icon-star-off" circle @click="star" size="small"></el-button>
                      </el-col>
                    </el-row>
                  
                    <el-row>
                        <el-col :span="6" class="grid-content bg-purple-light"><i class="el-icon-s-cooperation"> 机构:</i></el-col>
                        <el-col :span="18"><div class="grid-content bg-purple-light">{{ exp.inst }}</div></el-col>
                    </el-row>

                    <el-row style="font-size:14px">
                        <el-col :span="5" class="grid-content bg-purple-light redfont"  >#h-index:</el-col>
                        <el-col :span="3"><div class="grid-content bg-purple-light">&nbsp;{{ exp.hindex }} </div></el-col>
                        
                        <el-col :span="5" class="grid-content bg-purple-light redfont">#g-index: </el-col>
                        <el-col :span="3"><div class="grid-content bg-purple-light">&nbsp;{{ exp.gindex }}</div></el-col>
                        
                        <el-col :span="5" class="grid-content bg-purple-light redfont">论文数: </el-col>
                        <el-col :span="3"><div class="grid-content bg-purple-light">{{ exp.papercnt }}</div></el-col>
                    </el-row>

                </el-card>

                </el-carousel-item>
            </el-carousel>

            </el-main>

            <!-- <el-aside width="25%"> -->
                
            <!-- </el-aside> -->
        </el-container>

        <el-footer>Footer</el-footer>
    </el-container>
</template>


<script>

import Header from '@/components/Header'
export default {
    data() {
      return {

        //
        topPaperList:[{
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
        refcnt:99,
        readcnt:999,
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
        refcnt:66,
        readcnt:666,
      },

      {
        index:'3',
        title:"Hello World",
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
        refcnt:11,
        readcnt:111,
      }
      ],
        //top专家信息
        topExpList:[{
          index:'1',
          name:"Douglas K. Rex",
          papercnt:99,
          inst:"IU Health University Hospital",
          hindex:99,
          gindex:99,
        },
        {
          index:'2',
          name:"aaa",
          papercnt:66,
          inst:"bbb",
          hindex:66,
          gindex:66,
        },
        {
          index:'3',
          name:"ccc",
          papercnt:111,
          inst:"ddd",
          hindex:11,
          gindex:11,
        }
        ],

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
        console.log("检索:"+this.input2);
        this.$router.push({ path:'/sr'  }); //跳转至searchresult
      },
      //高级检索（待定）
      advsearch() {
        console.log("高级检索:"+this.input2);
      }
    }
}
</script>

<style scoped>
.flip{
  background: #FCFCFC;
  height: auto;
}
/* .el-carousel__item h3 {
    color: #475669;
    font-size: 14px;
    opacity: 0.75;
    line-height: 150px;
    margin: 0;
  } */

  .el-carousel__item:nth-child(2n) {
     background-color: #99a9bf;
     height: auto;
  }
  
  .el-carousel__item:nth-child(2n+1) {
     background-color: #d3dce6;
     height: auto;
  }

.box-card {
    width: 100%;
    height: auto;
  }
.main-con1{
  width:80%;
  /* height:300px; */
  margin:0 auto;
}

.tot{
    height:100%;
}

.main-con2{
  /* height:600px; */
  width:60%;
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
    /* line-height:30px; */
    
  }
  
  .bg-purple {
    background: #6C6C6C	 ;
  }
  .bg-purple-light {
    background: #FCFCFC;
  }
  .grid-content {
    border-radius: 4px;
    min-height: 30px;
  }
  .grid-content3 {
    min-height: 5px;
  }
  .row-bg {
    padding: 10px 0;
    background-color: #f9fafc;
  }


  .aulink {
    color:#409EFF;
  }
  .tagg {
    margin-right: 20px;
  }
  /* .bt{
    margin-right: 20px;
  } */

.papercard{
  margin-bottom: 0px;
}
</style>