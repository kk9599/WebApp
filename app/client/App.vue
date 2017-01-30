<template>
    <div>
        <headers></headers>
        <navi></navi>
        <div class="main">
            <counter></counter>
            <router-view></router-view>
        </div>
    </div>
</template>

<style lang="sass" scoped>
    $primary-color: #333;

    h1 {

        color: red;

    }


</style>

<script>

    import counter from './components/Counter.vue';
    import navi from './components/common/navi/navi.vue';
    import headers from './components/common/header/header.vue';

    export default{

        data(){
            return {
                msg: 'hello'

            }
        },
        components: {
           counter: counter,
           navi: navi,
           headers: headers

        },
        computed: {}


    };


</script>