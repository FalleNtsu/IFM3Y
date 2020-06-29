import userService from "../services/user.service";

const state = {
  isLoggedIn: false,
  details: {
    username: "",
    role: ""
  }
};

const getters = {};

const actions = {
  async login({ dispatch, commit }, { username, password }) {
    await userService.login(username, password).then(
      respData => {
        commit("loginSuccess", respData.payload);
        dispatch("alert/success", respData.message, { root: true });
      },
      err => {
        commit("loginFailure");
        dispatch("alert/error", err, { root: true });
      }
    );
  },
  logout({ commit }) {
    userService.logout();
    commit("logout");
  }
};

const mutations = {
  loginSuccess(state, user) {
    state.isLoggedIn = true;
    state.details = user;
  },
  loginFailure(state) {
    state.isLoggedIn = false;
    state.details = null;
  },
  logout(state) {
    state.isLoggedIn = false;
    state.details = null;
  }
};

export default {
  namespaced: true,
  state,
  actions,
  mutations,
  getters
};
