import { useState, useEffect } from "react";
import "../styles/planner.css"; // External CSS

export default function Planner() {
  const [satelliteInfo, setSatelliteInfo] = useState(null);
  const [passageInfo, setPassageInfo] = useState([]);
  const [nextAOS, setNextAOS] = useState(null);
  const [nextLOS, setNextLOS] = useState(null);
  const [aosCountdown, setAosCountdown] = useState("N/A");
  const [losCountdown, setLosCountdown] = useState("N/A");
  const [currentUTCTime, setCurrentUTCTime] = useState(new Date().toISOString());

  // Ground Station Mapping
  const groundStationMap = {
    "b485a02f3fe060052f6dc55d5f003284": "Iceland-01",
    "c7282b7a69df20d3a3d5d9d6d5de1088": "Iceland-02",
    "1899d2210bbb82d9e6837443aef0b5cd": "Iceland-03",
    "7b7db627a6f258717d80cca03f1d6018": "Chile-01",
    "39beffa9ad843190331e4f3dfd0efc38": "Mexico-02",
    "06b4439e3fd126af7ff6e7e245b2a8f4": "New Zealand-04",
    "797e80528873ead9622376f15f5cfcdc": "South Africa-01",
    "41fc8cc49429b64353173d662c719aa5": "New Zealand-03",
    "58b1ab9d2061b9029794c3baffd53a4c": "Mexico-01",
    "b4e15b7ffad118396de5afc5f4052219": "South Africa-02",
    "2c6673eeb9a0aad6ec72cf1c196fdcbd": "Chile-02",
    "89ecf0ea4f0f5f0f521c16854ee1c30c": "Chile-03",
  };

  useEffect(() => {
    fetchData("leaf/fetch-sat/", setSatelliteInfo);
    fetchData("leaf/fetch-schedule/", setPassageInfo);
  }, []);

  const fetchData = async (endpoint, setter) => {
    try {
      const response = await fetch(`http://localhost:8000/${endpoint}`);
      const data = await response.json();
      setter(data);
    } catch (error) {
      console.error(`Error fetching ${endpoint}:`, error);
    }
  };

  // Update UTC Clock
  useEffect(() => {
    const interval = setInterval(() => {
      setCurrentUTCTime(new Date().toISOString());
    }, 1000);
    return () => clearInterval(interval);
  }, []);

  useEffect(() => {
    if (passageInfo.length > 0) {
      const nowUTC = new Date().getTime(); // Current time in UTC
      const sortedPassages = passageInfo
        .filter((passage) => new Date(passage.aos).getTime() > nowUTC) // Only upcoming AOS
        .sort((a, b) => new Date(a.aos).getTime() - new Date(b.aos).getTime());

      if (sortedPassages.length > 0) {
        setNextAOS(new Date(sortedPassages[0].aos).getTime());
        setNextLOS(new Date(sortedPassages[0].los).getTime());
      } else {
        setNextAOS(null);
        setNextLOS(null);
      }
    }
  }, [passageInfo]);

  useEffect(() => {
    const updateCountdowns = () => {
      const nowUTC = new Date().getTime();

      if (nextAOS && nextAOS > nowUTC) {
        setAosCountdown(formatCountdown(nextAOS - nowUTC));
      } else {
        setAosCountdown("00:00:00");
      }

      if (nextLOS && nextLOS > nowUTC) {
        setLosCountdown(formatCountdown(nextLOS - nowUTC));
      } else {
        setLosCountdown("00:00:00");
      }
    };

    if (nextAOS || nextLOS) {
      updateCountdowns();
      const interval = setInterval(updateCountdowns, 1000);
      return () => clearInterval(interval);
    }
  }, [nextAOS, nextLOS]);

  const formatCountdown = (ms) => {
    if (ms <= 0) return "00:00:00";

    const totalSeconds = Math.floor(ms / 1000);
    const hours = Math.floor(totalSeconds / 3600);
    const minutes = Math.floor((totalSeconds % 3600) / 60);
    const seconds = totalSeconds % 60;

    return `${hours.toString().padStart(2, "0")}:${minutes
      .toString()
      .padStart(2, "0")}:${seconds.toString().padStart(2, "0")}`;
  };

  const formatDateTimeUTC = (dateString) => {
    return dateString ? new Date(dateString).toISOString().replace("T", " ").split(".")[0] + " UTC" : "N/A";
  };

  return (
    <div className="planner-container">
      <div className="table-container">
        <h2>Scheduled Passes</h2>
        <table className="table">
          <thead>
            <tr>
              <th>Ground Station</th>
              <th>Max Elevation</th>
              <th>Status</th>
              <th>AOS</th>
              <th>LOS</th>
              <th>Policy</th>
            </tr>
          </thead>
          <tbody>
            {passageInfo.length > 0 ? (
              passageInfo.map((passage) => (
                <tr key={passage.passage_id}>
                  <td>{groundStationMap[passage.ground_station_id] || passage.ground_station_id}</td>
                  <td>{passage.max_elevation ?? "N/A"}</td>
                  <td>{passage.passage_status ?? "N/A"}</td>
                  <td>{formatDateTimeUTC(passage.aos)}</td>
                  <td>{formatDateTimeUTC(passage.los)}</td>
                  <td>{passage.policy_type ?? "N/A"}</td>
                </tr>
              ))
            ) : (
              <tr>
                <td colSpan="6">Loading passage schedule...</td>
              </tr>
            )}
          </tbody>
        </table>
      </div>

      <div className="sidebar">
        <h2>Satellite Info</h2>
        {satelliteInfo ? (
          <p>
            <strong>Satellite ID:</strong> {satelliteInfo.response?.satelliteID ?? "N/A"}
            <br />
            <strong>NORAD ID:</strong> {satelliteInfo.response?.noradID ?? "N/A"}
          </p>
        ) : (
          <p>Loading satellite data...</p>
        )}

        <h2>Current UTC Time</h2>
        <p><strong>UTC Time:</strong> {currentUTCTime.replace("T", " ").split(".")[0]}</p>

        <h2>Time to Next Pass</h2>
        <p><strong>Next AOS:</strong> {nextAOS ? formatDateTimeUTC(new Date(nextAOS)) : "N/A"}</p>
        <p><strong>Countdown to AOS:</strong> {aosCountdown}</p>
        <p><strong>Next LOS:</strong> {nextLOS ? formatDateTimeUTC(new Date(nextLOS)) : "N/A"}</p>
        <p><strong>Countdown to LOS:</strong> {losCountdown}</p>
      </div>
    </div>
  );
}