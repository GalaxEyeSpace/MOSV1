import React from "react";
import { useNavigate } from "react-router-dom"; // For navigation
import "../styles/Home.css"; // Custom styling


const Home = () => {
  const navigate = useNavigate();

  const blocks = [
    { name: "Ground Station Planner", path: "/planner" },
    { name: "Real-Time Communication", path: "/rtc" },
    { name: "Scheduler", path: "/scheduler" },
    { name: "Monitor Wall", path: "/monitor" },
    { name: "System Console (Real-Time)", path: "/system-realtime" },
    { name: "System Console (Archive)", path: "/system-archive" },
    { name: "Astrodynamics Console (Real-Time)", path: "/astro-realtime" },
    { name: "Astrodynamics Console (Archive)", path: "/astro-archive" },
  ];

  return (
    <div className="home-container">
      {/* Header */}
      <header className="header">
        <h3>MOS Demo</h3>
      </header>

      {/* Grid of Blocks */}
      <div className="grid-container">
        {blocks.map((block, index) => (
          <div
            key={index}
            className="grid-item"
            onClick={() => navigate(block.path)}
          >
            <span>{block.name}</span>
          </div>
        ))}
      </div>
    </div>
  );
};

export default Home;

