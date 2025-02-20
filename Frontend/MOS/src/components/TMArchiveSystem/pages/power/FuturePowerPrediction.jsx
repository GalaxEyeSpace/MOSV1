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

const FuturePowerPrediction = () => {
  const [graphData, setGraphData] = useState([]);
  const [trendData, setTrendData] = useState([]);

  useEffect(() => {
    fetch("http://localhost:8000/telemetry/get-data/?table=power&start_time=2024-12-05T09:50:59.000Z&end_time=2024-12-05T10:40:58.000Z")
      .then(response => response.json())
      .then(data => {
        console.log("Fetched Power Data for Prediction:", data);

        if (Array.isArray(data)) {
          // ✅ Prepare Past Data
          const formattedData = data.map((item) => ({
            timestamp: new Date(item.timestep).toLocaleString(),
            power_consumed: parseFloat(item.power_consumed),
          }));

          setGraphData(formattedData);

          // ✅ Calculate Trendline (Linear Prediction)
          let sumX = 0, sumY = 0, sumXY = 0, sumX2 = 0;
          data.forEach((item, index) => {
            sumX += index;
            sumY += parseFloat(item.power_consumed);
            sumXY += index * parseFloat(item.power_consumed);
            sumX2 += index * index;
          });

          const n = data.length;
          const slope = (n * sumXY - sumX * sumY) / (n * sumX2 - sumX * sumX);
          const intercept = (sumY - slope * sumX) / n;

          // ✅ Generate Future Trendline Data (Next 5 Timesteps)
          const futureData = [];
          for (let i = 0; i < 5; i++) {
            const futureIndex = n + i;
            futureData.push({
              timestamp: `Future ${i + 1}`,
              power_consumed: slope * futureIndex + intercept,
            });
          }

          setTrendData(futureData);
        } else {
          console.error("Unexpected API response format:", data);
        }
      })
      .catch(error => console.error("Error fetching telemetry data:", error));
  }, []);

  return (
    <div style={{ width: "90%", margin: "auto", padding: "20px" }}>
      <h2>Future Power Consumption Prediction</h2>
      {graphData.length > 0 ? (
        <ResponsiveContainer width="100%" height={400}>
          <LineChart>
            <CartesianGrid stroke="#ccc" strokeDasharray="5 5" />
            <XAxis dataKey="timestamp" tick={{ fontSize: 12, fill: "white" }} />
            <YAxis label={{ value: "Power (W)", angle: -90, position: "insideLeft", fill: "white" }} />
            <Tooltip contentStyle={{ backgroundColor: "#2a2a2a", color: "white" }} />
            <Legend verticalAlign="top" height={36} />

            {/* Past Data */}
            <Line type="monotone" data={graphData} dataKey="power_consumed" stroke="red" dot={{ r: 2 }} />

            {/* Predicted Future Data */}
            <Line type="monotone" data={trendData} dataKey="power_consumed" stroke="blue" strokeDasharray="5 5" dot={{ r: 2 }} />
          </LineChart>
        </ResponsiveContainer>
      ) : (
        <p>Loading...</p>
      )}
    </div>
  );
};

export default FuturePowerPrediction;
