<template>
  <v-alert v-model="alert.show" dark :color="alert.type">
    {{ alert.message }}
  </v-alert>
</template>

<script>
import { mapState } from "vuex";

export default {
  name: "Alert",
  computed: {
    ...mapState({
      alert: state => state.alert
    })
  },
  methods: {}
};
</script>
