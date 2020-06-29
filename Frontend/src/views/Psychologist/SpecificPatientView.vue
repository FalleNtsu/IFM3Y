<template>
  <div class="home">
    <v-container>
      <v-row justify="center" class="mb-6">
        <v-col :cols="6">
          <v-card class="pa-2" elevation="8" v-if="patient">
            <v-card-title class="headline">
              {{
                patient.user.title +
                  " " +
                  patient.user.first_name +
                  " " +
                  patient.user.surname
              }}
            </v-card-title>
            <v-card-text>
              <div>
                <v-expansion-panels multiple>
                  <v-expansion-panel>
                    <v-expansion-panel-header>
                      Diagnosis
                    </v-expansion-panel-header>
                    <v-expansion-panel-content>
                      <div>Name: {{ patient.diagnosis.name }}</div>
                      <div>
                        Description: {{ patient.diagnosis.description }}
                      </div>
                    </v-expansion-panel-content>
                  </v-expansion-panel>
                  <v-expansion-panel>
                    <v-expansion-panel-header>
                      Activities
                    </v-expansion-panel-header>

                    <v-expansion-panel-content>
                      <patientAssignedActivties
                        :username="this.patientUsername"
                      >
                      </patientAssignedActivties>
                      <v-row>
                        <v-col>
                          <router-link
                            :to="
                              '/psychologist/patient/' +
                                patient.user.username +
                                '/activity/assign'
                            "
                          >
                            <v-btn color="primary " type="submit" block rounded>
                              Asign Activity
                            </v-btn>
                          </router-link>
                        </v-col>
                      </v-row>
                    </v-expansion-panel-content>
                  </v-expansion-panel>

                  <v-expansion-panel>
                    <v-expansion-panel-header>
                      Moods
                    </v-expansion-panel-header>
                    <v-expansion-panel-content>
                      <router-link
                        :to="
                          '/psychologist/patient/' +
                            patient.user.username +
                            '/moods'
                        "
                      >
                        <v-btn color="primary mt-6" type="submit" block rounded>
                          View Moods
                        </v-btn>
                      </router-link>
                    </v-expansion-panel-content>
                  </v-expansion-panel>

                  <v-expansion-panel>
                    <v-expansion-panel-header>
                      Medication
                    </v-expansion-panel-header>
                    <v-expansion-panel-content>
                      <div>Name: {{ patient.diagnosis.name }}</div>
                      <div>
                        Description: {{ patient.diagnosis.description }}
                      </div>
                    </v-expansion-panel-content>
                  </v-expansion-panel>
                </v-expansion-panels>
              </div>
            </v-card-text>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
import userService from "@/services/user.service";
import DateHelper from "@/helpers/date.helper";
import patientAssignedActivties from "@/components/psychologist/PatientAssignedActivities";

import { mapState } from "vuex";

export default {
  name: "SpecificPatient",
  components: {
    patientAssignedActivties
  },
  data() {
    return {
      patient: null,
      patientUsername: ""
    };
  },
  computed: {
    ...mapState({
      user: state => state.user
    })
  },
  async created() {
    this.patientUsername = this.$route.params.username;

    await userService
      .getPsychologistSpecificPatients(this.patientUsername)
      .then(
        respData => {
          this.patient = respData.payload;
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
