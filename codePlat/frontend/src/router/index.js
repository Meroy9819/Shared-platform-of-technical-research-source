import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import Login from '@/components/Login/Login'
import Register from '@/components/Register/Register'
import Paperview from '@/components/Paperview'
import Header from '@/components/Header'
import SearchResult from '@/components/SearchResult'
import indexx from '@/components/indexx'
// import test from '@/components/test'

import ExpertInfo from '@/components/ExpertInfo/ExpertInfo'
import UserInfo from '@/components/UserInfo/UserInfo'
// import Certificate from '@/components/Certificate/Certificate'
import Administrator from '@/components/Administrator/Administrator'

Vue.use(Router);

export default new Router({
  routes: [
    // {
    //   path: '/',
    //   name: 'Login',
    //   component: Login
    // },
    // {
    //   path: '/',
    //   name: 'Register',
    //   component: Register
    // }
    {
      path: '/',
      name: 'index',
      component: indexx
    },
    {
      path: '/Paperview',
      name: 'Paperview',
      component: Paperview
    },
    {
      path: '/SearchResult',
      name: 'SearchResult',
      component: SearchResult
    },
    // {
    //   path: '/t',
    //   name: 'test',
    //   component: test
    // },
    {
      path:'/Login',
      name:'Login',
      meta:{
        requireAuth: false
      },
      component:Login
    },
    {
      path:'/Register',
      name:'Register',
      meta:{
        requireAuth: false
      },
      component:Register
    },
    {
      path:'/ExpertInfo',
      name:'ExpertInfo',
      meta:{
        requireAuth: false
      },
      component:ExpertInfo
    },
    {
      path:'/UserInfo',
      name:'UserInfo',
      meta:{
        requireAuth: false
      },
      component:UserInfo
    },
    // {
    //   path:'/Certificate',
    //   name:'Certificate',
    //   meta:{
    //     requireAuth: false
    //   },
    //   component:Certificate
    // },
    {
      path:'/Administrator',
      name:'Administrator',
      meta:{
        requireAuth: false
      },
      component:Administrator
    }
  ]
})
