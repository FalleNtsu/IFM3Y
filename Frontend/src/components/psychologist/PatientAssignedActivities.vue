<template>
  <v-container fluid>
    <h3>Current assigned activities</h3>
    <v-row dense>
      <v-col
        v-for="assignedActivity in assignedActivities"
        :key="assignedActivity.id"
        cols="12"
      >
        <v-card dense dark>
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
            <v-row>
              <v-col>
                <v-btn
                  @click="unassignActivity(assignedActivity.id)"
                  color="red"
                  type="submit"
                  block
                  rounded
                >
                  Unasign activity
                </v-btn>
              </v-col>
            </v-row>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import ActivityService from "@/services/activity.service";
import DateHelper from "@/helpers/date.helper";

export default {
  name: "PatientAssignedActivities",
  data() {
    return { assignedActivities: [] };
  },
  props: { username: { type: String, required: true } },
  computed: {},
  methods: {
    formatDate: function(date) {
      return DateHelper.formatDate(date);
    },
    unassignActivity: async function(activityID) {
      ActivityService.unassignActivity(activityID);
      this.assignedActivities = this.assignedActivities.filter(function(obj) {
        return obj.id != activityID;
      });
    }
  },
  async created() {
    await ActivityService.getAssignedActivities(this.username).then(
      respData => {
        this.assignedActivities = respData;
        console.log("====================================");
        console.log(respData);
        console.log("====================================");
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
