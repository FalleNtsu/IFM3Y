<template>
 <v-container grid-list-xl class= 'justify-center '>
     <MoodSelection> </MoodSelection>
     <DefaultMoods></DefaultMoods>
     <!-- <Selector  class="justify-center"></Selector> -->
     <!-- <List> </List> -->
     <!-- <v-btn @click="change()">{{btnMessage}}</v-btn> -->
     <!-- <component v-bind:is="component" class="justify-center"></component> -->
     
 </v-container>   
</template>
<script>
// import List from "../../components/MoodTracking/ListMoods";
import DefaultMoods from "@/components/MoodTracking/Mood";
import MoodSelection from "../../components/MoodTracking/MoodSelect"
export default {
      components:{
        MoodSelection,
        DefaultMoods
        // List

    },
    data(){
        return{
component:'S',
btnMessage:"View Previous Moods"
        }
    },
  
    methods:{
change(){
if(this.component==='S'){
this.component='L'
this.btnMessage="Add Mood"
}else if(this.component==='L'){
    this.component='S'
    this.btnMessage="View Previous Moods"
}
}
    }

}
</script>