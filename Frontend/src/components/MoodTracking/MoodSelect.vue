<template>
  <v-container>
    <div>
      <h1>How Are You Feeling Today</h1>
      <v-row>
        <v-col>
          <v-menu
            ref="menu1"
            v-model="menu1"
            :close-on-content-click="false"
            transition="scale-transition"
            offset-y
            max-width="290px" 
          >
            <template v-slot:activator="{ on }">
              <v-text-field
                v-model="dateFormatted"
                label="Date"
                @blur="date = parseDate(dateFormatted)"
                v-on="on"
              ></v-text-field>
            </template>
            <v-date-picker v-model="date" no-title @input="menu1 = false"></v-date-picker>
          </v-menu>
        <v-row>
          <!-- <moodIcons ></moodIcons> -->
        </v-row>
        </v-col>
      </v-row>
    </div>
  </v-container>
</template>

<script>
// import moodIcons from "@/components/MoodTracking/Mood";
export default {
  data: vm => ({
    date: new Date().toISOString().substr(0, 10),
    dateFormatted: vm.formatDate(new Date().toISOString().substr(0, 10)),
    menu1: false
  }),
  components: {
    // moodIcons
  },
  computed: {
    computedDateFormatted() {
      return this.formatDate(this.date);
    }
  },
  watch: {
    date() {
      this.dateFormatted = this.formatDate(this.date);
    }
  },

  methods: {
    formatDate(date) {
      if (!date) return null;
      const [year, month, day] = date.split("-");
      return `${day}/${month}/${year}`;
    },
    parseDate(date) {
      if (!date) return null;
      const [day, month, year] = date.split("/");
      return `${year}-${month.padStart(2, "0")}-${day.padStart(2, "0")}`;
    }
  }
};
</script>
<style scoped>
/* .container {
  position: relative;

  bottom: 70px;
  padding: 5%;
  left: 10%;
}
h1 {
  position: relative;
  left: 200px;
}
.row {
  position: relative;

  left: 200px;
}
.moodIcons {
  position: relative;
  color: blue;
  top: 50px;
}
.tHi {
  position: relative;
  right: 20%; */
/* } */
</style>
