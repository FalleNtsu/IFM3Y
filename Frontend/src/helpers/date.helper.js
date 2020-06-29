// const MONTHS = [
//   "January",
//   "February",
//   "March",
//   "April",
//   "May",
//   "June",
//   "July",
//   "August",
//   "September",
//   "October",
//   "November",
//   "December"
// ];

const DateHelper = {
  formatDate(date) {
    var d = new Date(date);
    var output = d.getFullYear() + "/" + d.getMonth() + "/" + d.getDate();
    return output.toString();
  }
};

export default DateHelper;
