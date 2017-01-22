/**
 * Created by admin on 2016-12-30.
 */
import Vue from 'vue';
import Vuex from 'vuex';
import count from './modules/count.js'


Vue.use(Vuex);

export default new Vuex.Store({


    modules:{
        count,

    }

});