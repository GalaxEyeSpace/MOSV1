import React, { useEffect, useState } from "react";
import styled from "styled-components";

// Styled Components for Layout
const Container = styled.div`
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 30px;
  height: 100vh;
  font-family: Arial, sans-serif;
`;

const Column = styled.div`
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 40px;
`;

const Block = styled.div`
  width: 180px;
  height: 60px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 16px;
  font-weight: bold;
  border-radius: 8px;
  border: 2px solid #4CAF50;
  background-color: ${(props) => props.color};
  color: white;
  transition: background-color 0.5s ease;
`;

const CenterBlock = styled.div`
  width: 50px;
  height: 300px;
  background-color:rgb(159, 130, 71);
  border-radius: 10px;
`;

const Arrow = styled.div`
  font-size: 24px;
  font-weight: bold;
  color: black;
`;

// Function to generate a random temperature between 10°C - 42°C
const getRandomTemperature = () => Math.floor(Math.random() * (45 - 10 + 1)) + 10;

// Function to determine block color based on temperature
const getColor = (temp) => {
  if (temp >= 75) return "red"; // Critical
  if (temp >= 45) return "orange"; // Warning
  return "green"; // Normal
};

const Temperature = () => {
  const [temperatures, setTemperatures] = useState(
    Array(6).fill(0).map(() => getRandomTemperature()) // Generate 6 random temperatures initially
  );

  useEffect(() => {
    const updateTemperature = () => {
      setTemperatures(Array(6).fill(0).map(() => getRandomTemperature()));
    };

    const interval = setInterval(updateTemperature, 1000); // Update every second
    return () => clearInterval(interval);
  }, []);

  return (
    <Container>
      {/* Left Column */}
      <Column>
        <Block color={getColor(temperatures[0])}>Level 0 ({temperatures[0]}°C)</Block>
        <Block color={getColor(temperatures[1])}>Level 1 ({temperatures[1]}°C)</Block>
        <Block color={getColor(temperatures[2])}>Level 2 ({temperatures[2]}°C)</Block>
      </Column>
      
      {/* Arrows and Center Block */}
      <Column>
        <Arrow>⬅️</Arrow>
        <Arrow>⬅️</Arrow>
        <Arrow>⬅️</Arrow>
      </Column>

      {/* Central Block */}
      <CenterBlock> Temp</CenterBlock>

      {/* Arrows and Right Column */}
      <Column>
        <Arrow>➡️</Arrow>
        <Arrow>➡️</Arrow>
        <Arrow>➡️</Arrow>
      </Column>

      {/* Right Column */}
      <Column>
        <Block color={getColor(temperatures[3])}>Antenna Solar Panel ({temperatures[3]}°C)</Block>
        <Block color={getColor(temperatures[4])}>Comms ({temperatures[4]}°C)</Block>
        <Block color={getColor(temperatures[5])}>MSI ({temperatures[5]}°C)</Block>
      </Column>
    </Container>
  );
};

export default Temperature;
