<template>
<v-container>
  <v-card v-for= "(med,m) in this.TakenMeds" :key = "m" class="pa-2 mt-5" elevation="8" >
    <v-card-title :key = "m" class="headline">
      {{ med.patients_medication.medication.medication_name}}
      <v-spacer></v-spacer>
      Taken At :  {{  formatDate(med.time_taken) }} 
    </v-card-title>
    <v-card-text>
      <p>
        <v-row>
          <v-col cols="auto"> Dosage: </v-col>
          <v-col>
            {{med.patients_medication.dosage }}
          </v-col>
        </v-row>
        <v-row>
          <v-col cols="auto">Medication Instructions :</v-col>
          <v-col>
            {{ med.patients_medication.instructions }}
          </v-col>
        </v-row>
        <!-- <v-row>
          <v-col cols="auto">Personal Description:</v-col>
          <v-col>
            {{ assignedActivity.description }}
          </v-col>
        </v-row> -->
      </p>
      <v-divider></v-divider>
      <br>
    </v-card-text>
    
  </v-card>
</v-container>
</template>

<script>

import DateHelper from "@/helpers/date.helper";
import MedicationService from "@/services/medication.service";
import {mapState} from 'vuex'
export default {
  name: "PatientMedication",
    components: {},
  data() {
    return {
        Patientmedication : [],
        TakenMeds : []
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
    await MedicationService
      .getPatientMedication(this.user.details.username)
      .then(
        respData => {
          this.Patientmedication = respData.payload;
          console.log(respData)
        },
        err => {
          console.log("====================================");
          console.log(err);
          console.log("====================================");
        }
      );

    // Get the completed activities for a specific user using their username
    // Store the result of this into an array
    await MedicationService
      .PatientTakenMeds(this.user.details.username)
      .then(
        respData => {
          this.TakenMeds = respData.payload;
          console.log(this.TakenMeds);
          
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
