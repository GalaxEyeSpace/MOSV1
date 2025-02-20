
import "../../styles/power/powerEfficiency.css";
import React, { useEffect, useState } from "react";


const PowerEfficiency = () => {
  const [efficiency, setEfficiency] = useState(0);

  useEffect(() => {
    fetch("http://localhost:8000/telemetry/get-data/?table=power&start_time=2024-12-05T09:50:59.000Z&end_time=2024-12-05T10:40:58.000Z")
      .then(response => response.json())
      .then(data => {
        console.log("Fetched Efficiency Data:", data);

        if (Array.isArray(data) && data.length > 0) {
          const latest = data[data.length - 1]; // Get the latest timestamp
          const solar = parseFloat(latest.solar);
          const consumed = parseFloat(latest.power_consumed);
          const efficiencyCalc = solar > 0 ? ((solar - consumed) / solar) * 100 : 0;

          setEfficiency(efficiencyCalc.toFixed(2)); // Set efficiency
        } else {
          console.error("Unexpected API response format:", data);
        }
      })
      .catch(error => console.error("Error fetching telemetry data:", error));
  }, []);

  return (
    <>
      
      <div className="progress-bar">
        <div
          className="progress"
          style={{
            width: `${efficiency}%`,
            backgroundColor: efficiency > 50 ? "#00C49F" : "#FF4444", // Green if good, Red if poor
          }}
        >
          {efficiency}%
        </div>
      </div>
    </>
  );
};

export default PowerEfficiency;
