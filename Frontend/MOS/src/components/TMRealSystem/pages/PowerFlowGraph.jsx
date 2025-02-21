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
import styled from "styled-components";

const GraphContainer = styled.div`
  width: 600px;
  height: 450px;
  padding: 20px;
  background: #222;
  border-radius: 10px;
`;

const PowerFlowGraph = () => {
  const [graphData, setGraphData] = useState([]);

  const fetchTelemetryData = async () => {
    try {
      const endTime = Date.now(); // Current Time (T)
      const startTime = endTime - 1000; // T - 1 second

      const response = await fetch(
        `http://localhost:8000/telemetry/get-data/?table=power&start_time=${new Date(startTime).toISOString()}&end_time=${new Date(endTime).toISOString()}`
      );
      const data = await response.json();

      let newPoint;
      if (Array.isArray(data) && data.length > 0) {
        const latest = data[data.length - 1];
        newPoint = {
          timestamp: endTime, // Use the current timestamp
          solar: parseFloat(latest.solar),
          storage: parseFloat(latest.storage),
          power_consumed: parseFloat(latest.power_consumed),
          net_power: parseFloat(latest.net_power),
        };
      } else {
        // No data received, push a blank point
        newPoint = {
          timestamp: endTime,
          solar: null,
          storage: null,
          power_consumed: null,
          net_power: null,
        };
      }

      // Keep only the last 20 data points (FIFO - First In, First Out)
      setGraphData((prevData) => [...prevData, newPoint].slice(-20));
    } catch (error) {
      console.error("Error fetching telemetry data:", error);
    }
  };

  useEffect(() => {
    fetchTelemetryData(); // Fetch immediately on mount
    const interval = setInterval(fetchTelemetryData, 1000); // Fetch every second
    return () => clearInterval(interval); // Cleanup on unmount
  }, []);

  return (
    <GraphContainer>
      {graphData.length > 0 ? (
        <ResponsiveContainer width="100%" height="100%">
          <LineChart data={graphData} margin={{ top: 5, right: 10, left: 0, bottom: 5 }}>
            <XAxis
              dataKey="timestamp"
              domain={[Date.now() - 1000, Date.now()]} // Dynamically updates X-axis
              tickFormatter={(tick) => new Date(tick).toLocaleTimeString([], { minute: "2-digit", second: "2-digit" })}
              tick={{ fontSize: 10, fill: "white" }}
              interval="preserveStartEnd"
              tickCount={5} // Show exactly 5 timestamps
            />
            <YAxis tick={{ fontSize: 12, fill: "white" }} />
            <CartesianGrid stroke="#444" strokeDasharray="5 5" />
            <Tooltip contentStyle={{ backgroundColor: "#222", color: "white" }} />
            <Legend wrapperStyle={{ fontSize: "12px", color: "white" }} />

            <Line type="monotone" dataKey="solar" stroke="yellow" dot={true} strokeWidth={2} connectNulls={false} isAnimationActive={false} />
            <Line type="monotone" dataKey="power_consumed" stroke="red" dot={true} strokeWidth={2} connectNulls={false} isAnimationActive={false}/>
            <Line type="monotone" dataKey="storage" stroke="blue" dot={true} strokeWidth={2} connectNulls={false} isAnimationActive={false}/>
            <Line type="monotone" dataKey="net_power" stroke="green" dot={true} strokeWidth={2} connectNulls={false}isAnimationActive={false} />

          </LineChart>
        </ResponsiveContainer>
      ) : (
        <p style={{ color: "white", fontSize: "12px", textAlign: "center" }}>Loading...</p>
      )}
    </GraphContainer>
  );
};

export default PowerFlowGraph;
