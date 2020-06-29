import axios from "axios";

// API url for raspberry pi
// const API_URL = "http://105.186.29.124/api/";
// API url for raspberry pi
const API_URL = "http://127.0.0.1:8000/api/";

const ApiService = {
  /**
   * Function for get function using axios
   *
   * @param {string} path path of api
   */
  get(path) {
    path = path.charAt(0) === "/" ? path.substring(1) : path;
    return axios.get(API_URL + path);
  },

  /**
   * Function for posting data to a specific path of the API
   *
   * @param {string} path path of api
   * @param {object} data object to post
   */
  post(path, data) {
    path = path.charAt(0) === "/" ? path.substring(1) : path;
    return axios.post(API_URL + path, data);
  }
};

export default ApiService;
