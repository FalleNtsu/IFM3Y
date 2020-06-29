<template>
  <div class="home">
    <v-container>
      <v-row justify="center" class="mb-6">
        <v-col :cols="6">
          <div v-if="!activityData">
            No Activity
          </div>
          <div v-else>
            <div v-if="activityData.isCompleted">
              <CompletedActivityDetails
                :completedActivity="activityData"
              ></CompletedActivityDetails>
            </div>
            <div v-else-if="!activityData.isCompleted">
              <AssignedActivityDetails
                :assignedActivity="activityData"
              ></AssignedActivityDetails>
            </div>
          </div>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
// @ is an alias to /src
// import HelloWorld from "@/components/HelloWorld.vue";
import activityService from "@/services/activity.service";
import CompletedActivityDetails from "@/components/ActivityTracking/CompletedActivityDetails";
import AssignedActivityDetails from "@/components/ActivityTracking/AssignedActivityDetails";

import { mapState } from "vuex";
import { ROLE_PATIENT } from "@/store/user.type";

export default {
  name: "SpecificActivity",
  components: {
    CompletedActivityDetails,
    AssignedActivityDetails
  },
  data() {
    return {
      id: 0,
      ROLE_PATIENT: ROLE_PATIENT,
      activityData: null
    };
  },
  computed: {
    ...mapState({
      user: state => state.user
    })
  },
  async created() {
    this.id = this.$route.params.id;
    // Get the assigned activities for a specific user using their username
    // Store the result of this into an array
    await activityService
      .getSpecificActivity(this.user.details.username, this.id)
      .then(
        respData => {
          this.activityData = respData;
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
