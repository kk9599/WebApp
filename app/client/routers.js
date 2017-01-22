/**
 * Created by admin on 2016-12-26.
 */
import home from './components/pages/home/home.vue'
import about from './components/pages/about/about.vue'


export default {

    linkActiveClass: 'active',
    routes:[
    {
        path:'/home',
        component: home


    },
    {
        path:'about',
        component: about

    }


]

}





