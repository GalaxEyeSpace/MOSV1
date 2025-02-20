// TMArchiveSystem/services/api.js

export const fetchPowerTelemetry = () => {
  return fetch("http://localhost:8000/telemetry/get-data/?table=power&start_time=2024-12-05T09:50:59.000Z&end_time=2024-12-05T10:40:58.000Z") 
    .then(response => response.json()) // Convert response to JSON
    .then(data => {
      console.log("API Response:", data); // ✅ Keep logging API response
      return data; // ✅ Return fetched data
    })
    .catch(error => {
      console.error("Error fetching data:", error); // Handle errors
      return []; // ✅ Return empty array if error occurs
    });
};
