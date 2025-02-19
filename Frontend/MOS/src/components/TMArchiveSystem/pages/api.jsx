// TMArchiveSystem/services/api.js
import axios from "axios";

const API_BASE_URL = "http://localhost:8000/get-data/"; // Django API URL

/**
 * Fetch Power Data for a given time range
 */
export const fetchPowerTelemetry = async () => {
  try {
    // Define the specific time range
    const startTime = "2024-12-05 09:50:59.000";
    const endTime = "2024-12-05 10:40:58.000";

    // Make the API call with time filters
    const response = await axios.get(API_BASE_URL, {
      params: {
        start_time: startTime,
        end_time: endTime,
      },
    });

    // Extract only power-related data
    const powerData = response.data.filter(entry => entry.module === "Power");

    return powerData;
  } catch (error) {
    console.error("Error fetching power telemetry:", error);
    return [];
  }
};
