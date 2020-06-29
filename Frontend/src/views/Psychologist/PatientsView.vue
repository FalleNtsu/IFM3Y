<template>
  <div class="home">
    <v-container>
      <v-row class="mb-6" justify="center">
        <v-col cols="10">
          <v-simple-table fixed-header>
            <template v-slot:default>
              <thead>
                <tr>
                  <th class="text-left">Username</th>
                  <th class="text-left">Title</th>
                  <th class="text-left">First Name</th>
                  <th class="text-left">Surname</th>
                  <th class="text-right">Actions</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="patient in patients" :key="patient.user.username">
                  <td>{{ patient.user.username }}</td>
                  <td>{{ patient.user.title }}</td>
                  <td>{{ patient.user.first_name }}</td>
                  <td>{{ patient.user.surname }}</td>
                  <td class="text-right">
                    <router-link
                      :to="'/psychologist/patient/' + patient.user.username"
                    >
                      <v-btn>
                        View
                      </v-btn>
                    </router-link>
                  </td>
                </tr>
              </tbody>
            </template>
          </v-simple-table>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
import userService from "@/services/user.service";
import DateHelper from "@/helpers/date.helper";

import { mapState } from "vuex";

export default {
  name: "Patients",
  components: {},
  data() {
    return {
      patients: []
    };
  },
  computed: {
    ...mapState({
      user: state => state.user
    })
  },
  async created() {
    await userService.getPsychologistPatients(this.user.details.username).then(
      respData => {
        this.patients = respData.payload;

        console.log("====================================");
        console.log(this.patients);
        console.log("====================================");
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
