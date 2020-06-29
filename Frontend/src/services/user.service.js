import ApiService from "./api.service";

const UserService = {
  /**
   * Function to send the username and password
   * to the API and get a response
   *
   * @param {string} username
   * @param {string} password
   * @returns response.data
   * @throws {Error} login was unsucesful
   */
  login: async function(username, password) {
    const postData = { username: username, password: password };
    //post data and get response
    const response = await ApiService.post("user/login", postData);
    if (!response.data.success) {
      throw new Error(response.data.message);
    }
    return response.data;
  },
  logout: async function() {
    return null;
  },
  /**
   * Function to get the Patients that belong to a psychologist
   *
   * @param {string} username
   */
  getPsychologistPatients: async function(username) {
    //post data and get response
    const response = await ApiService.get(
      "user/psychologist/" + username + "/patients"
    );
    if (!response.data.success) {
      throw new Error(response.data.message);
    }
    return response.data;
  },
  /**
   * Function to get the Patients that belong to a psychologist
   *
   * @param {string} username
   */
  getPsychologistSpecificPatients: async function(username) {
    //post data and get response
    const response = await ApiService.get("user/patient/" + username);
    if (!response.data.success) {
      throw new Error(response.data.message);
    }
    return response.data;
  }
};

export default UserService;
