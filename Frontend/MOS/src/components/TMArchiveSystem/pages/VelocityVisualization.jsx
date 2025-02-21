import React, { useEffect, useState } from "react";
import { LineChart, Line, CartesianGrid, XAxis, YAxis, Tooltip, Legend, ResponsiveContainer } from "recharts";

const AttitudeVisualization = () => {
  const [attitudeData, setAttitudeData] = useState([]);

  // Function to calculate attitude (roll, pitch, yaw) from velocity components
  const calculateAttitude = (x, y, z) => {
    const roll = Math.atan2(y, z); // Roll calculation
    const pitch = Math.atan2(-x, Math.sqrt(y * y + z * z)); // Pitch calculation
    const yaw = Math.atan2(y, x); // Yaw calculation
    return { roll, pitch, yaw };
  };
  
  // Fetch velocity data and process it
  useEffect(() => {
    fetch("http://localhost:8000/telemetry/get-data/?table=velocity&start_time=2024-12-05T09:50:59.000Z&end_time=2024-12-05T10:40:58.000Z")
      .then((response) => response.json())
      .then((data) => {
        if (Array.isArray(data)) {
          const formattedData = data.map((item) => {
            const { roll, pitch, yaw } = calculateAttitude(item.x, item.y, item.z); // Calculate attitude
            return {
              time: new Date(item.timestep).toLocaleString([], { hour: "2-digit", minute: "2-digit" }),
              roll: roll * (180 / Math.PI), // Convert to degrees
              pitch: pitch * (180 / Math.PI), // Convert to degrees
              yaw: yaw * (180 / Math.PI), // Convert to degrees
            };
          });
          setAttitudeData(formattedData);
        } else {
          console.error("No valid telemetry data received.");
        }
      })
      .catch((error) => console.error("Error fetching velocity data:", error));
  }, []);
  
  return (
    <div style={{ width: "90%", margin: "auto", padding: "20px" }}>
      {attitudeData.length > 0 ? (
        <ResponsiveContainer width="100%" height={400}>
          <LineChart data={attitudeData}>
            {/* X-Axis */}
            <XAxis dataKey="time" tick={{ fontSize: 10, fill: "white" }} />
            {/* Y-Axis */}
            <YAxis tick={{ fontSize: 20, fill: "white" }} />
            <CartesianGrid stroke="#444" strokeDasharray="5 5" />
            <Tooltip contentStyle={{ backgroundColor: "#222", color: "white" }} />
            <Legend wrapperStyle={{ fontSize: "10px" }} />
            {/* Line for Roll */}
            <Line type="monotone" dataKey="roll" stroke="red" dot={{ r: 1 }} />
            {/* Line for Pitch */}
            <Line type="monotone" dataKey="pitch" stroke="green" dot={{ r: 1 }} />
            {/* Line for Yaw */}
            <Line type="monotone" dataKey="yaw" stroke="blue" dot={{ r: 1 }} />
          </LineChart>
        </ResponsiveContainer>
      ) : (
        <p style={{ color: "white", fontSize: "12px" }}>Loading...</p>
      )}
    </div>
  );
};

export default AttitudeVisualization;
