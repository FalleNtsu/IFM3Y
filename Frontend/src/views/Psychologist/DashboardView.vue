<template>
  <div class="home">
    <v-container>
      <v-row class="mb-6">
        <v-col>
          <graphCard name="Patients Added"></graphCard>
        </v-col>

        <v-col>
          <graphCard name="Mood useage"></graphCard>
        </v-col>

        <v-col>
          <graphCard name="Medication useage"></graphCard>
        </v-col>
        <v-col>
          <graphCard name="Activtiy useage"></graphCard>
        </v-col>
      </v-row>

      <v-row class="mb-6">
        <v-col>
          <router-link to="/psychologist/patient">
            <v-btn color="primary mt-6" type="submit" x-large block rounded>
              View All Patients
            </v-btn>
          </router-link>
        </v-col>
        <v-col>
          <router-link to="/patients">
            <v-btn color="primary mt-6" type="submit" x-large block rounded>
              Add patient
            </v-btn>
          </router-link>
        </v-col>
        <v-col>
          <router-link to="/psychologist/activities">
            <v-btn color="primary mt-6" type="submit" x-large block rounded>
              Activities
            </v-btn>
          </router-link>
        </v-col>
        <v-col>
          <router-link to="/patients">
            <v-btn color="primary mt-6" type="submit" x-large block rounded>
              Medications
            </v-btn>
          </router-link>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
import DateHelper from "@/helpers/date.helper";
import graphCard from "@/components/dashboard/graphCard";

import { mapState } from "vuex";

export default {
  name: "Dashboard",
  components: { graphCard },
  data() {
    return {};
  },
  computed: {
    ...mapState({
      user: state => state.user
    })
  },
  async created() {},
  methods: {
    formatDate: function(date) {
      return DateHelper.formatDate(date);
    }
  }
};
</script>
