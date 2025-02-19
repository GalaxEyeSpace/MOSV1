import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Home from "./components/Home/pages/Home";
import Planner from "./components/GroundStationPlanner/pages/Planner";
import MonitorWall from "./components/MonitorWall/pages/MonitorWall";
import TMRealSystem from "./components/TMRealSystem/pages/TMRealSystem";
import TMArchiveSystem from "./components/TMArchiveSystem/pages/ArchiveTelemetry";
import TMRealAstro from "./components/TMRealAstro/pages/TMRealAstro";
import TMArchiveAstro from "./components/TMArchiveAstro/pages/TMArchiveAstro";
import Rtc from "./components/RTC/pages/Rtc";
import Scheduler from "./components/Scheduler/pages/Scheduler";

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/planner" element={<Planner/>} />
        <Route path="/rtc" element={<Rtc />} />
        <Route path="/scheduler" element={<Scheduler />} />
        <Route path="/monitor" element={<MonitorWall />} />
        <Route path="/system-realtime" element={<TMRealSystem />} />
        <Route path="/system-archive" element={<TMArchiveSystem />} />
        <Route path="/astro-realtime" element={<TMRealAstro />} />
        <Route path="/astro-archive" element={<TMArchiveAstro />} />
      </Routes>
    </Router>
  );
}

export default App;

