import ApiService from "./api.service";

const ActivityService = {
  // Working
  getActivityTypes: async function() {
    const response = await ApiService.get("activity/activityTypes");
    if (!response.data.success) {
      throw new Error(response.data.message);
    }
    return response.data;
  },
  getProofTypes: async function() {
    const response = await ApiService.get("activity/proofTypes");
    if (!response.data.success) {
      throw new Error(response.data.message);
    }
    return response.data;
  },
  // Temp functions
  // TODO: Change functions to use API instead of test data
  getAssignedActivities: async function(username) {
    const response = await ApiService.get("activity/" + username + "/assigned");
    if (!response.data.success) {
      throw new Error(response.data.message);
    }
    var payload = response.data.payload;
    var output = [];
    if (username) {
      output = payload.filter(function(obj) {
        return obj.isCompleted === false;
      });
    }
    return output;
  },
  getCompletedActivities: async function(username) {
    const response = await ApiService.get("activity/" + username + "/assigned");
    if (!response.data.success) {
      throw new Error(response.data.message);
    }
    var payload = response.data.payload;
    var output = [];
    if (username) {
      output = payload.filter(function(obj) {
        return obj.isCompleted === true;
      });
    }
    return output;
  },
  getSpecificActivity: async function(username, id) {
    const response = await ApiService.get(
      "activity/" + username + "/assigned/" + id
    );
    if (!response.data.success) {
      throw new Error(response.data.message);
    }
    var payload = response.data.payload;
    return payload;
  },
  unassignActivity: async function(assignedActivityID) {
    const response = await ApiService.post("activity/unassign", {
      assigned_activity_id: assignedActivityID
    });
    if (!response.data.success) {
      throw new Error(response.data.message);
    }
    var payload = response.data.payload;
    return payload;
  },
  getActivities: async function() {
    const response = await ApiService.get("activity/all");
    if (!response.data.success) {
      throw new Error(response.data.message);
    }
    var payload = response.data.payload;
    return payload;
  }
};

export default ActivityService;
