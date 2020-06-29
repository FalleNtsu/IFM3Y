<template>
  <div class="home">
    <v-container>
      <v-row class="text-center">
        <v-col cols="12">
          <v-img
            :src="require('../assets/logo.svg')"
            class="my-3"
            contain
            height="200"
          />
        </v-col>

        <v-col class="mb-4">
          <router-link to="/apply">
            <v-btn color="primary" dark x-large>Apply Now!</v-btn>
          </router-link>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
// @ is an alias to /src
// import HelloWorld from "@/components/HelloWorld.vue";

import { mapState, mapActions } from "vuex";

export default {
  name: "Home",
  components: {},
  data() {
    return {
      drawer: false
    };
  },
  computed: {
    ...mapState({
      user: state => state.user
    })
  },
  methods: {
    ...mapActions("user", ["logout"])
  }
};
</script>
