// TMArchiveSystem/pages/ArchiveTelemetry.js
import React from "react";
import MissionDetails from "./MissionDetails";
import PowerDetails from "./PowerDetails";
import StorageDetails from "./StorageDetails";
import VelocityDetails from "./VelocityDetails";
import PositionsDetails from "./PositionDetails";
import OmegaDetails from "./OmegaDetails";
import ADCSDetails from "./ADCSDetails";
import "../styles/archiveTelemetry.css";

const ArchiveTelemetry = () => {
  return (
    <div className="telemetry-dashboard">
      {/* 🔹 Header */}
      <header className="header">
        <h1>TM ARCHIVE SYSTEM DEMO</h1>
      </header>

      {/* 📡 Mission Details Section */}
      <section className="mission-section">
        <MissionDetails />
      </section>

      {/* 📊 Main Data Grid (Two Rows - 6 Components) */}
      <div className="main-content">
        {/* Row 1 */}
        <PowerDetails />
        <StorageDetails />
        <VelocityDetails />

        {/* Row 2 */}
        <PositionsDetails />
        <OmegaDetails />
        <ADCSDetails />
      </div>
    </div>
  );
};

export default ArchiveTelemetry;
