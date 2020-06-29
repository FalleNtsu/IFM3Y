<template>
  <v-container>
    <v-col>
      <v-row>
        <template v-for="(mood,m) in defaultmoods">
          <v-card
            :key="m"
            class="mx-auto"
            color="white lighten-4"
            width="200px"
            height="200px"
            align="center"
            outlined="false"
            hover="20px"
          >
            <v-container>
              <v-icon
                :key="m"
                v-bind:class="mood.class"
                @click="setMood(mood.mood); setColor(mood.color)"
                size="125pt"
                :color="mood.color"
                :ripple="false"
              >{{mood.icon}}</v-icon>
            </v-container>
          </v-card>
        </template>
      </v-row>
    </v-col>

    <v-container class="text-center">
      <!-- <p>You feeling: {{this.mood}}</p> -->
      <v-row>
        <v-textarea
          v-model="description"
          label="Add A Description To Your Mood"
          name="description"
          auto-grow
          filled
          :color="this.color"
          rows="5"
        ></v-textarea>
      </v-row>

      <v-row>
        <v-flex class="left">
          <v-btn @click="addToDatase()" :color="this.color" width="300px" x-large rounded>Add</v-btn>
        </v-flex>
        <v-flex class="right">
          <router-link to="/mood/previous" style="text-decoration: none">
            <v-btn :color="this.color" width="300px" x-large rounded >Previous Moods</v-btn>
          </router-link>
        </v-flex>
      </v-row>
    </v-container>
  </v-container>
</template>
<script>
import { mapState } from "vuex";
import MoodService from "../../services/mood.service";
export default {
  data() {
    return {
      hover: false,
      mood: null,
      color: null,
      description: "",
      defaultmoods: [
        {
          mood: "Excellent",
          icon: "mdi-emoticon",
          color: "green"
        },
        { mood: "Happy", icon: "mdi-emoticon-happy", color: "yellow" },
        { mood: "Angry", icon: "mdi-emoticon-angry", color: "red" },
        { mood: "Meh", icon: "mdi-emoticon-neutral", color: "indigo" },
        { mood: "Sad", icon: "mdi-emoticon-sad", color: "blue" }
      ]
    };
  },
  computed: {
    ...mapState({
      user: state => state.user
    })
  },
  methods: {
    setMood(Mood) {
      this.mood = Mood;
    },
    setColor(Color) {
      this.color = Color;
    },

    async addToDatase() {
      let time = new Date();

      let rData = await MoodService.addPatientMood(
        this.user.details.username,
        this.mood,
        time,
        this.description
      );

      console.log(rData);
    }
  }
};
</script>
<style scoped>
.v-ripple__container {
  display: none !important;
}
</style>
