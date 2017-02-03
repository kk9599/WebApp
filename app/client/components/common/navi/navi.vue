<template>
    <div>
        <el-menu theme="dark" default-active="1" class="el-menu-demo" mode="vertical" @select="handleSelect" :router= route>
            <el-menu-item index="1">处理中心</el-menu-item>
            <el-submenu index="2">
                <template slot="title">我的工作台</template>
                <el-menu-item index="/home">home</el-menu-item>
                <el-menu-item index="2-2">选项2</el-menu-item>
                <el-menu-item index="2-3">选项3</el-menu-item>
            </el-submenu>
            <el-menu-item index="3"><a href="https://www.ele.me" target="_blank">订单管理</a></el-menu-item>
        </el-menu>
        <img src="/img/download.jpg">
    </div>
</template>


<script>
    export default {
        data(){

            return{
                route: true


            }

        },

        methods: {
            handleSelect(key, keyPath) {
                console.log(key, keyPath);
            }


        }
    }
</script>