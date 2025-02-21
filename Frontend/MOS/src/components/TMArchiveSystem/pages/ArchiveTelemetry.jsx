// TMArchiveSystem/pages/ArchiveTelemetry.js
import React from "react";
import "../styles/archivetelemetry.css";
import SolarVsConsumedGraph from "./power/SolarVsConsumedGraph";
import StorageUsage from "./power/StorageUsage";
import EnergySummary from "./power/EnergySummary";
import PowerEfficiency from "./power/PowerEfficiency";
import ThresholdAlerts from "./power/ThresholdAlerts";
import VelocityVisualization from "./VelocityVisualization";
import PositionTrend from "./PositionTrend";
import Temperature from "./Temperature";

const ArchiveTelemetry = () => {
  return (
     <>
     <div className="telemetry-container">
       <SolarVsConsumedGraph />
      </div>
      <div className="telemetry1-container">
       <StorageUsage />
      </div>
      <div className="telemetry2-container">
       <EnergySummary />
      </div>
      <div className="telemetry3-container">
       <PowerEfficiency />
      </div>
      <div className="telemetry4-container">
       <ThresholdAlerts />
      </div>
      <div className="telemetry6-container">
        <VelocityVisualization />
      </div>
      <div className="telemetry9-container">
        <PositionTrend />
      </div>
      <div className="telemetry10-container">
        <Temperature />
      </div>
     </>
  );
};

export default ArchiveTelemetry;



