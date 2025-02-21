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

const generateFakeData = () => ({
  timestamp: new Date().toLocaleTimeString(),
  solar: Math.random() * 500,
  storage: Math.random() * 400,
  power_consumed: Math.random() * 450,
  net_power: Math.random() * 250,
  threshold: 200,
});

const PowerFlowGraph = () => {
  const [graphData, setGraphData] = useState([]);

  useEffect(() => {
    const fetchData = () => {
      const newDataPoint = generateFakeData();
      setGraphData((prevData) => [...prevData, newDataPoint].slice(-20));
    };

    const interval = setInterval(fetchData, 2000);
    return () => clearInterval(interval);
  }, []);

  return (
    <GraphContainer>
      {graphData.length > 0 ? (
        <ResponsiveContainer width="100%" height="100%">
          <LineChart data={graphData} margin={{ top: 5, right: 10, left: 0, bottom: 5 }}>
            <XAxis dataKey="timestamp" tick={{ fontSize: 10, fill: "white" }} />
            <YAxis tick={{ fontSize: 12, fill: "white" }} />
            <CartesianGrid stroke="#444" strokeDasharray="5 5" />
            <Tooltip contentStyle={{ backgroundColor: "#222", color: "white" }} />
            <Legend wrapperStyle={{ fontSize: "12px", color: "white" }} />

            <Line type="monotone" dataKey="solar" stroke="yellow" dot={true} strokeWidth={2} />
            <Line type="monotone" dataKey="power_consumed" stroke="red" dot={true} strokeWidth={2} />
            <Line type="monotone" dataKey="storage" stroke="blue" dot={true} strokeWidth={2} />
            <Line type="monotone" dataKey="net_power" stroke="green" dot={true} strokeWidth={2} />
            <Line type="monotone" dataKey="threshold" stroke="orange" strokeDasharray="5 5" dot={false} strokeWidth={2} />
          </LineChart>
        </ResponsiveContainer>
      ) : (
        <p style={{ color: "white", fontSize: "12px", textAlign: "center" }}>Loading...</p>
      )}
    </GraphContainer>
  );
};

export default PowerFlowGraph;
