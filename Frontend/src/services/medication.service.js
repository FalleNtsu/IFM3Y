import ApiService from "./api.service";

const MeciationService = {
  /**
   * Function to get the generic moods from backend
   *
   * @returns response.data
   * @throws {Error} generic moods was unsucesful
   */
  MedicationList: async function() {
    const response = await ApiService.get("medication/listMeds");
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
  getPatientMedication: async function(username) {
    const response = await ApiService.get("medication/" + username + "/patientMeds");
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
  PatientTakenMeds: async function(username) {
    //post data and get response
    const response = await ApiService.get("medication/" + username + "/patientMeds/Taken"
    );
    if (!response.data.success) {
      throw new Error(response.data.message);
    }
    return response.data;
  }
};

export default MeciationService;
