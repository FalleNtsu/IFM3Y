<template>
  <div>
    <v-navigation-drawer v-if="user.isLoggedIn" clipped v-model="drawer" app>
      <SideDrawer></SideDrawer>
    </v-navigation-drawer>
    <v-app-bar clipped-left app light>
      <v-app-bar-nav-icon
        v-if="user.isLoggedIn"
        @click.stop="drawer = !drawer"
      ></v-app-bar-nav-icon>

      <v-toolbar-title>
        <router-link to="/">
          <v-btn text>
            <div class="d-flex align-center">
              <h1 style=" color : purple">MindCompass</h1>
            </div>
          </v-btn>
        </router-link>
      </v-toolbar-title>

      <div v-if="user.isLoggedIn && user.details.role === ROLE_PATIENT">
        <router-link to="/mood">
          <v-btn text>
            <span>Mood</span>
          </v-btn>
        </router-link>
        <router-link to="/activity">
          <v-btn text>
            <span>Activity</span>
          </v-btn>
        </router-link>
        <router-link to="/medication">
          <v-btn text>
            <span>Medication</span>
          </v-btn>
        </router-link>
      </div>
      <div v-if="user.isLoggedIn && user.details.role === ROLE_PSYCHOLOGIST">
        <router-link to="/psychologist/dashboard">
          <v-btn text>
            <span>Dashboard</span>
          </v-btn>
        </router-link>
      </div>

      <v-spacer></v-spacer>

      <router-link v-if="!user.isLoggedIn" to="/login">
        <v-btn text>
          <span>Login</span>
        </v-btn>
      </router-link>
    </v-app-bar>
  </div>
</template>

<script>
import { mapState, mapActions } from "vuex";
import { ROLE_PATIENT, ROLE_PSYCHOLOGIST } from "@/store/user.type";
import SideDrawer from "./SideDrawer";

export default {
  name: "Header",
  components: {
    SideDrawer
  },
  data() {
    return {
      ROLE_PATIENT: ROLE_PATIENT,
      ROLE_PSYCHOLOGIST: ROLE_PSYCHOLOGIST,
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
<style scoped>
/* .a {
  color: rgb(141, 99, 45);
} */
/* h1 {
  color: rgb(175, 199, 43);
} */
a {
  text-decoration-line: none;
}
</style>
