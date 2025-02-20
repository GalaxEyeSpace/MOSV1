import React, { useEffect, useState } from "react";
import {
  LineChart,
  Line,
  CartesianGrid,
  XAxis,
  YAxis,
  Tooltip,
  Legend,
  ResponsiveContainer,
} from "recharts";

const SolarVsConsumedGraph = () => {
  const [graphData, setGraphData] = useState([]);

  useEffect(() => {
    fetch("http://localhost:8000/telemetry/get-data/?table=power&start_time=2024-12-05T09:50:59.000Z&end_time=2024-12-05T10:40:58.000Z")
      .then(response => response.json())
      .then(data => {
        if (Array.isArray(data)) {
          const formattedData = data.map((item) => ({
            timestamp: new Date(item.timestep).toLocaleTimeString([], { hour: "2-digit", minute: "2-digit" }),
            solar: parseFloat(item.solar),
            power_consumed: parseFloat(item.power_consumed),
          }));
          setGraphData(formattedData);
        } else {
          console.error("Unexpected API response format:", data);
        }
      })
      .catch(error => console.error("Error fetching telemetry data:", error));
  }, []);

  return (
    <div className="graph-wrapper" style={{ width: "100%", height: "100%" }}>
      {graphData.length > 0 ? (
        <ResponsiveContainer width="100%" height="100%">
          <LineChart data={graphData} margin={{ top: 5, right: 10, left: 0, bottom: 5 }}>
            <XAxis dataKey="timestamp" tick={{ fontSize: 10, fill: "white" }} />
            <YAxis tick={{ fontSize: 20, fill: "white" }} />
            <CartesianGrid stroke="#444" strokeDasharray="5 5" />
            <Tooltip contentStyle={{ backgroundColor: "#222", color: "white" }} />
            <Legend wrapperStyle={{ fontSize: "12px" }} />
            <Line type="monotone" dataKey="solar" stroke="yellow" dot={{ r: 1 }} />
            <Line type="monotone" dataKey="power_consumed" stroke="red" dot={{ r: 1 }} />
          </LineChart>
        </ResponsiveContainer>
      ) : (
        <p style={{ color: "white", fontSize: "12px" }}>Loading...</p>
      )}
    </div>
  );
};

export default SolarVsConsumedGraph;
