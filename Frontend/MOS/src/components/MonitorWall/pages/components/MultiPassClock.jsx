import React, { useMemo } from "react";

const secondsToHMS = (sec) => {
  if (sec < 0) return "00:00:00";
  const hrs = Math.floor(sec / 3600);
  const mins = Math.floor((sec % 3600) / 60);
  const secs = Math.floor(sec % 60);
  return [hrs, mins, secs]
    .map((v) => String(v).padStart(2, "0"))
    .join(":");
};

const MultiPassClock = ({ passes, currentTime }) => {
  const nowMs = currentTime.getTime();

  // We'll produce an array of clocks, each describing the pass ID and time left
  const passClocks = useMemo(() => {
    return passes.map((ps) => {
      const aosMs = new Date(ps.aos).getTime();
      const losMs = new Date(ps.los).getTime();
      const timeToAOS = (aosMs - nowMs) / 1000; // in seconds
      const timeToLOS = (losMs - nowMs) / 1000; // in seconds

      let label = "";
      let displayTime = "";
      if (timeToAOS > 0) {
        // not started
        label = "Pass " + ps.passId + " (AOS in)";
        displayTime = secondsToHMS(timeToAOS);
      } else if (timeToLOS > 0) {
        // in progress
        label = "Pass " + ps.passId + " (LOS in)";
        displayTime = secondsToHMS(timeToLOS);
      } else {
        // ended
        label = "Pass " + ps.passId + " ended";
        displayTime = "00:00:00";
      }

      return {
        passId: ps.passId,
        label,
        displayTime
      };
    });
  }, [passes, nowMs]);

  return (
    <div className="station-clocks">
      {passClocks.map((pc) => (
        <div key={pc.passId} className="pass-clock">
          {pc.label}: {pc.displayTime}
        </div>
      ))}
    </div>
  );
};

export default MultiPassClock;
