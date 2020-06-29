<template>
  <v-list subheader dense>
    <v-subheader>General</v-subheader>
    <v-list-item-group color="primary">
      <v-list-item>
        <!-- <v-list-item-icon>
          <v-icon>settings</v-icon>
        </v-list-item-icon> -->
        <v-list-item-content>
          <v-list-item-title>Settings</v-list-item-title>
        </v-list-item-content>
      </v-list-item>

      <v-list-item @click="this.logoutUser">
        <v-list-item-content>
          <v-list-item-title>Logout</v-list-item-title>
        </v-list-item-content>
      </v-list-item>
    </v-list-item-group>
  </v-list>
</template>

<script>
import { mapActions } from "vuex";

export default {
  name: "SideDrawer",
  methods: {
    ...mapActions("user", ["logout"]),
    logoutUser: async function() {
      await this.logout();
      this.$router.push("/");
    }
  }
};
</script>
