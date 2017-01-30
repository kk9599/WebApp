/*
* Bootstrap and frontAwesome
* import 'bootstrap/dist/js/bootstrap.min.js'
* import 'bootstrap/dist/css/bootstrap.min.css'
* */
import 'jquery/dist/jquery.slim.min.js'
import 'font-awesome/css/font-awesome.css'





/*
* Vue
* */


import Vue from 'vue'

import VueResource from 'vue-resource'
Vue.use(VueResource)


/*
* Vue Router
* */
import VueRouter from 'vue-router'
import routers from './routers'
Vue.use(VueRouter)

/*
* Vuex
*
* */
import store from './vuex/store.js'



let app = require('./App.vue')
//app.router = new VueRouter(routers)

//new Vue(app).$mount('#app')
const router= new VueRouter(routers)
new Vue(Vue.util.extend({ router,store }, app)).$mount('#app')