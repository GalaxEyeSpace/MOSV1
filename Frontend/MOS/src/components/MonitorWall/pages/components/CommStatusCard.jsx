import React, { useState, useEffect } from "react";

// Utility function to convert seconds -> "HH:MM:SS"
function secondsToHMS(sec) {
  if (sec < 0) return "00:00:00";
  const hrs = Math.floor(sec / 3600);
  const mins = Math.floor((sec % 3600) / 60);
  const secs = Math.floor(sec % 60);
  return [hrs, mins, secs]
    .map((v) => String(v).padStart(2, "0"))
    .join(":");
}

const CommStatusCard = ({
  activeStation,    // A station object if in pass, or null
  nextStation,      // The soonest upcoming station, or null
  currentTime
}) => {
  // Keep a random signal strength state (60–100 if active, else 0)
  const [signalStrength, setSignalStrength] = useState(0);

  // If we have an active station, we recalc a random strength every second
  useEffect(() => {
    let interval = null;
    if (activeStation) {
      interval = setInterval(() => {
        const randomVal = Math.floor(Math.random() * 41) + 60; // 60-100
        setSignalStrength(randomVal);
      }, 1000);
    } else {
      // No active station => reset to 0
      setSignalStrength(0);
    }
    return () => {
      if (interval) clearInterval(interval);
    };
  }, [activeStation]);

  // If there's an active station, compute time to LOS
  const nowMs = currentTime.getTime();
  let losStr = "";
  if (activeStation) {
    const losMs = new Date(activeStation.los).getTime();
    const timeToLOS = (losMs - nowMs) / 1000;
    losStr = secondsToHMS(timeToLOS);
  }

  // If no active station, show next station info (time to AOS)
  let nextStationStr = "";
  if (!activeStation && nextStation) {
    const aosMs = new Date(nextStation.aos).getTime();
    const timeToAOS = (aosMs - nowMs) / 1000;
    nextStationStr = `Next GS: ${nextStation.name} in ${secondsToHMS(timeToAOS)}`;
  }

  // Rendering:
  // - If activeStation is defined => big neon box with station + LOS + random signal
  // - Else => "OFFLINE" + smaller text with next station info
  return (
    <div className="comm-status-card">
      {activeStation ? (
        <div className="comm-active">
          <h2 className="comm-station-name">{activeStation.name}</h2>
          <div className="comm-details">
            <span>LOS in: {losStr}</span>
            <span>Signal Strength: {signalStrength}</span>
          </div>
        </div>
      ) : (
        <div className="comm-offline">
          <h1 className="offline-text">OFFLINE</h1>
          {nextStationStr && (
            <div className="next-station-info">{nextStationStr}</div>
          )}
        </div>
      )}
    </div>
  );
};

export default CommStatusCard;
