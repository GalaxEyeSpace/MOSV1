import React, { useEffect, useState } from "react";
import styled from "styled-components";

const BatteryContainer = styled.div`
  width: 60px;
  height: 120px;
  border: 4px solid white;
  border-radius: 10px;
  position: relative;
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
  background-color: #333;
  overflow: hidden;
`;

const BatteryFill = styled.div`
  width: 100%;
  height: ${(props) => props.level}%;
  background-color: ${(props) => props.color};
  transition: height 0.5s ease-in-out;
`;

const BatteryCap = styled.div`
  width: 25px;
  height: 10px;
  background-color: white;
  border-radius: 3px;
  position: absolute;
  top: -12px;
  left: 50%;
  transform: translateX(-50%);
`;

const BatteryText = styled.div`
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  font-size: 14px;
  font-weight: bold;
  color: white;
`;

const generateFakeStorage = () => Math.random() * 400;

const BatteryIndicator = () => {
  const [storage, setStorage] = useState(generateFakeStorage());

  useEffect(() => {
    const interval = setInterval(() => {
      setStorage(generateFakeStorage());
    }, 2000);
    return () => clearInterval(interval);
  }, []);

  const batteryLevel = Math.min(Math.max((storage / 500) * 100, 0), 100);

  const getBatteryColor = (level) => {
    if (level > 60) return "#4CAF50"; // Green
    if (level > 30) return "#FFA500"; // Orange
    return "#FF3B30"; // Red
  };

  return (
    <div style={{ display: "flex", flexDirection: "column", alignItems: "center" }}>
      <BatteryContainer>
        <BatteryCap />
        <BatteryFill level={batteryLevel} color={getBatteryColor(batteryLevel)} />
        <BatteryText>{Math.round(batteryLevel)}%</BatteryText>
      </BatteryContainer>
      <p style={{ color: "white", marginTop: "10px" }}>Battery</p>
    </div>
  );
};

export default BatteryIndicator;
