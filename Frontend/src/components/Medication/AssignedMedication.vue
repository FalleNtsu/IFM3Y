<template>
  <v-container>
    <v-card v-for="(med,m) in this.Patientmedication" :key="m" class="pa-2 mt-5" elevation="8">
      <v-card-title :key="m" class="headline">
        {{ med.medication.medication_name }}
        <v-spacer></v-spacer>
        Dosage Time: Every {{ med.dosage_time_hours }} Hours
      </v-card-title>
      <v-card-text>
        <p>
          <v-row>
            <v-col cols="auto">Dosage:</v-col>
            <v-col>{{ med.dosage }}</v-col>
          </v-row>
          <v-row>
            <v-col cols="auto">Medication Instructions :</v-col>
            <v-col>{{ med.instructions }}</v-col>
          </v-row>
          <!-- <v-row>
          <v-col cols="auto">Personal Description:</v-col>
          <v-col>
            {{ assignedActivity.description }}
          </v-col>
          </v-row>-->
        </p>
        <v-divider></v-divider>
        <br />
      </v-card-text>
      <v-row>
        <v-col>
          <router-link to="/medication/taken" style="text-decoration : none ">
            <v-btn color="primary" right block rounded>Take Medication</v-btn>
          </router-link>
        </v-col>
      </v-row>
    </v-card>
    <v-spacer></v-spacer>
  </v-container>
</template>

<script>
import DateHelper from "@/helpers/date.helper";
import MedicationService from "@/services/medication.service";
import { mapState } from "vuex";
export default {
  name: "PatientMedication",
  components: {},
  data() {
    return {
      Patientmedication: [],
      TakenMeds: []
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
    await MedicationService.getPatientMedication(
      this.user.details.username
    ).then(
      respData => {
        this.Patientmedication = respData.payload;
        console.log(respData);
      },
      err => {
        console.log("====================================");
        console.log(err);
        console.log("====================================");
      }
    );

    // Get the completed activities for a specific user using their username
    // Store the result of this into an array
    await MedicationService.PatientTakenMeds(this.user.details.username).then(
      respData => {
        this.TakenMeds = respData;
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
