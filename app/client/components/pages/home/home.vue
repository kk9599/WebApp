<template>

<<<<<<< HEAD

    <el-form :model="ruleForm2" :rules="rules2" ref="ruleForm2" label-width="120px" class="demo-ruleForm">
        <el-form-item label="Password" prop="pass">
            <el-input type="password" v-model="ruleForm2.pass" auto-complete="off"></el-input>
        </el-form-item>
        <el-form-item label="Confirm" prop="checkPass">
            <el-input type="password" v-model="ruleForm2.checkPass" auto-complete="off"></el-input>
        </el-form-item>
        <el-form-item label="Age" prop="age">
            <el-input v-model.number="ruleForm2.age"></el-input>
        </el-form-item>
        <el-form-item>
            <el-button type="primary" @click="submitForm('ruleForm2')">Submit</el-button>
            <el-button @click="resetForm('ruleForm2')">Reset</el-button>
        </el-form-item>
=======
<<<<<<< HEAD
    <p>this is home</p>

=======

   
>>>>>>> ebe08a2cfada2444c029fdafcdfd3047ad9d3f62
         <p>this is home</p>
    </el-form>
>>>>>>> a4675f5188287c1fbcb5a86f10d7b744abb444ee
</template>


<script>
    export default {

    data: function(){

    return {}
    }
    }



</script>