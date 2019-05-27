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
                    <el-button disabled type="primary" @click="advsearch" icon="el-icon-s-fold">高级检索</el-button>
                </el-col>
              </el-row>
              <el-divider></el-divider>
            </el-main>
         </el-container>
         
        <el-container class="main-con2">
            <el-main width="60%">
              <el-tabs v-model="activeName" type="card" @tab-click="handleClick">
                <el-tab-pane label="论文" name="first">
                    <el-row  class="papercard" v-for="paper in paperlist.slice((currentPage-1)*pagesize,currentPage*pagesize)" :key="paper.index">
                      <el-card class="box-card" shadow="always">
                      <el-row >
                        <el-col :span="16" class="grid-content bg-purple-light">
                          <el-link @click="topv" target="_blank"><h2>{{paper.title}}</h2></el-link>
                        </el-col>
                        <el-col :span="1" class="grid-content bg-purple-light" :offset="7">
                            <el-button type="warning" icon="el-icon-star-off" circle @click="star" size="small"></el-button>
                        </el-col>
                      </el-row>
                      

                        <el-row>
                            <el-col :span="3" class="grid-content bg-purple-light greyfont">作者：</el-col>
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
                            <el-col :span="3" class="grid-content bg-purple-light greyfont">关键词:</el-col>
                            <el-col :span="21">
                              <div class="grid-content bg-purple-light">
                                <el-tag v-for="tag in paper.taglist" :key="tag.index" class="tagg">
                                  {{ tag.text }}
                                </el-tag>
                              </div>
                              </el-col>
                        </el-row>
                        <el-row>
                            <el-col :span="3" class="grid-content bg-purple-light greyfont">发表年份:</el-col>
                            <el-col :span="3"><div class="grid-content bg-purple-light">{{ paper.pubyear }}</div></el-col>

                            <el-col :span="3" class="grid-content bg-purple-light greyfont"><i class="el-icon-link"> 被引量:</i></el-col>
                            <el-col :span="3"><div class="grid-content bg-purple-light">{{ paper.refcnt }}</div></el-col>
                            
                            <el-tooltip placement="bottom">
                              <div slot="content">我们如何定义“阅读量”？<br/><br/>一次“阅读”行为是……</div>
                              <el-col :span="3" :offset="1" class="grid-content bg-purple-light greyfont"><i class="el-icon-view"> 阅读量:</i></el-col>
                            </el-tooltip>
                            
                            <el-col :span="3"><div class="grid-content bg-purple-light">{{ paper.readcnt }}</div></el-col>
                        </el-row>
                        </el-card>
                        <el-divider></el-divider>
                      </el-row>

                      <el-pagination
                        background
                        layout="prev, pager, next"
                        :total="total"
                        :page-size="pagesize"
                        :hide-on-single-page=true
                        @current-change="current_change">
                      </el-pagination>
                </el-tab-pane>

                <el-tab-pane label="专家" name="second">
                  <el-row  class="papercard" v-for="exp in explist.slice((currentPage-1)*pagesize,currentPage*pagesize)" :key="exp.index">
                      <el-card class="box-card" shadow="always">
                      <el-row>
                        <el-col :span="4" class="grid-content bg-purple-light">
                          <el-row><el-col :span="24"><div class="grid-content2"></div></el-col></el-row>
                          <img
                          style="width: 100px; height: 100px; border-radius: 50px"
                          src="../assets/exp.jpg"
                          ></img>
                        </el-col>
                        
                        <el-col :span="20" class="grid-content bg-purple-light">  
                          <el-row >
                            <el-col :span="16" class="grid-content bg-purple-light">
                              <el-link href="https://element.eleme.io" target="_blank"><h3>{{exp.name}}</h3></el-link>
                            </el-col>
                            <el-col :span="1" class="grid-content bg-purple-light" :offset="7">
                                <el-button type="warning" icon="el-icon-star-off" circle @click="star" size="small"></el-button>
                            </el-col>
                          </el-row>
                        
                          <el-row>
                              <el-col :span="4" class="grid-content bg-purple-light"><i class="el-icon-s-cooperation"> 机构:</i></el-col>
                              <el-col :span="20"><div class="grid-content bg-purple-light">{{ exp.inst }}</div></el-col>
                          </el-row>

                          <el-row>
                              <el-col :span="4" class="grid-content bg-purple-light redfont">#h-index: </el-col>
                              <el-col :span="3"><div class="grid-content bg-purple-light">{{ exp.hindex }} <el-divider direction="vertical"></el-divider></div></el-col>
                              
                              <el-col :span="4" class="grid-content bg-purple-light redfont">#g-index: </el-col>
                              <el-col :span="3"><div class="grid-content bg-purple-light">{{ exp.gindex }} <el-divider direction="vertical"></el-divider></div></el-col>
                              
                              <el-col :span="4" class="grid-content bg-purple-light redfont">论文数: </el-col>
                              <el-col :span="3"><div class="grid-content bg-purple-light">{{ exp.papercnt }}</div></el-col>
                          </el-row>
                          
                        </el-col>  
                      </el-row>  
                      </el-card>
                    <el-divider></el-divider>
                  </el-row>

                      <el-pagination
                        background
                        layout="prev, pager, next"
                        :total="total"
                        :page-size="pagesize"
                        :hide-on-single-page=true
                        @current-change="current_change">
                      </el-pagination>
                </el-tab-pane>
              </el-tabs>

              
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
        //tab
        activeName: 'first',
        //分页
        total:2, //总条目数
        pagesize:10, //每页条目数
        currentPage:1, //当前所在页

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
        pubyear:1999,
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
        pubyear:2000,
        refcnt:66,
        readcnt:666,
      }
      ],
        //专家信息
        explist:[{
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
      //切换tab
      handleClick(tab, event) {
        // console.log(tab, event);
        console.log(this.activeName);
      },
      //换页
      current_change:function(currentPage){
        this.currentPage = currentPage;
      },
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
      },
      //高级检索（待定）
      advsearch() {
        console.log("高级检索:"+this.input2);
      },

      //标题跳转
      topv() {
        this.$router.push({ path:'/pv'  }); //跳转至pv
      },
    }
}
</script>

<style scoped>

.main-con1{
  width:80%;
  margin:0 auto;
}

.main-con2{
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
    margin-bottom: 10px;
  }
  /* p:last-child {
      margin-bottom: 0;
    } */

  .el-col {
    border-radius: 4px;
    line-height:30px;
    
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
  .grid-content2 {
    min-height: 20px;
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

  /* 评论row */
.comm{
  margin-bottom: 5px;
  text-align: left;
}

.papercard{
  margin-bottom: 0px;
}
</style>