<template>
  <v-container fill-height>
    <v-layout align-center justify-center>
      <v-stepper v-model="stepPos" alt-labels>
        <v-stepper-header>
          <v-stepper-step :complete="stepPos > 1" step="1">
            Practice details
          </v-stepper-step>

          <v-divider></v-divider>

          <v-stepper-step :complete="stepPos > 2" step="2">
            User Details
          </v-stepper-step>

          <v-divider></v-divider>

          <v-stepper-step step="3"> Done </v-stepper-step>
        </v-stepper-header>

        <v-stepper-items>
          <v-stepper-content step="1">
            <!-- <v-card class="mb-12" color="grey lighten-1" height="200px"> -->
            <PracticeDetailsForm
              :pracID="practice.pracID"
              :pracAddress="practice.pracAddress"
              :pracCellNumber="practice.pracCellNumber"
              :pracEmail="practice.pracEmail"
            ></PracticeDetailsForm>

            <v-btn color="primary" @click="stepPos = 2">
              Continue
            </v-btn>
            <v-btn color="primary" @click="test">
              Continue
            </v-btn>

            <!-- <v-btn text>Cancel</v-btn> -->
          </v-stepper-content>

          <v-stepper-content step="2">
            <UserDetailsForm></UserDetailsForm>

            <v-btn color="primary" @click="stepPos = 3">
              Continue
            </v-btn>

            <v-btn text @click="stepPos = 1">Back</v-btn>
          </v-stepper-content>

          <v-stepper-content step="3">
            <v-card
              class="mb-12"
              color="grey lighten-1"
              height="200px"
            ></v-card>

            <v-btn color="primary" @click="stepPos = 1">
              Continue
            </v-btn>

            <v-btn text @click="stepPos = 2">Back</v-btn>
          </v-stepper-content>
        </v-stepper-items>
      </v-stepper>
    </v-layout>
  </v-container>
</template>

<script>
// @ is an alias to /src
import PracticeDetailsForm from "@/components/apply/PracticeDetailsForm.vue";
import UserDetailsForm from "@/components/apply/UserDetailsForm.vue";

import { mapState, mapActions } from "vuex";

export default {
  name: "Apply",
  components: {
    PracticeDetailsForm,
    UserDetailsForm
  },
  data() {
    return {
      drawer: false,
      stepPos: 1,
      steps: 2,
      practice: {
        pracID: "",
        pracAddress: "",
        pracCellNumber: "",
        pracEmail: ""
      }
    };
  },
  watch: {
    steps(val) {
      if (this.stepPos > val) {
        this.stepPos = val;
      }
    }
  },
  computed: {
    ...mapState({
      user: state => state.user
    })
  },
  methods: {
    ...mapActions("user", ["logout"]),
    nextStep: function(n) {
      if (n === this.steps) {
        this.stepPos = 1;
      } else {
        this.e1 = n + 1;
      }
    },
    test() {
      console.log("====================================");
      console.log(this.practice);
      console.log("====================================");
    }
  }
};
</script>
