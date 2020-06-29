<template>
  <v-card class="pa-2" elevation="8">
    <v-card-title class="headline">
      {{ assignedActivity.activity.name }}
      <v-spacer></v-spacer>
      Due Date: {{ formatDate(assignedActivity.due_date) }}
    </v-card-title>
    <v-card-text>
      <p>
        <v-row>
          <v-col cols="auto"> Type: </v-col>
          <v-col>
            {{ assignedActivity.activity.activity_type.name }}
          </v-col>
        </v-row>
        <v-row>
          <v-col cols="auto">Activty Description:</v-col>
          <v-col>
            {{ assignedActivity.activity.description }}
          </v-col>
        </v-row>
        <v-row>
          <v-col cols="auto">Personal Description:</v-col>
          <v-col>
            {{ assignedActivity.description }}
          </v-col>
        </v-row>
      </p>
      <v-divider></v-divider>
      <div v-if="assignedActivity.activity.proof_type.name === PROOF_PHOTO">
        <v-form v-on:submit.prevent="">
          <h2 class="my-5">
            Proof ({{ assignedActivity.activity.proof_type.name }})
          </h2>

          <v-file-input
            label="Upload Photo"
            prepend-icon="mdi-camera"
            accept="image/png, image/jpeg, image/bmp"
            outlined
            chips
            hint="Click on 'Upload Photo' and pick a single photo to upload"
            persistent-hint
          >
          </v-file-input>

          <v-btn
            @click="console.log('submitted')"
            color="primary"
            type="submit"
            x-large
            block
            rounded
            >Upload</v-btn
          >
        </v-form>
      </div>
      <div v-if="assignedActivity.activity.proof_type.name === PROOF_DOCUMENT">
        <v-form v-on:submit.prevent="">
          <h2 class="my-5">
            Proof ({{ assignedActivity.activity.proof_type.name }})
          </h2>

          <v-file-input
            label="Upload Document"
            prepend-icon="mdi-file-document"
            outlined
            chips
            hint="Click on 'Upload Document' and pick a single document to upload"
            persistent-hint
          >
          </v-file-input>

          <v-btn
            @click="console.log('submitted')"
            color="primary"
            type="submit"
            x-large
            block
            rounded
            >Upload</v-btn
          >
        </v-form>
      </div>
    </v-card-text>
  </v-card>
</template>

<script>
import { PROOF_PHOTO, PROOF_DOCUMENT } from "@/store/activity.proof.type";
import DateHelper from "@/helpers/date.helper";

export default {
  name: "AssignedActivityDetails",
  props: {
    assignedActivity: { type: Object, required: true }
  },
  data() {
    return {
      PROOF_PHOTO: PROOF_PHOTO,
      PROOF_DOCUMENT: PROOF_DOCUMENT
    };
  },
  methods: {
    formatDate: function(date) {
      return DateHelper.formatDate(date);
    }
  }
};
</script>
