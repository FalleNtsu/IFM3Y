<template>
  <v-app>
    <Header></Header>
    <v-content>
    <router-view></router-view>
    </v-content>
  </v-app>
</template>

<script>
// import HelloWorld from "./components/HelloWorld";
import Header from "./components/general/Header";
import { mapActions } from "vuex";

export default {
  name: "App",
  components: {
    // HelloWorld,
    Header,
 
  },
  methods: {
    ...mapActions({
      closeAlert: "alert/clear"
    })
  },
  watch: {
    $route() {
      this.closeAlert();
    }
  }
};
</script>
