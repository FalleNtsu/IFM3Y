<template>
  <v-hover v-slot:default="{ hover }" value = true>
      <v-row>
        <template v-for="(mood,m) in defaultmoods">
          <v-card :key="m" class="mx-auto" color="grey lighten-4" max-width="600" width = 300px height = 300px style="justify-content : center">
               <div
                  :key ="m"
                  v-if="hover"
                  class="d-flex transition-fast-in-fast-out orange darken-2 v-card--reveal display-3 white--text"
                  style="height: 100%;"
                >
                <v-icon :key="m" v-bind:class="mood.class" @click="setMood(mood.mood)">{{mood.icon}}
            </v-icon>
                </div>
          </v-card>
        </template>
      </v-row>
    </v-hover>
</template>