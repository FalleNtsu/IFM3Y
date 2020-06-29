<template>
  <v-card class="pa-2" elevation="8">
    <p class="headline text-center">
      <span class="font-weight-bold fill">COMPLETED</span>
    </p>
    <v-card-title class="headline">
      {{ activity.name }}
      <v-spacer></v-spacer>
      Due Date: {{ completedActivity.due_date }}
    </v-card-title>
    <v-card-text>
      <v-row>
        <v-col cols="auto"> Type: </v-col>
        <v-col> {{ completedActivity.activity.type }} Activity </v-col>
      </v-row>
      <v-row>
        <v-col cols="auto">Activty Description:</v-col>
        <v-col>
          {{ completedActivity.activity.descrption }}
        </v-col>
      </v-row>
      <v-row>
        <v-col cols="auto">Personal Description:</v-col>
        <v-col>
          {{ completedActivity.description }}
        </v-col>
      </v-row>
    </v-card-text>
  </v-card>
</template>

<script>
import DateHelper from "@/helpers/date.helper";

export default {
  name: "CompletedActivityDetails",
  props: {
    completedActivity: { type: Object, required: true }
  },
  data() {
    return {};
  },
  methods: {
    formatDate: function(date) {
      return DateHelper.formatDate(date);
    }
  }
};
</script>
