import React, { useEffect, useState } from "react";
import {
  PieChart,
  Pie,
  Cell,
  Tooltip,
  Legend,
  ResponsiveContainer,
} from "recharts";


const StorageUsage = () => {
  const [storageData, setStorageData] = useState([]);

  useEffect(() => {
    fetch("http://localhost:8000/telemetry/get-data/?table=power&start_time=2024-12-05T09:50:59.000Z&end_time=2024-12-05T10:40:58.000Z")
      .then(response => response.json())
      .then(data => {
        console.log("Fetched Storage Data:", data);

        if (Array.isArray(data)) {
          // ✅ Aggregate Data (Total Storage vs. Total Consumed)
          let totalStorage = 0;
          let totalConsumed = 0;

          data.forEach((item) => {
            totalStorage += parseFloat(item.storage);
            totalConsumed += parseFloat(item.power_consumed);
          });

          // ✅ Format Data for Pie Chart
          const formattedData = [
            { name: "Stored Power", value: totalStorage },
            { name: "Consumed Power", value: totalConsumed },
          ];

          setStorageData(formattedData);
        } else {
          console.error("Unexpected API response format:", data);
        }
      })
      .catch(error => console.error("Error fetching telemetry data:", error));
  }, []);

  const COLORS = ["#0088FE", "#FF8042"]; // Blue = Storage, Orange = Used

  return (
    <div style={{ width: "90%", margin: "auto", padding: "20px" }}>
      {storageData.length > 0 ? (
        <ResponsiveContainer width="100%" height={400}>
          <PieChart>
            <Pie
              data={storageData}
              cx="50%"
              cy="50%"
              innerRadius={80}
              outerRadius={120}
              fill="#8884d8"
              paddingAngle={3}
              dataKey="value"
              label
            >
              {storageData.map((entry, index) => (
                <Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />
              ))}
            </Pie>
            <Tooltip contentStyle={{ backgroundColor: "#2a2a2a", color: "white" }} />
            <Legend verticalAlign="bottom" height={36} />
          </PieChart>
        </ResponsiveContainer>
      ) : (
        <p>Loading...</p>
      )}
    </div>
  );
};

export default StorageUsage;
