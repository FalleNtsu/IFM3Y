const state = {
  show: false,
  type: null,
  message: null
};

const actions = {
  success({ commit }, message) {
    commit("success", message);
  },
  error({ commit }, message) {
    commit("error", message);
  },
  clear({ commit }) {
    commit("clear");
  }
};

const mutations = {
  success(state, message) {
    state.type = "success";
    state.show = true;
    state.message = message;
  },
  error(state, message) {
    state.type = "error";
    state.show = true;
    state.message = message;
  },
  clear(state) {
    state.show = false;
    state.type = null;
    state.message = null;
  }
};

export default {
  namespaced: true,
  state,
  actions,
  mutations
};
