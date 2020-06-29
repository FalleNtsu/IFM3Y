<template>
  <v-container >
    <v-row>
<v-col> <p>Organizing your schedule <br> Letting you to focus better</p>

</v-col>
  <v-col>
    <v-img height="40%" width="250"  aspect-ratio="0.5" src="../images/Brain.jpg" ></v-img>
    </v-col>
    <v-col>
      <p> Track your Moods, Medication<br> and Activities all in one place</p>
      </v-col>
    </v-row> 
    <v-row class="A">
      <v-col>
        <v-icon class="homeIcon"> mdi-pill</v-icon>
        </v-col>
        <v-col>
          <p>Cake or pie? I can tell a lot about you by which one you pick. It may seem silly, but cake people and pie people are really different. I know which one I hope you are, but that's not for me to decide. So, what is it? Cake or pie?
It's always good to bring a slower friend with you on a hike. If you happen to come across bears, the whole group doesn't have to worry. Only the slowest in the group do. That was the lesson they were about to learn that day.</p>
        </v-col>
      </v-row>
      <v-row class="A">
      <v-col>
        <v-icon class="homeIcon"> mdi-emoticon-happy</v-icon>
        </v-col>
        <v-col>
          <p>Cake or pie? I can tell a lot about you by which one you pick. It may seem silly, but cake people and pie people are really different. I know which one I hope you are, but that's not for me to decide. So, what is it? Cake or pie?
It's always good to bring a slower friend with you on a hike. If you happen to come across bears, the whole group doesn't have to worry. Only the slowest in the group do. That was the lesson they were about to learn that day.</p>
        </v-col>
      </v-row>
      <v-row class="A">
      <v-col>
        <v-icon class="homeIcon"> mdi-clipboard-list</v-icon>
        </v-col>
        <v-col>
          <p>Cake or pie? I can tell a lot about you by which one you pick. It may seem silly, but cake people and pie people are really different. I know which one I hope you are, but that's not for me to decide. So, what is it? Cake or pie?
It's always good to bring a slower friend with you on a hike. If you happen to come across bears, the whole group doesn't have to worry. Only the slowest in the group do. That was the lesson they were about to learn that day.</p>
        </v-col>
      </v-row>
  </v-container>
</template>

<script>
// @ is an alias to /src
//import HelloWorld from "@/components/HelloWorld.vue";
//import c from "../components/general/carouselView"
//import imgBrain from "../images/Brain.svg"
export default {
  name: "Home",
  components: {
    
  //  c
  }
};
</script>
<style scoped>
.container{
  position: relative;
  top:5%
}
.homeIcon{
  font-size: 200px;
  color:rgb(87, 189, 192);
}
.A{
  position: relative;
  bottom:145px;
}

</style>