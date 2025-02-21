import React from "react";
import PositionFlowGraph from "./OmegaFlowGraph";
import VelocityFlowGraph from "./VelocityFlowGraph";
import OmegaFlowGraph from "./OmegaFlowGraph";
import "../styles/realAstro.css"
import TaskManager from "../pages/TaskManager"
import PowerHeading from "./PowerHeading";
import VelocityHeading from "./VelocityHeading";
import OmegaHeading from "./OmegaHeading";


const TMRealSystem = () => {
  return (
  <>
    <div className="telemetry2">
       <PositionFlowGraph />
   </div>
   <div className="telemetry3">
       <VelocityFlowGraph />
   </div>
   <div className="telemetry4">
       <OmegaFlowGraph />
   </div>
   <div className="telemetry5">
       <TaskManager />
   </div>
   <div className="telemetry6">
       <PowerHeading />
   </div>
   <div className="telemetry7">
       <VelocityHeading />
   </div>
   <div className="telemetry8">
       <OmegaHeading />
   </div>
  </>
  );
};

export default TMRealSystem;
