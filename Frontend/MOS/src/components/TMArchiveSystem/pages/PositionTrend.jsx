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

const PositionGraph = () => {
  const [graphData, setGraphData] = useState([]);

  useEffect(() => {
    fetch("http://localhost:8000/telemetry/get-data/?table=position&start_time=2024-12-05T09:50:59.000Z&end_time=2024-12-05T10:40:58.000Z")
      .then(response => response.json())
      .then(data => {
        if (Array.isArray(data)) {
          const formattedData = data.map((item) => ({
            timestamp: new Date(item.timestep).toLocaleString([], { hour: "2-digit", minute: "2-digit" }), // Convert timestamp
            x: parseFloat(item.x),
            y: parseFloat(item.y),
            z: parseFloat(item.z),
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
            <YAxis tick={{ fontSize: 12, fill: "white" }} />
            <CartesianGrid stroke="#444" strokeDasharray="5 5" />
            <Tooltip contentStyle={{ backgroundColor: "#222", color: "white" }} />
            <Legend wrapperStyle={{ fontSize: "10px" }} />
            <Line type="monotone" dataKey="x" stroke="cyan" dot={{ r: 1 }} />
            <Line type="monotone" dataKey="y" stroke="lime" dot={{ r: 1 }} />
            <Line type="monotone" dataKey="z" stroke="magenta" dot={{ r: 1 }} />
          </LineChart>
        </ResponsiveContainer>
      ) : (
        <p style={{ color: "white", fontSize: "12px" }}>Loading...</p>
      )}
    </div>
  );
};

export default PositionGraph;
