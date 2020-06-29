<template>
  <PreviousMoods :username="this.patientUsername"></PreviousMoods>
</template>

<script>
import PreviousMoods from "@/components/MoodTracking/ListMoods.vue";
export default {
  name: "PatientMoods",
  components: {
    PreviousMoods
  },
  data() {
    return {
      patientUsername: ""
    };
  },
  async created() {
    this.patientUsername = this.$route.params.username;
  }
};
</script>
