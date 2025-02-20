import React, { useMemo } from "react";

// Utility to convert seconds to HH:MM:SS
const secondsToHMS = (sec) => {
  if (sec < 0) return "00:00:00";
  const hrs = Math.floor(sec / 3600);
  const mins = Math.floor((sec % 3600) / 60);
  const secs = Math.floor(sec % 60);
  return [hrs, mins, secs]
    .map((v) => String(v).padStart(2, "0"))
    .join(":");
};

const GroundStationCard = ({
  station,
  currentTime,
  isMostImminent,
  communicationActive,
  signalStrength
}) => {
  const { name, status } = station;
  const aosMs = new Date(station.aos).getTime();
  const losMs = new Date(station.los).getTime();
  const nowMs = currentTime.getTime();

  // Basic pass timing
  const inPass = nowMs >= aosMs && nowMs < losMs; // Are we inside this pass window?
  const ended = nowMs >= losMs;                  // If pass ended
  const timeToAOS = (aosMs - nowMs) / 1000;
  const timeToLOS = (losMs - nowMs) / 1000;

  // Decide pass timing label
  const passInfo = useMemo(() => {
    if (inPass) {
      return `Time to LOS: ${secondsToHMS(timeToLOS)}`;
    } else if (!ended && timeToAOS > 0) {
      return `Time to AOS: ${secondsToHMS(timeToAOS)}`;
    } else {
      return "Pass ended";
    }
  }, [inPass, ended, timeToAOS, timeToLOS]);

  // Build dynamic class name for card:
  // - station-card
  // - station-active if in pass
  // - station-ended if pass ended
  // - (no special class if pass is upcoming but not the earliest => normal)
  let cardClass = "station-card";
  if (inPass) {
    cardClass += " station-active";
  } else if (ended) {
    cardClass += " station-ended";
  }

  return (
    <div className={cardClass}>
      {/* Header row: station name + status */}
      <div className="station-header">
        <div
          className={`station-name ${
            !inPass && isMostImminent ? "station-most-imminent" : ""
          }`}
        >
          {name}
        </div>
        <div className={`status-indicator status-${status}`}>
          {status}
        </div>
      </div>

      {/* AOS / LOS times */}
      <div className="station-detail">
        <strong>AOS:</strong>{" "}
        {new Date(aosMs).toLocaleTimeString("en-US", { hour12: false })}
      </div>
      <div className="station-detail">
        <strong>LOS:</strong>{" "}
        {new Date(losMs).toLocaleTimeString("en-US", { hour12: false })}
      </div>

      {/* Pass timing info in an info-box */}
      <div className="info-box" style={{ marginTop: "6px" }}>
        {passInfo}
      </div>

      {/* Communication info (only show if we're truly in comm window) */}
      {communicationActive && (
        <div className="comm-indicator" style={{ marginTop: "8px" }}>
          <div style={{ marginBottom: "6px" }}>Communication Active!</div>
          <div className="info-box">Signal Strength: {signalStrength}</div>
        </div>
      )}
    </div>
  );
};

export default GroundStationCard;
