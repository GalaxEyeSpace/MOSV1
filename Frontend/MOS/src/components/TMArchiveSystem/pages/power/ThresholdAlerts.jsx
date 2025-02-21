import React, { useEffect, useState } from "react";
import "../../styles/power/alerts.css";

const ThresholdAlerts = () => {
  const [alerts, setAlerts] = useState([]);
  
  useEffect(() => {
    fetch("http://localhost:8000/telemetry/get-data/?table=power&start_time=2024-12-05T09:50:59.000Z&end_time=2024-12-05T10:40:58.000Z")
      .then(response => response.json())
      .then(data => {
        console.log("Fetched Power Data for Alerts:", data);

        if (Array.isArray(data)) {
          // ✅ Filter out data where power consumption exceeds threshold
          const alertData = data
            .filter(item => parseFloat(item.power_consumed) > parseFloat(item.threshold))
            .map(item => ({
              timestamp: new Date(item.timestep).toLocaleString(),
              power_consumed: parseFloat(item.power_consumed),
              threshold: parseFloat(item.threshold),
            }));

          setAlerts(alertData);
        } else {
          console.error("Unexpected API response format:", data);
        }
      })
      .catch(error => console.error("Error fetching telemetry data:", error));
  }, []);

  return (
    <div className="alert-container">
      <h2>⚠️ Power Consumption Alerts</h2>
      {alerts.length > 0 ? (
        <table className="alert-table">
          <thead>
            <tr>
              <th>Timestamp</th>
              <th>Power Consumed (W)</th>
              <th>Threshold (W)</th>
              <th>Status</th>
            </tr>
          </thead>
          <tbody>
            {alerts.map((alert, index) => (
              <tr key={index} className="alert-row">
                <td>{alert.timestamp}</td>
                <td>{alert.power_consumed}</td>
                <td>{alert.threshold}</td>
                <td className="alert-status critical">⚠️ Exceeded</td>
              </tr>
            ))}
          </tbody>
        </table>
      ) : (
        <p className="no-alerts">✅ No Alerts - Power Consumption is Safe</p>
      )}
    </div>
  );
};

export default ThresholdAlerts;
