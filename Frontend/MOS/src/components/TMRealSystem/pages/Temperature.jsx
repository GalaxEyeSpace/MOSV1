import React, { useEffect, useState } from "react";
import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  Legend,
  ResponsiveContainer,
  Cell
} from "recharts";
import styled from "styled-components";

const GraphContainer = styled.div`
  width: 800px;
  height: 500px;
  padding: 20px;
  background: #222;
  border-radius: 10px;
  margin: 20px auto;
`;

// List of subsystems
const subsystems = ["Subsystem 1", "Subsystem 2", "Subsystem 3", "Subsystem 4", "Subsystem 5", "Subsystem 6"];

// Function to gradually change temperature with small variations
const adjustTemperatureGradually = (prevTemp) => {
  let tempChange = Math.random() * 2 - 1; // Small variation (-1°C to +1°C)
  let newTemp = prevTemp + tempChange;

  // Rarely move temperature to the orange/red zone, but smoothly
  const chance = Math.random();
  if (chance < 0.02) newTemp = 55 + Math.random() * 10; // Rare 2% chance to orange (55-65°C)
  if (chance < 0.005) newTemp = 65 + Math.random() * 30; // Extremely rare 0.5% chance to red (65-95°C)

  return Math.max(0, Math.min(100, newTemp)); // Keep within range
};

// Function to generate telemetry data with smooth transitions
const generateFakeTemperatureData = (prevData) =>
  subsystems.map((name, index) => ({
    name, // Label for the Y-axis (Subsystem names)
    temperature: adjustTemperatureGradually(prevData?.[index]?.temperature || Math.random() * 45),
  }));

const RealTimeTemperatureBarGraph = () => {
  const [temperatureData, setTemperatureData] = useState(generateFakeTemperatureData([]));

  useEffect(() => {
    const interval = setInterval(() => {
      setTemperatureData(generateFakeTemperatureData(temperatureData)); // Keep smooth transition
    }, 2000); // Update every 2 seconds for a more natural effect

    return () => clearInterval(interval);
  }, [temperatureData]); // Dependency on temperatureData for realistic updates

  // Function to determine bar color based on temperature range
  const getBarColor = (temp) => {
    if (temp <= 45) return "green";
    if (temp > 45 && temp <= 55) return "orange";
    return "red"; // Above 55
  };

  return (
    <GraphContainer>
      <h3 style={{ color: "white", textAlign: "center", marginBottom: "10px" }}>
        Real-Time Temperature Comparison (6 Subsystems)
      </h3>
      <ResponsiveContainer width="100%" height="100%">
        <BarChart layout="vertical" data={temperatureData} margin={{ top: 10, right: 20, left: 100, bottom: 10 }}>
          <CartesianGrid stroke="#444" strokeDasharray="5 5" />
          <XAxis type="number" domain={[0, 100]} tick={{ fontSize: 12, fill: "white" }} />
          <YAxis 
            dataKey="name" 
            type="category" 
            tick={{ fontSize: 14, fill: "white" }} 
            width={140} // Ensure space for subsystem names
          />
          <Tooltip contentStyle={{ backgroundColor: "#222", color: "white" }} />
          <Legend wrapperStyle={{ fontSize: "12px", color: "white" }} />

          {/* Single Bar (looping through 6 subsystems with dynamic color) */}
          <Bar dataKey="temperature" barSize={30}> {/* Increased bar width */}
            {temperatureData.map((entry, idx) => (
              <Cell key={`cell-${idx}`} fill={getBarColor(entry.temperature)} />
            ))}
          </Bar>
        </BarChart>
      </ResponsiveContainer>
    </GraphContainer>
  );
};

export default RealTimeTemperatureBarGraph;
