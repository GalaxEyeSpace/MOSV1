import React from "react";

const CommandsLog = ({ commandsData }) => {
  return (
    <div className="log-window">
      <div className="log-title">Uplink Commands</div>
      {commandsData.map((cmd, idx) => {
        const localTime = new Date(cmd.timestamp).toLocaleTimeString("en-US", {
          hour12: false,
        });
        return (
          <div key={idx} className="log-entry">
            <span className="timestamp">{localTime}</span>
            <span>{cmd.command}</span>
          </div>
        );
      })}
    </div>
  );
};

export default CommandsLog;
