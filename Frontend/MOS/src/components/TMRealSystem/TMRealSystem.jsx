import React from "react";
import styled from "styled-components";
import PowerFlowGraph from "./pages/PowerFlowGraph";
import BatteryIndicator from "./pages/BatteryIndicator";
import "./styles/realSystem.css"

const TMRealSystem = () => {
  return (
  <>
   <div className="telemetry1">
       <PowerFlowGraph />
   </div>
   <div className="telemetry2">
       <BatteryIndicator />
   </div>
  </>
  );
};

export default TMRealSystem;
