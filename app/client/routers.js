/**
 * Created by admin on 2016-12-26.
 */
import home from './components/pages/home/home.vue'
import about from './components/pages/about/about.vue'
import login from './components/pages/login/login.vue'
import task from './components/common/task/task.vue'
export default {
    hashbang: false,
    linkActiveClass: 'active',
    transitionOnLoad: true,

    routes: [
        {
            path: '/home',
            component: home

        },
        {
            path: '/about',
            component: about

        },
        {
            path: '/login',
            component: login

        },
        {
            path: '/task',
            component: task

        }
    ]

}





