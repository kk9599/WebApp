import * as types from '../mutation-types.js'

//inital state
const state = {
    count: 0
}

// getters are functions
const getters = {
    evenOrOdd: state => state.count % 2 === 0 ? 'even' : 'odd'
}

const actions = {
    increment: ({commit}) => commit(types.INCREMENT),
    decrement: ({commit}) => commit(types.DECREMENT),
    incrementIfOdd ({commit, state}) {
        if ((state.count + 1) % 2 === 0) {
            commit(types.INCREMENT)
        }
    },
    incrementAsync ({commit}) {
        return new Promise((resolve, reject) => {
            setTimeout(() => {
                commit(types.INCREMENT)
                resolve()
            }, 1000)
        })
    }


}

const mutations = {

      [types.DECREMENT] (state){
        state.count--
    },

       [types.INCREMENT] (state){
        state.count++
    }



}


export default {
    state,
    getters,
    actions,
    mutations
}