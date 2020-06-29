<template>
  <v-container fluid fill-height>
    <v-layout align-center justify-center>
      <v-card class="elevation-12" width="500">
        <v-card-text>
          <div class="text-center display-2 mb-12"><span>Login</span></div>

          <Alert></Alert>

          <v-form v-on:submit.prevent="">
            <v-alert v-if="this.err" type="error" :icon="false">
              {{ this.errMessage }}
            </v-alert>
            <v-alert v-if="this.success" type="success" :icon="false">
              {{ this.successMessage }}
            </v-alert>
            <v-text-field
              v-model="username"
              label="Username"
              name="username"
              type="text"
              :error="this.err"
              :success="this.success"
              :rules="rules"
            ></v-text-field>
            <v-text-field
              v-model="password"
              label="Password"
              name="password"
              :type="showPassword ? 'text' : 'password'"
              :append-icon="showPassword ? 'mdi-eye' : 'mdi-eye-off'"
              :error="this.err"
              :success="this.success"
              :rules="rules"
              @click:append="showPassword = !showPassword"
            ></v-text-field>
            <div class="text-right">
              <router-link to="forgot">Forgot password?</router-link>
            </div>

            <v-btn
              @click="LoginHandler"
              color="primary mt-6"
              type="submit"
              x-large
              block
              rounded
              >Login</v-btn
            >
          </v-form>

          <div class="mt-4 text-center">
            <span>
              Don't have an account?
              <router-link to="register">Register Here</router-link>
            </span>
          </div>
        </v-card-text>
      </v-card>
    </v-layout>
  </v-container>
</template>

<script>
export default {
  name: "AssignActivity",
  components: {},
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
