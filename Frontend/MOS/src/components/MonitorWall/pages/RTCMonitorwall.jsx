import React, { useState, useEffect, useRef } from "react";
import "./styles.css";

// Components
import CommStatusCard from "./components/CommStatusCard";
import GroundStationCard from "./components/GroundStationCard";
import TelemetryLog from "./components/TelemetryLog";
import CommandsLog from "./components/CommandsLog";

// Data
import fiveGSData from "./data/fiveGSData.json";

function RTCMonitorwall() {
  // State
  const [currentTime, setCurrentTime] = useState(new Date());
  const [stations, setStations] = useState([]);
  const [telemetry, setTelemetry] = useState([]);
  const [commands, setCommands] = useState([]);

  // Ref to the telemetry log window for auto-scrolling
  const telemetryLogRef = useRef(null);

  useEffect(() => {
    // On mount, load station data and initial logs
    setStations(fiveGSData.groundStations);
    setTelemetry(fiveGSData.initialTelemetry);
    setCommands(fiveGSData.initialCommands);

    // Update the current time every second
    const clockInterval = setInterval(() => {
      setCurrentTime(new Date());
    }, 1000);

    // Generate commands every 10s for demonstration
    const cmdInterval = setInterval(() => {
      addRandomCommand();
    }, 10000);

    return () => {
      clearInterval(clockInterval);
      clearInterval(cmdInterval);
    };
  }, []);

  // Telemetry generation: 3 logs/sec if station is in pass
  useEffect(() => {
    const tmInterval = setInterval(() => {
      generateTelemetry();
    }, 333);
    return () => clearInterval(tmInterval);
  }, [stations, currentTime]);

  // Auto-scroll telemetry window on changes
  useEffect(() => {
    if (telemetryLogRef.current) {
      telemetryLogRef.current.scrollTop = telemetryLogRef.current.scrollHeight;
    }
  }, [telemetry]);

  // Only generate new TM if station is in pass (AOS ≤ now < LOS)
  const generateTelemetry = () => {
    const nowMs = currentTime.getTime();
    const activeStations = stations.filter((st) => {
      const aosMs = new Date(st.aos).getTime();
      const losMs = new Date(st.los).getTime();
      return nowMs >= aosMs && nowMs < losMs;
    });
    if (activeStations.length === 0) return;

    const newTM = activeStations.map((st) => ({
      timestamp: new Date().toISOString(),
      message: getRandomTMMessage(st.name),
    }));
    setTelemetry((prev) => [...prev, ...newTM]);
  };

  const getRandomTMMessage = (stationName) => {
    const messages = [
      "Temperature stable at 22C",
      "Battery at 80% capacity",
      "Nominal attitude control",
      "Signal locked",
      "Minor vibration detected",
      "Radiation levels normal",
      "Payload data collection stable",
    ];
    const idx = Math.floor(Math.random() * messages.length);
    return `TM (${stationName}): ${messages[idx]}`;
  };

  // Example commands generation
  const addRandomCommand = () => {
    const possibleCmds = [
      "TC: Adjust antenna +3 deg",
      "TC: Switch to backup power",
      "TC: Start thermal calibration",
      "TC: Engage reaction wheels",
      "TC: Rotate solar array",
    ];
    const idx = Math.floor(Math.random() * possibleCmds.length);
    const newCmd = {
      timestamp: new Date().toISOString(),
      command: possibleCmds[idx],
    };
    setCommands((prev) => [...prev, newCmd]);
  };

  // Find the single "active" station, if any
  const findActiveStation = () => {
    const nowMs = currentTime.getTime();
    // If multiple are in pass, pick the earliest LOS or something
    let active = null;
    let minLOS = Number.MAX_SAFE_INTEGER;
    stations.forEach((st) => {
      const aosMs = new Date(st.aos).getTime();
      const losMs = new Date(st.los).getTime();
      if (nowMs >= aosMs && nowMs < losMs) {
        // It's in pass
        if (losMs < minLOS) {
          minLOS = losMs;
          active = st;
        }
      }
    });
    return active;
  };

  // Find the next upcoming station (earliest AOS that is still future)
  const findNextStation = () => {
    const nowMs = currentTime.getTime();
    let next = null;
    let minDiff = Number.MAX_SAFE_INTEGER;
    stations.forEach((st) => {
      const aosMs = new Date(st.aos).getTime();
      const diff = aosMs - nowMs;
      if (diff > 0 && diff < minDiff) {
        minDiff = diff;
        next = st;
      }
    });
    return next;
  };

  const activeStation = findActiveStation();
  const nextStation = !activeStation ? findNextStation() : null;

  // For highlighting "most imminent" station card
  // (earliest future pass if not active)
  const findMostImminentStationId = () => {
    if (activeStation) return activeStation.id; // or you can skip highlighting if active
    if (!nextStation) return null;
    return nextStation.id;
  };
  const mostImminentId = findMostImminentStationId();

  // Clocks
  const localTimeStr = currentTime.toLocaleTimeString("en-US", { hour12: false });
  const utcTimeStr = currentTime.toUTCString().split(" ")[4]; // HH:MM:SS

  return (
    <div className="app-container">
      {/* HEADER */}
      <header className="app-header">
        <div className="header-left">
          <h1>Mission Control</h1>
        </div>
        <div className="header-right">
          <div className="big-clock">{localTimeStr}</div>
          <div className="small-clock">UTC: {utcTimeStr}</div>
        </div>
      </header>

      {/* MAIN CONTENT */}
      <div className="app-main">
        {/* BIG COMMUNICATION STATUS CARD */}

        {/* Ground Stations */}
        <div className="ground-stations-container">
        <CommStatusCard 
          activeStation={activeStation}
          nextStation={nextStation}
          currentTime={currentTime}
        />
          {stations.map((station) => {
            // Evaluate pass state
            const aosMs = new Date(station.aos).getTime();
            const losMs = new Date(station.los).getTime();
            const nowMs = currentTime.getTime();
            const isEnded = nowMs >= losMs;
            const isActivePass = nowMs >= aosMs && nowMs < losMs;
            // We still generate a random 1-100 signal for these cards
            // but the big card does a separate 60-100 if active
            const signalStrength = isActivePass
              ? Math.floor(Math.random() * 100) + 1
              : 0;

            return (
              <GroundStationCard
                key={station.id}
                station={station}
                currentTime={currentTime}
                isMostImminent={station.id === mostImminentId}
                isEnded={isEnded}
                signalStrength={signalStrength}
              />
            );
          })}
        </div>


        {/* Logs */}
        <div className="logs-container">
          <div className="log-title">Downlink Telemetry</div>
          <div className="log-window" ref={telemetryLogRef}>
            {telemetry.map((tm, idx) => {
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

          <CommandsLog commandsData={commands} />
        </div>
      </div>
    </div>
  );
}

export default RTCMonitorwall;
