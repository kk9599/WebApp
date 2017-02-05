<template>
<ul>
    <li v-for="item  in tasks">
        {{item}}
    </li>

</ul>

</template>

<script>

    export default {
        data(){
            return {

                tasks: ['Do the dishes',
                    'Take out the trash',
                    'Mow the lawn'


                ]

            }


        }


    }

</script>