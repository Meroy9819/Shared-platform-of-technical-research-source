import Vue from 'vue'
import Router from 'vue-router'
import Login from '@/components/Login/Login'
import Register from '@/components/Register/Register'
import Paperview from '@/components/Paperview'
import SearchResult from '@/components/SearchResult'
import indexx from '@/components/indexx'

import ExpertInfo from '@/components/ExpertInfo/ExpertInfo'
import UserInfo from '@/components/UserInfo/UserInfo'
import Administrator from '@/components/Administrator/Administrator'
import test from '@/components/test'

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/test',
      name: 'test',
      component: test
    },
    {
      path: '/',
      name: 'Index',
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
