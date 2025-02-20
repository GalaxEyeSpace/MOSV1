// TMArchiveSystem/pages/power/SolarVsConsumedGraph.js
import React, { useEffect, useRef } from "react";
import { DataSet, Timeline } from "vis-timeline/standalone";
import "vis-timeline/styles/vis-timeline-graph2d.min.css";
<<<<<<< HEAD
//import "../styles/power/solarVsConsumed.css";
=======
import "../styles/power/solarVsConsumed.css";
>>>>>>> rush

const SolarVsConsumedGraph = ({ data }) => {
  const graphRef = useRef(null);

  useEffect(() => {
    if (!data || data.length === 0) return;

    // Prepare Vis.js Data
    const dataset = new DataSet(
      data.map((entry) => ({
        x: new Date(entry.timestamp),
        y: entry.power_consumed,
        group: "Power Consumed",
      }))
    );

    // Define Graph Options
    const options = {
      start: new Date(data[0].timestamp),
      end: new Date(data[data.length - 1].timestamp),
      showCurrentTime: false,
      width: "100%",
      height: "100%",
      drawPoints: true,
      style: "line",
    };

    // Create Graph
    new Timeline(graphRef.current, dataset, options);
  }, [data]);

  return (
    <div className="solar-graph-container">
      <h3>📈 Solar vs. Consumed Power</h3>
      <div ref={graphRef} className="vis-container"></div>
    </div>
  );
};

export default SolarVsConsumedGraph;
