import React from "react";
import PowerFlowGraph from "./pages/PowerFlowGraph";
import VelocityFlowGraph from "./pages/VelocityFlowgraph";
import PositionFlowGraph from "./pages/PositionFlowGraph";
import OmegaFlowGraph from "./pages/OmegaFlowGraph";
import "./styles/realSystem.css"
import PowerHeading from "../TMRealAstro/pages/PowerHeading";
import PositionHeading from "./pages/PositionHeading";
import VelocityHeading from "../TMRealAstro/pages/VelocityHeading";
import OmegaHeading from "../TMRealAstro/pages/OmegaHeading";
import TemperatureGraph from "./pages/Temperature";

const TMRealSystem = () => {
  return (
  <>
   <div className="telemetry1">
       <PowerFlowGraph />
   </div>
   {/* <div className="telemetry2">
       <PositionFlowGraph />
   </div>
   <div className="telemetry3">
       <VelocityFlowGraph />
   </div>
   <div className="telemetry4">
       <OmegaFlowGraph />
   </div>
   <div className="telemetry5">
       <PowerHeading />
   </div>
   <div className="telemetry6">
       <PositionHeading />
   </div>
   <div className="telemetry7">
       <VelocityHeading />
   </div>
   <div className="telemetry8">
       <OmegaHeading />
   </div> */}
   <div className="telemetry2">
       <TemperatureGraph />
   </div>
  </>
  );
};

export default TMRealSystem;
