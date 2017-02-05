<template>
    <div>
        <el-menu theme="dark" default-active="1" class="el-menu-demo" mode="vertical" @select="handleSelect" :router= "true">
            <el-menu-item index="1">处理中心</el-menu-item>
            <el-submenu index="2">
                <template slot="title">我的工作台</template>
                <el-menu-item index="/home">home</el-menu-item>
                <el-menu-item index="/login">login</el-menu-item>
                <el-menu-item index="/task">task</el-menu-item>
            </el-submenu>
            <el-menu-item index="3"><a href="https://www.ele.me" target="_blank">订单管理</a></el-menu-item>
        </el-menu>
<<<<<<< HEAD

=======
       
>>>>>>> a4675f5188287c1fbcb5a86f10d7b744abb444ee
    </div>
</template>


<script>
    export default {
        data(){

            return{



            }

        },

        methods: {
            handleSelect(key, keyPath) {
                console.log(key, keyPath);
            }


        }
    }
</script>