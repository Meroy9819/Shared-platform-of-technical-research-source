import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import Login from '@/components/Login'
import Register from '@/components/Register'
import Navbar from '@/components/Navbar'
import Paperview from '@/components/Paperview'
import Header from '@/components/Header'
import test from '@/components/test'


Vue.use(Router);

export default new Router({
  // mode: 'history',
  routes: [
    {
      path: '/login',
      name: 'Login',
      component: Login
    },
    {
      path: '/register',
      name: 'Register',
      component: Register
    },

    {
      path: '/paperview',
      name: 'Paperview',
      component: Paperview
    },

    {
      path: '/test',
      name: 'test',
      component: test
    },


  ]

})
