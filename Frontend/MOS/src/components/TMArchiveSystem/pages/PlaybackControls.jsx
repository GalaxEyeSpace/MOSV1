// TMArchiveSystem/pages/PlaybackControls.js
import React from "react";
import "../styles/playbackControls.css";

const PlaybackControls = () => {
  return (
    <div className="playback-container">
      <h2>⏯ Playback Controls</h2>
      <button>⏮</button>
      <button>⏯</button>
      <button>⏭</button>
    </div>
  );
};

export default PlaybackControls;
