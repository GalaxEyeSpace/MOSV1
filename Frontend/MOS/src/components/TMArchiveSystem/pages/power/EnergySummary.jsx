import React, { useEffect, useState } from "react";


const EnergySummary = () => {
  const [summary, setSummary] = useState(null);

  useEffect(() => {
    fetch("http://localhost:8000/telemetry/get-data/?table=power&start_time=2024-12-05T09:50:59.000Z&end_time=2024-12-05T10:40:58.000Z")
      .then(response => response.json())
      .then(data => {
        console.log("Fetched Power Data for Summary:", data);

        if (Array.isArray(data) && data.length > 0) {
          const solarValues = data.map((item) => parseFloat(item.solar));
          const consumedValues = data.map((item) => parseFloat(item.power_consumed));

          const summaryData = {
            minSolar: Math.min(...solarValues),
            maxSolar: Math.max(...solarValues),
            avgSolar: (solarValues.reduce((a, b) => a + b, 0) / solarValues.length).toFixed(2),
            minConsumed: Math.min(...consumedValues),
            maxConsumed: Math.max(...consumedValues),
            avgConsumed: (consumedValues.reduce((a, b) => a + b, 0) / consumedValues.length).toFixed(2),
          };

          setSummary(summaryData);
        } else {
          console.error("Unexpected API response format:", data);
        }
      })
      .catch(error => console.error("Error fetching telemetry data:", error));
  }, []);

  return (
    <div className="summary-container">
      <h2>Energy Summary</h2>
      {summary ? (
        <div className="summary-table">
          <div>
            <h3>Solar Power</h3>
            <p>🔹 Min: {summary.minSolar} W</p>
            <p>🔹 Max: {summary.maxSolar} W</p>
            <p>🔹 Avg: {summary.avgSolar} W</p>
          </div>
          <div>
            <h3>Power Consumed</h3>
            <p>🔸 Min: {summary.minConsumed} W</p>
            <p>🔸 Max: {summary.maxConsumed} W</p>
            <p>🔸 Avg: {summary.avgConsumed} W</p>
          </div>
        </div>
      ) : (
        <p>Loading...</p>
      )}
    </div>
  );
};

export default EnergySummary;
