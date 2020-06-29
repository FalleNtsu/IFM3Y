<template>
  <v-timeline :dense="$vuetify.breakpoint.smAndDown">
    <template v-for="(prevMood, i) in this.prevMoods">
      <v-timeline-item
        :key="i"
        v-if="i % 2 === 0"
        color="red lighten-2"
        fill-dot
        right
      >
        <v-card>
          <v-card-title class="red lighten-2">
            <v-icon dark size="42" class="mr-4">
              mdi-magnify
            </v-icon>
            <h2 class="display-1 white--text font-weight-light">
              {{ formatDate(prevMood.logged_time) }} -
              {{ prevMood.generic_mood.name }}
            </h2>
          </v-card-title>
          <v-container>
            <v-row>
              <v-col cols="12" md="10">
                <h2>{{ prevMood.description }}</h2>
              </v-col>
              <v-col class="hidden-sm-and-down text-right" md="2">
                <v-icon size="64">mdi-calendar-text</v-icon>
              </v-col>
            </v-row>
          </v-container>
        </v-card>
      </v-timeline-item>

      <v-timeline-item :key="i" v-else color="primary lighten-2" fill-dot left>
        <v-card>
          <v-card-title class="primary lighten-2">
            <v-icon dark size="42" class="mr-4">
              mdi-magnify
            </v-icon>
            <h2 class="display-1 white--text font-weight-light">
              {{ formatDate(prevMood.logged_time) }} -
              {{ prevMood.generic_mood.name }}
            </h2>
          </v-card-title>
          <v-container>
            <v-row>
              <v-col cols="12" md="10">
                <h2>{{ prevMood.description }}</h2>
              </v-col>
              <v-col class="hidden-sm-and-down text-right" md="2">
                <v-icon size="64">mdi-calendar-text</v-icon>
              </v-col>
            </v-row>
          </v-container>
        </v-card>
      </v-timeline-item>
    </template>
  </v-timeline>
</template>

<script>
import DateHelper from "@/helpers/date.helper";
import moodService from "@/services/mood.service";
import { mapState } from "vuex";
// import MoodService from "../../services/mood.service"
export default {
  props: { username: { type: String, required: true } },
  data() {
    return {
      prevMoods: [],
      // TODO Implement Mood Types for the icons and colors of each timeline
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
    }),
    odd: function() {
      return this.prevMoods.filter(function(item) {
        if (item.id % 2 === 0) {
          return item.id;
        }
      });
    },
    even: function() {
      return this.prevMoods.filter(function(item) {
        if (item.id % 2 !== 0) {
          return item.id + 1;
        }
      });
    }
  },
  methods: {
    formatDate: function(date) {
      return DateHelper.formatDate(date);
    }
  },

  async created() {
    await moodService.getPreviousMoods(this.username).then(
      respData => {
        this.prevMoods = respData.payload;
        console.log(this.prevMoods);
      },
      err => {
        console.log("====================================");
        console.log(err);
        console.log("====================================");
      }
    );
  }
};
</script>
<style scoped>
.icon {
  font-size: 100px;
  color: rgb(170, 197, 13);
}

.angry {
  color: crimson;
}
.neutral {
  color: indigo;
}
.sad {
  color: rgb(21, 21, 121);
}
.awful {
  color: grey;
}
.good {
  color: green;
}
.v-card {
  margin: 2%;
}
.heading {
  position: relative;
  left: 35%;
}
</style>
