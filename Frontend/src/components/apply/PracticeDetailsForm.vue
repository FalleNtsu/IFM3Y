<template>
  <v-card class="elevation-0" :width="width ? width : '500px'">
    <v-card-text>
      <!-- <div class="text-center display-2 mb-12">
        <span>Enter details of your practice</span>
      </div> -->

      <v-form v-on:submit.prevent="">
        <v-text-field
          v-model="practice.pracIDData"
          label="Practitioners ID"
          name="pracID"
          type="text"
          :rules="rules"
          outlined
          clearable
          dense
        ></v-text-field>
        <v-text-field
          v-model="practice.pracAddressData"
          label="Practice Address"
          name="pracAddress"
          type="text"
          :rules="rules"
          outlined
          clearable
          dense
        ></v-text-field>
        <v-text-field
          v-model="practice.pracCellNumberData"
          label="Practie Contact Number"
          name="pracCellNumber"
          type="text"
          placeholder="e.g. 011 256 ****"
          :rules="rules"
          outlined
          clearable
          dense
        ></v-text-field>
        <v-text-field
          v-model="practice.pracEmailData"
          label="Practice Email"
          name="pracEmail"
          type="email"
          :rules="emailRules"
          outlined
          clearable
          dense
        ></v-text-field>
      </v-form>
    </v-card-text>
  </v-card>
</template>

<script>
export default {
  name: "PracticeDetailsForm",
  props: {
    width: String,
    pracID: String,
    pracAddress: String,
    pracCellNumber: String,
    pracEmail: String
  },
  data() {
    return {
      practice: {
        pracIDData: "",
        pracAddressData: "",
        pracCellNumberData: "",
        pracEmailData: ""
      },

      rules: [v => !!v || "Required"],
      emailRules: [
        v => !!v || "Required",
        v => /.+@.+\..+/.test(v) || "E-mail must be valid"
      ]
    };
  },
  watch: {
    "practice.pracIDData": function(newVal) {
      this.pracID = newVal;
    },
    "practice.pracAddressData": function(newVal) {
      this.pracAddress = newVal;
    },
    "practice.pracCellNumberData": function(newVal) {
      this.pracCellNumber = newVal;
    },
    "practice.pracEmailData": function(newVal) {
      this.pracEmail = newVal;
    }
  }
};
</script>
