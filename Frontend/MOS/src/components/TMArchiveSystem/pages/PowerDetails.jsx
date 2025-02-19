// TMArchiveSystem/pages/PowerDetails.js
import React, { useEffect, useState } from "react";
import { fetchPowerTelemetry } from "../services/api";
import SolarVsConsumedGraph from "./power/SolarVsConsumedGraph";
import StorageUsage from "./power/StorageUsage";
import ThresholdAlerts from "./power/ThresholdAlerts";
import PowerEfficiency from "./power/PowerEfficiency";
import FuturePowerPrediction from "./power/FuturePowerPrediction";
import EnergySummary from "./power/EnergySummary";
import "../styles/powerDetails.css";

const PowerDetails = () => {
  const [powerData, setPowerData] = useState([]);

  useEffect(() => {
    const getData = async () => {
      const data = await fetchPowerTelemetry();
      setPowerData(data);
    };
    getData();
  }, []);

  return (
    <div className="power-container">
      <h2>⚡ Power Insights</h2>

      <div className="power-grid">
        {/* Large Graph - Vis.js */}
        <div className="full-width">
          <SolarVsConsumedGraph data={powerData} />
        </div>

        {/* Smaller Components in Grid */}
        <div className="medium">
          <StorageUsage data={powerData} />
        </div>
        <div className="small">
          <PowerEfficiency data={powerData} />
        </div>
        <div className="small">
          <ThresholdAlerts data={powerData} />
        </div>
        <div className="medium">
          <FuturePowerPrediction data={powerData} />
        </div>

        {/* Summary Section */}
        <div className="full-width compact">
          <EnergySummary data={powerData} />
        </div>
      </div>
    </div>
  );
};

export default PowerDetails;
