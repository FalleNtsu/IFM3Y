<template>
  <v-container>
    <v-card>
      <v-card-title>
        Activities
        <v-spacer></v-spacer>
        <v-text-field
          v-model="search"
          append-icon="mdi-magnify"
          label="Search"
          single-line
          hide-details
        ></v-text-field>
      </v-card-title>

      <v-data-table
        :items="activities"
        :headers="headers"
        item-key="id"
        show-select
        single-select
      ></v-data-table>
    </v-card>
    <v-btn class="mt-5" color="primary" rounded="" block>Add Activity</v-btn>
  </v-container>
</template>

<script>
import ActivityService from "@/services/activity.service";
import DateHelper from "@/helpers/date.helper";

import { mapState } from "vuex";

export default {
  name: "Patients",
  components: {},
  data() {
    return {
      activities: [],
      search: "",
      headers: [
        {
          text: "id",
          align: "start",
          sortable: false,
          value: "id"
        },
        { text: "Name", value: "name" },
        { text: "description", value: "description" },
        { text: "proof_type", value: "proof_type" },
        { text: "activity_type", value: "activity_type" }
      ]
    };
  },
  computed: {
    ...mapState({
      user: state => state.user
    })
  },
  async created() {
    await ActivityService.getActivities().then(
      respData => {
        this.activities = respData;

        console.log("====================================");
        console.log(this.activities);
        console.log("====================================");
        for (let i = 0; i < this.activities.length; i++) {
          this.activities[i].proof_type = this.activities[i].proof_type.name;
          this.activities[i].activity_type = this.activities[
            i
          ].activity_type.name;
        }
      },
      err => {
        console.log("====================================");
        console.log(err);
        console.log("====================================");
      }
    );
  },
  methods: {
    formatDate: function(date) {
      return DateHelper.formatDate(date);
    }
  }
};
</script>
