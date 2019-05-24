import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import Login from '@/components/Login'
import Register from '@/components/Register'
import Navbar from '@/components/Navbar'
import Paperview from '@/components/Paperview'
import Header from '@/components/Header'
import SearchResult from '@/components/SearchResult'


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
      name: 'Paperview',
      component: Paperview
    }
  ]
})
