import Vue from "vue";
import VueRouter from "vue-router";
import { ROLE_PATIENT, ROLE_PSYCHOLOGIST } from "@/store/user.type";
import store from "@/store";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: () => import("../views/Home.vue")
  },
  {
    path: "/about",
    name: "About",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/About.vue")
  },
  {
    path: "/login",
    name: "Login",
    component: () => import("../views/User/LoginView.vue"),
    beforeEnter: (to, from, next) => {
      if (store.state.user.isLoggedIn) {
        next("/");
      } else {
        next();
      }
    }
  },
  {
    path: "/mood",
    name: "Mood",
    component: () => import("../views/MoodTracking/MoodView.vue"),
    beforeEnter: (to, from, next) => {
      if (
        !store.state.user.isLoggedIn ||
        store.state.user.details.role !== ROLE_PATIENT
      ) {
        next("/");
      } else {
        next();
      }
    }
  },
  {
    path: "/mood/previous",
    name: "previousMood",
    component: () => import("../views/MoodTracking/PreviousMoods.vue")
  },
  {
    path: "/medication",
    name: "medication",
    component: () => import("../views/Medication/MedicationView.vue"),
    beforeEnter: (to, from, next) => {
      if (
        !store.state.user.isLoggedIn ||
        store.state.user.details.role !== ROLE_PATIENT
      ) {
        next("/");
      } else {
        next();
      }
    }
  },
  {
    path: "/medication/taken",
    name: "medication",
    component: () => import("../views/Medication/TakenMedicationView.vue"),
    beforeEnter: (to, from, next) => {
      if (
        !store.state.user.isLoggedIn ||
        store.state.user.details.role !== ROLE_PATIENT
      ) {
        next("/");
      } else {
        next();
      }
    }
  },
  {
    path: "/activity",
    name: "Activity",
    component: () =>
      import("../views/ActivityTracking/ActivityTrackingView.vue"),
    beforeEnter: (to, from, next) => {
      if (
        !store.state.user.isLoggedIn ||
        store.state.user.details.role !== ROLE_PATIENT
      ) {
        next("/");
      } else {
        next();
      }
    }
  },
  {
    path: "/activity/:id",
    name: "SpecificActivity",
    component: () =>
      import("../views/ActivityTracking/SpecificActivityView.vue"),
    beforeEnter: (to, from, next) => {
      if (
        !store.state.user.isLoggedIn ||
        store.state.user.details.role !== ROLE_PATIENT
      ) {
        next("/");
      } else {
        next();
      }
    }
  },
  {
    path: "/psychologist/dashboard",
    name: "PsychologistDashboard",
    component: () => import("../views/Psychologist/DashboardView.vue"),
    beforeEnter: (to, from, next) => {
      if (
        !store.state.user.isLoggedIn ||
        store.state.user.details.role !== ROLE_PSYCHOLOGIST
      ) {
        next("/");
      } else {
        next();
      }
    }
  },
  {
    path: "/psychologist/patient",
    name: "PsychologistPatient",
    component: () => import("../views/Psychologist/PatientsView.vue"),
    beforeEnter: (to, from, next) => {
      if (
        !store.state.user.isLoggedIn ||
        store.state.user.details.role !== ROLE_PSYCHOLOGIST
      ) {
        next("/");
      } else {
        next();
      }
    }
  },
  {
    path: "/psychologist/activities",
    name: "PsychologistActivities",
    component: () => import("../views/Psychologist/ActivitiesView.vue"),
    beforeEnter: (to, from, next) => {
      if (
        !store.state.user.isLoggedIn ||
        store.state.user.details.role !== ROLE_PSYCHOLOGIST
      ) {
        next("/");
      } else {
        next();
      }
    }
  },
  {
    path: "/psychologist/patient/:username",
    name: "PsychologistSpecificPatient",
    component: () => import("../views/Psychologist/SpecificPatientView.vue"),
    beforeEnter: (to, from, next) => {
      if (
        !store.state.user.isLoggedIn ||
        store.state.user.details.role !== ROLE_PSYCHOLOGIST
      ) {
        next("/");
      } else {
        next();
      }
    }
  },
  {
    path: "/psychologist/patient/:username/moods",
    name: "PatientMoods",
    component: () => import("../views/Psychologist/PatientMoodsView.vue"),
    beforeEnter: (to, from, next) => {
      if (
        !store.state.user.isLoggedIn ||
        store.state.user.details.role !== ROLE_PSYCHOLOGIST
      ) {
        next("/");
      } else {
        next();
      }
    }
  },
  {
    path: "/psychologist/patient/:username/activity/assign",
    name: "AssignActivity",
    component: () => import("../views/Psychologist/AssignActivityView.vue"),
    beforeEnter: (to, from, next) => {
      if (
        !store.state.user.isLoggedIn ||
        store.state.user.details.role !== ROLE_PSYCHOLOGIST
      ) {
        next("/");
      } else {
        next();
      }
    }
  }
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes
});

export default router;
