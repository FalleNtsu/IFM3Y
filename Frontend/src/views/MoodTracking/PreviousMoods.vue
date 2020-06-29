<template>
  <PreviousMoods :username="this.user.details.username"></PreviousMoods>
</template>

<script>
import PreviousMoods from "@/components/MoodTracking/ListMoods.vue";
import { mapState } from "vuex";

export default {
  components: {
    PreviousMoods
  },
  computed: {
    ...mapState({
      user: state => state.user
    })
  }
};
</script>
