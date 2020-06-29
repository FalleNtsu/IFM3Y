<template>
  <v-card class="elevation-0" :width="width ? width : '500px'">
    <v-card-text>
      <!-- <div class="text-center display-2 mb-12">
        <span>Enter details of your practice</span>
      </div> -->

      <v-form v-on:submit.prevent="">
        <v-text-field
          v-model="pracID"
          label="Practitioners ID"
          name="pracID"
          type="text"
          :rules="rules"
          outlined
          clearable
          dense
        ></v-text-field>
        <v-text-field
          v-model="pracAddress"
          label="Practice Address"
          name="pracAddress"
          type="text"
          :rules="rules"
          outlined
          clearable
          dense
        ></v-text-field>
        <v-text-field
          v-model="pracCellNumber"
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
          v-model="pracEmail"
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
  name: "UserDetailsForm",
  props: {
    width: String,
    pracID: { type: String, Required: true },
    pracAddress: { type: String, Required: true },
    pracCellNumber: { type: String, Required: true },
    pracEmail: { type: String, Required: true }
  },
  data() {
    return {
      pracIDData: "",
      pracAddressData: "",
      pracCellNumberData: "",
      pracEmaiDatal: "",
      rules: [v => !!v || "Required"],
      emailRules: [
        v => !!v || "Required",
        v => /.+@.+\..+/.test(v) || "E-mail must be valid"
      ]
    };
  }
};
</script>
