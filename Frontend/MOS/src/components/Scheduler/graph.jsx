import React, { useEffect, useRef } from 'react';
import * as vis from 'vis';
import 'vis/dist/vis.css';
import * as satellite from 'satellite.js';

const Graph2D = ({ noteStartTime, noteEndTime, items }) => {
  const containerRef = useRef(null);

  // Example TLE (ISS). Replace with your own if desired.
  const TLE_LINE1 =
    "1 25544U 98067A   24028.55694444  .00016717  00000-0  10270-3 0  9992";
  const TLE_LINE2 =
    "2 25544  51.6412  84.2526 0005717 152.9171 207.2152 15.50013420321769";
  const satrec = satellite.twoline2satrec(TLE_LINE1, TLE_LINE2);

  // Very naive "sunlight" check:
  const isSatelliteSunlit = (date) => {
    const posVel = satellite.propagate(satrec, date);
    if (!posVel.position) return false;

    const gmst = satellite.gstime(date);
    const geo = satellite.eciToGeodetic(posVel.position, gmst);
    const lonDeg = satellite.degreesLong(geo.longitude);

    const offsetHours = lonDeg / 15.0;
    const localDate = new Date(date);
    localDate.setHours(localDate.getUTCHours() + offsetHours);

    const hour = localDate.getHours();
    return hour >= 6 && hour < 18;
  };

  useEffect(() => {
    // Graph2D config
    const options = {
      start: noteStartTime ? new Date(noteStartTime).toISOString() : null,
      end: noteEndTime ? new Date(noteEndTime).toISOString() : null,
      zoomable: true,
      moveable: false,
    };

    // GROUP 0: Main battery line
    const batteryGroup = {
      id: 0,
      content: "Battery Over Time",
      options: {
        drawPoints: { style: "square" },
        shaded: { orientation: "zero" },
      },
    };

    // GROUP 1: Horizontal line at y=70
    // We use style: 'line' so it draws a simple line.
    const horizontalGroup = {
      id: 1,
      content: "Threshold = 70",
      options: {
        style: "line",
        drawPoints: false,
      },
    };

    // Combine the groups into a single DataSet
    const groups = new vis.DataSet([batteryGroup, horizontalGroup]);

    if (!items || items.length === 0) {
      // If no items => show empty chart
      const emptyData = new vis.DataSet([]);
      const graph2d = new vis.Graph2d(
        containerRef.current,
        emptyData,
        groups,
        options
      );
      return () => graph2d.destroy();
    }

    // 1) Sort items by start time
    const sortedItems = [...items].sort(
      (a, b) => new Date(a.start) - new Date(b.start)
    );

    // 2) Earliest & latest item times
    const earliest = new Date(sortedItems[0].start).getTime();
    const latest = new Date(
      sortedItems[sortedItems.length - 1].start
    ).getTime();

    // 3) We'll step in 10-minute increments from earliest -> latest
    const stepMillis = 10 * 60 * 1000; // 10 minutes
    const dataPoints = [];

    // Running battery starts at 100
    let battery = 100;
    let itemIndex = 0; // which item we have processed

    for (let t = earliest; t <= latest; t += stepMillis) {
      const currentTime = new Date(t);

      // Subtract 5 for each unprocessed item whose start <= this time
      while (
        itemIndex < sortedItems.length &&
        new Date(sortedItems[itemIndex].start).getTime() <= t
      ) {
        battery -= 5;
        itemIndex++;
      }

      // If in sunlight and battery < 100 => add +2
      if (isSatelliteSunlit(currentTime) && battery < 100) {
        battery += 2;
      }

      // Add a data point in GROUP 0 (battery line)
      dataPoints.push({
        x: currentTime.toISOString(),
        y: battery,
        group: 0, // battery group
      });
    }

    // 4) Add two points in GROUP 1 for the horizontal line at y=70
    //    We'll draw from earliest time to latest time
    const linePoints = [
      {
        x: new Date(earliest).toISOString(),
        y: 70,
        group: 1, // horizontal line group
      },
      {
        x: new Date(latest).toISOString(),
        y: 70,
        group: 1,
      },
    ];

    // Combine main dataPoints + horizontal line points
    const allPoints = [...dataPoints, ...linePoints];

    // Create dataset
    const dataset = new vis.DataSet(allPoints);

    // Create the Graph2D
    const graph2d = new vis.Graph2d(
      containerRef.current,
      dataset,
      groups,
      options
    );

    // Cleanup
    return () => graph2d.destroy();
  }, [noteStartTime, noteEndTime, items]);

  return (
    <div>
      <h1 style={{ marginLeft: '366px' }}>Battery Time Series (w/Horizontal Line)</h1>
      <div
        ref={containerRef}
        style={{ height: '300px', width: '78%', marginLeft: '366px' }}
      />
    </div>
  );
};

export default Graph2D;
