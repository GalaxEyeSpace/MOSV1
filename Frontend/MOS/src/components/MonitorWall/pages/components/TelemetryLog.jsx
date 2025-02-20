import React, { useRef, useEffect } from "react";
import "../styles.css";

const TelemetryLog = ({ telemetryData }) => {
  const logBodyRef = useRef(null);

  // Auto-scroll to bottom when new telemetry arrives
  useEffect(() => {
    if (logBodyRef.current) {
      logBodyRef.current.scrollTop = logBodyRef.current.scrollHeight;
    }
  }, [telemetryData]);

  return (
    <div className="log-window">
      {/* Fixed heading: not part of the scroll */}
      <div className="log-header">Downlink Telemetry</div>

      {/* Scrollable body */}
      <div className="log-body" ref={logBodyRef}>
        {telemetryData.map((tm, idx) => {
          const localTime = new Date(tm.timestamp).toLocaleTimeString("en-US", {
            hour12: false,
          });
          return (
            <div key={idx} className="log-entry">
              <span className="timestamp">{localTime}</span>
              <span>{tm.message}</span>
            </div>
          );
        })}
      </div>
    </div>
  );
};

export default TelemetryLog;
