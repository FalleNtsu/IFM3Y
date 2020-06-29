import ApiService from "./api.service";

const MoodService = {
  /**
   * Function to get the generic moods from backend
   *
   * @returns response.data
   * @throws {Error} generic moods was unsucesful
   */
  getGenricMoods: async function() {
    const response = await ApiService.get("mood/generic");
    if (!response.data.success) {
      throw new Error(response.data.message);
    }
    return response.data;
  },

  /**
   * Function to get the previous moods for a specific user
   * using their username
   *
   * @returns response.data
   * @throws {Error} generic moods was unsucesful
   */
  // TODO: Add JWT authentication
  getPreviousMoods: async function(username) {
    const response = await ApiService.get("mood/" + username);
    if (!response.data.success) {
      throw new Error(response.data.message);
    }
    return response.data;
  },

  /**
   * Fucntion to add a mood to a specifc patient
   *
   * @param {string} username
   * @param {string} genericMood
   * @param {datetime} loggedTime
   * @param {string} description
   * @returns response.data
   * @throws {Error} adding of mood was unsucesful
   */
  addPatientMood: async function(
    username,
    genericMood,
    loggedTime,
    description
  ) {
    const postData = {
      generic_mood: genericMood,
      logged_time: loggedTime,
      description: description
    };
    //post data and get response
    const response = await ApiService.post(
      "mood/" + username + "/add",
      postData
    );
    if (!response.data.success) {
      throw new Error(response.data.message);
    }
    return response.data;
  }
};

export default MoodService;
