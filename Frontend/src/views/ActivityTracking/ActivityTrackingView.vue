<template>
  <div class="home">
    <v-container>
      <v-row class="mb-6">
        <v-col :cols="6">
          <v-card class="pa-2" elevation="8">
            <v-card-title class="headline font-weight-bold">
              Assigned Activities
            </v-card-title>
            <v-container fluid>
              <v-row dense>
                <v-col
                  v-for="assignedActivity in assignedActivities"
                  :key="assignedActivity.activity.id"
                  cols="12"
                >
                  <v-card dark color="indigo">
                    <v-card-title>
                      <span class="title">
                        {{ assignedActivity.activity.activity_type.name }}
                      </span>
                    </v-card-title>

                    <v-card-text class="headline font-weight-bold">
                      <v-row>
                        <v-col>
                          {{ assignedActivity.activity.name }}
                        </v-col>
                        <v-col class="text-end" cols="auto">
                          Due Date:
                          {{ formatDate(assignedActivity.due_date) }}
                        </v-col>
                      </v-row>
                    </v-card-text>

                    <v-card-actions>
                      <v-spacer></v-spacer>
                      <router-link
                        :to="{
                          name: 'SpecificActivity',
                          params: { id: assignedActivity.id }
                        }"
                      >
                        <v-btn color="primary">View</v-btn>
                      </router-link>
                    </v-card-actions>
                  </v-card>
                </v-col>
              </v-row>
            </v-container>
          </v-card>
        </v-col>

        <v-col :cols="6">
          <v-card class="pa-2" elevation="8" outlined>
            <v-card-title class="headline font-weight-bold">
              Completed Activities
            </v-card-title>
            <v-container fluid>
              <v-row dense>
                <v-col
                  v-for="completedActivity in completedActivities"
                  :key="completedActivity.activity.id"
                  cols="12"
                >
                  <v-card dark>
                    <v-card-title>
                      <span class="title">
                        {{ completedActivity.activity.activity_type.name }}
                      </span>
                    </v-card-title>

                    <v-card-text class="headline font-weight-bold">
                      <v-row>
                        <v-col>
                          {{ activity.name }}
                        </v-col>
                        <v-col class="text-end" cols="auto">
                          Due:
                          {{ completedActivity.due_date }}
                        </v-col>
                      </v-row>
                    </v-card-text>

                    <v-card-actions>
                      <v-spacer></v-spacer>
                      <router-link
                        :to="{
                          name: 'SpecificActivity',
                          params: { id: completedActivity.activity.id }
                        }"
                      >
                        <v-btn color="primary">View</v-btn>
                      </router-link>
                    </v-card-actions>
                  </v-card>
                </v-col>
              </v-row>
            </v-container>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
// @ is an alias to /src
// import HelloWorld from "@/components/HelloWorld.vue";
import activityService from "@/services/activity.service";
import DateHelper from "@/helpers/date.helper";

import { mapState } from "vuex";
import { ROLE_PATIENT } from "@/store/user.type";

export default {
  name: "ActivityTracking",
  components: {},
  data() {
    return {
      ROLE_PATIENT: ROLE_PATIENT,
      completedActivities: [],
      assignedActivities: []
    };
  },
  computed: {
    ...mapState({
      user: state => state.user
    })
  },
  async created() {
    // If the user is not logged in and if the user is not a patient

    // Get the assigned activities for a specific user using their username
    // Store the result of this into an array
    await activityService
      .getAssignedActivities(this.user.details.username)
      .then(
        respData => {
          this.assignedActivities = respData;
        },
        err => {
          console.log("====================================");
          console.log(err);
          console.log("====================================");
        }
      );

    // Get the completed activities for a specific user using their username
    // Store the result of this into an array
    await activityService
      .getCompletedActivities(this.user.details.username)
      .then(
        respData => {
          this.completedActivities = respData;
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
