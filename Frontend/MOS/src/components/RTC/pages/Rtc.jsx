import { useState, useEffect } from "react";
import "../styles/rtc.css"; // External CSS for styling

export default function CommandingModule() {
  const [scheduleSets, setScheduleSets] = useState([]); // Stores available schedule sets
  const [selectedSchedule, setSelectedSchedule] = useState(""); // Selected schedule set
  const [uplinkedCommands, setUplinkedCommands] = useState([]); // Stores uplinked commands
  const [downlinkedResponses, setDownlinkedResponses] = useState([]); // Stores received responses
  const [loading, setLoading] = useState(false);

  // Fetch schedule sets from API on load
  useEffect(() => {
    fetchScheduleSets();
  }, []);

  const fetchScheduleSets = async () => {
    try {
      const response = await fetch("http://localhost:8000/schedule-planner/fetch-schedule-sets");
      const data = await response.json();
      setScheduleSets(data.schedule_sets || []);
    } catch (error) {
      console.error("Error fetching schedule sets:", error);
    }
  };

  // Handles dropdown selection
  const handleScheduleChange = (event) => {
    setSelectedSchedule(event.target.value);
  };

  // Sends command to API
  const sendCommand = async () => {
    if (!selectedSchedule) {
      alert("Please select a schedule set before sending.");
      return;
    }

    setLoading(true);
    try {
      const response = await fetch("http://localhost:8000/mqtt/command", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ schedule: selectedSchedule }),
      });

      const data = await response.json();

      // Store the command and response
      setUplinkedCommands([...uplinkedCommands, selectedSchedule]);
      setDownlinkedResponses([...downlinkedResponses, data.response || "No response"]);

    } catch (error) {
      console.error("Error sending command:", error);
    }
    setLoading(false);
  };

  return (
    <div className="commanding-container">
      <h2>Commanding Module</h2>

      {/* Dropdown Selection */}
      <div className="command-selection">
        <label>Select a Schedule Set:</label>
        <select value={selectedSchedule} onChange={handleScheduleChange}>
          <option value="">-- Choose a schedule --</option>
          {scheduleSets.map((set, index) => (
            <option key={index} value={set}>
              {set}
            </option>
          ))}
        </select>
        <button onClick={sendCommand} disabled={loading}>
          {loading ? "Sending..." : "Send Command"}
        </button>
      </div>

      {/* Uplinked Commands */}
      <div className="command-log">
        <h3>Uplinked Commands</h3>
        {uplinkedCommands.length > 0 ? (
          <ul>
            {uplinkedCommands.map((cmd, index) => (
              <li key={index}>{cmd}</li>
            ))}
          </ul>
        ) : (
          <p>No commands uplinked yet.</p>
        )}
      </div>

      {/* Downlinked Responses */}
      <div className="response-log">
        <h3>Downlinked Responses</h3>
        {downlinkedResponses.length > 0 ? (
          <ul>
            {downlinkedResponses.map((resp, index) => (
              <li key={index}>{resp}</li>
            ))}
          </ul>
        ) : (
          <p>No responses received yet.</p>
        )}
      </div>
    </div>
  );
}