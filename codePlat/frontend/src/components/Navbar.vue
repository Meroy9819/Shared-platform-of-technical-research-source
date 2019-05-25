<template>
    <nav class="navbar is-primary is-fixed-top"  role="navigation" aria-label="main navigation">
        <div class="container">
            <div class="navbar-brand">
                <div class="navbar-burger burger" v-bind:class="{'is-active':isActive}" data-target="navbar-main" @click="toggle">
                    <span></span>
                    <span></span>
                    <span></span>
                </div>
                </div>
                <div id="navbar-main" class="navbar-menu" @click="closeMenu"  v-bind:class="{'is-active':isActive}">
                    <div class="navbar-start">
                      <router-link class="navbar-item" to="/ExpertSearch">学术圈</router-link>

                          <router-link v-if="user.status>=3" class="navbar-item" to="/ExpertInfo">我的门户</router-link>
                       
                        <router-link v-if="user.status>=0" class="navbar-item" to="/info">我的资料</router-link>
                        <router-link v-if="user.status>=4" class="navbar-item" to="/admin">管理</router-link>

                    </div>

                    <div class="navbar-end" v-bind:class="{'is-active':isActive}">
                        <div v-if="isSignedin" class="navbar-item">
                            {{user.name}},欢迎您
                        </div>
                        <div class="navbar-item">
                        <div class="field is-grouped">
                            <p class="control" v-if="!isSignedin" @click="toggleSignInModal">
                                <a class="bd-tw-button button is-info" >
                                    <span class="icon"></span>
                                    <span>登录</span>
                                </a>
                            </p>
                            <p class="control" v-if="!isSignedin" @click="toggleSignUpModal">
                                <a class="bd-tw-button button is-primary" >
                                    <span class="icon"></span>
                                    <span>注册</span>
                                </a>
                            </p>
                            <p class="control" @click="signOut"  v-if="isSignedin">
                                <a class="bd-tw-button button is-info" >
                                <span class="icon"></span>
                                <span>登出</span>
                                </a>
                            </p>
                        </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="modal" v-bind:class="{'is-active':showSigninModal}">
                <div class="modal-background"></div>
                <div class="modal-card">
                    <header class="modal-card-head">
                        <p class="modal-card-title">登录</p>
                        <button @click="toggleSignInModal" class="delete" aria-label="close"></button>
                    </header>
                    <section class="modal-card-body">
                        <div class="field">
                            <p class="control has-icons-left has-icons-right">
                                <label class="label">用户名</label>
                                <input v-model="userName" class="input" type="text" placeholder="用户名">
                                <span class="icon is-small is-left">
                                    <i class="fas fa-envelope"></i>
                                </span>
                                <span class="icon is-small is-right">
                                    <i class="fas fa-check"></i>
                                </span>
                            </p>
                        </div>
                        <div class="field">
                            <p class="control has-icons-left">
                                <label class="label">密码</label>
                                <input  v-model="password" class="input" type="password" placeholder="Password">
                                <span class="icon is-small is-left">
                                    <i class="fas fa-lock"></i>
                                </span>
                            </p>
                        </div>
                        </section>
                        <footer class="modal-card-foot">
                        <button class="button is-success" @click="signIn" >登录</button>
                        <button class="button is-primary" @click="toggleSignUpModal" >注册</button>
                        <button class="button" @click="toggleSignInModal">取消</button>
                        </footer>
                    </div>
                </div>
                <div class="modal" v-bind:class="{'is-active':showSignupModal}">
                    <div class="modal-background"></div>
                    <div class="modal-card">
                        <header class="modal-card-head">
                        <p class="modal-card-title">注册</p>
                        <button @click="toggleSignUpModal" class="delete" aria-label="close"></button>
                        </header>
                        <section class="modal-card-body">
                            <div class="field">
                                <p class="control has-icons-left has-icons-right">
                                    <label class="label">用户名</label>
                                    <input v-model="signupForm.userName" class="input" type="text" placeholder="请在此处填写用户名">
                                    <span class="icon is-small is-left">
                                    <i class="fas fa-envelope"></i>
                                    </span>
                                    <span class="icon is-small is-right">
                                    <i class="fas fa-check"></i>
                                    </span>
                                </p>
                            </div>
                            <div class="field">
                                <p class="control has-icons-left">
                                    <label class="label">密码</label>
                                    <input  v-model="signupForm.password" class="input" type="password" placeholder="请在此处填写密码">
                                    <span class="icon is-small is-left">
                                    <i class="fas fa-lock"></i>
                                    </span>
                                </p>
                            </div>
                            <div class="field">
                                <p class="control has-icons-left">
                                    <label class="label">重复密码</label>
                                    <input  v-model="signupForm.password2" class="input" type="password" placeholder="请在此处重复一遍密码">
                                    <span class="icon is-small is-left">
                                    <i class="fas fa-lock"></i>
                                    </span>
                                </p>
                            </div>
                            <div class="field">
                                <p class="control has-icons-left">
                                    <label class="label">电话</label>
                                    <input  v-model="signupForm.tel" class="input" type="text" placeholder="请在此处填写电话号码">
                                    <span class="icon is-small is-left">
                                    <i class="fas fa-lock"></i>
                                    </span>
                                </p>
                            </div>
                            <div class="field">
                                <p class="control has-icons-left">
                                    <label class="label">E-mail</label>
                                    <input  v-model="signupForm.email" class="input" type="email" placeholder="请在此处填写电子邮箱">
                                    <span class="icon is-small is-left">
                                    <i class="fas fa-lock"></i>
                                    </span>
                                </p>
                            </div>
                        </section>
                        <footer class="modal-card-foot">
                        <button class="button is-success" @click="signUp" >注册</button>
                        <button class="button" @click="toggleSignUpModal">取消</button>
                        </footer>
                    </div>
                </div>
            </nav>

</template>

<script>
export default {
    data() {
      return {
        
      }
    }
}
</script>

<style scoped>
#header {
    margin-top:0px;
    height: 60px;
    text-align: center;
    vertical-align: middle;
    line-height: 60px;
}
.box-card {
    width: 480px;
    height:200px;
    margin:0 auto;
  }
</style>