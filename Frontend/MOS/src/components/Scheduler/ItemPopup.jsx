// ItemPopup.jsx
import React, { useState, useEffect } from 'react';
import { Button } from '@mui/material';
import { MapContainer, TileLayer, CircleMarker, Polyline } from 'react-leaflet';
import 'leaflet/dist/leaflet.css';
import * as satellite from 'satellite.js';

// TLE data for the ISS (replace with your own TLE if needed)
const TLE_LINE1 =
  "1 25544U 98067A   24028.55694444  .00016717  00000-0  10270-3 0  9992";
const TLE_LINE2 =
  "2 25544  51.6412  84.2526 0005717 152.9171 207.2152 15.50013420321769";

const ItemPopup = ({ open, startTime, onClose }) => {
  // 1) Keep a local "reference time" state.
  const [refTime, setRefTime] = useState(null);
  // 2) States for satellite position and track segments.
  const [satPos, setSatPos] = useState([0, 0]);
  const [pastTrack, setPastTrack] = useState([]);
  const [futureTrack, setFutureTrack] = useState([]);
  // 3) State to toggle map visibility.
  const [showMap, setShowMap] = useState(true);

  // Parse startTime when popup becomes open.
  useEffect(() => {
    if (open && startTime) {
      const parsed = new Date(startTime);
      if (!isNaN(parsed)) {
        setRefTime(parsed);
      }
    }
    if (!open) {
      setRefTime(null);
    }
  }, [open, startTime]);

  // SGP4 setup from TLE.
  const satrec = satellite.twoline2satrec(TLE_LINE1, TLE_LINE2);

  const getPosition = (dateObj) => {
    const posVel = satellite.propagate(satrec, dateObj);
    if (!posVel.position) return null;
    const gmst = satellite.gstime(dateObj);
    const geo = satellite.eciToGeodetic(posVel.position, gmst);
    const lat = satellite.degreesLat(geo.latitude);
    const lng = satellite.degreesLong(geo.longitude);
    return [lat, lng];
  };

  // Helper: split track segments at the International Date Line.
  const splitTrackAtIDL = (track) => {
    const segments = [];
    let currentSegment = [];
    for (let i = 0; i < track.length - 1; i++) {
      currentSegment.push(track[i]);
      const [, lng1] = track[i];
      const [, lng2] = track[i + 1];
      if (Math.abs(lng2 - lng1) > 180) {
        segments.push(currentSegment);
        currentSegment = [];
      }
    }
    currentSegment.push(track[track.length - 1]);
    segments.push(currentSegment);
    return segments;
  };

  // --------------------
  // Force re-calculation of the satellite position and tracks when refTime changes.
  // (Using the same syntax style as your doubleClick / move listeners.)
  // --------------------
  useEffect(() => {
    if (!open) return;
    if (!refTime || isNaN(refTime)) return;

    // 1) Update current position.
    const currentPos = getPosition(refTime);
    if (currentPos) {
      setSatPos(currentPos);
    }

    // 2) Compute past & future track.
    const stepSec = 120; // 2-minute steps.
    const oneHour = 3600;
    const pastPoints = [];
    const futurePoints = [];

    for (let t = -oneHour; t <= oneHour; t += stepSec) {
      const dt = new Date(refTime.getTime() + t * 1000);
      const pos = getPosition(dt);
      if (!pos) continue;
      if (t < 0) {
        pastPoints.push(pos);
      } else if (t > 0) {
        futurePoints.push(pos);
      }
    }
    setPastTrack(splitTrackAtIDL(pastPoints));
    setFutureTrack(splitTrackAtIDL(futurePoints));
  }, [open, refTime]);

  if (!open) return null;

  return (
    <div
      style={{
        marginLeft: '366px',
        width: '78%',
        border: '1px solid #ccc',
        borderRadius: '8px',
        padding: '16px',
        maxWidth: 'lg',
       }}
    >
      <h2>Satellite Ground Track</h2>
      
      {/* Toggle Button for Map Visibility */}
      <div style={{ textAlign: 'right' }}>
        <Button
          onClick={onClose}
          variant="contained"
          color="primary"
          style={{ marginTop: '10px' }}
        >
          Close
        </Button>
      </div>
      
      {/* Map Container with custom CSS styling */}
      {showMap && (
        <div
          className="satellite-map"
          style={{
            width: '100%',
            height: '600px',
            border: '2px solid #1976d2',
            borderRadius: '4px',
          }}
        >
          <MapContainer
            center={satPos}
            zoom={3}
            style={{ width: '100%', height: '100%' }}
          >
            <TileLayer
              url="https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png"
            />

            {pastTrack.map((segment, idx) => (
              <Polyline key={`past-${idx}`} positions={segment} color="blue" weight={2} />
            ))}
            {futureTrack.map((segment, idx) => (
              <Polyline key={`future-${idx}`} positions={segment} color="yellow" weight={2} />
            ))}

            <CircleMarker
              center={satPos}
              radius={5}
              pathOptions={{ color: 'red' }}
            />
          </MapContainer>
        </div>
      )}

      <div style={{ marginTop: '10px' }}>
        <p>
          <strong>Reference Time:</strong> {startTime || 'N/A'}
        </p>
        <p>
          <strong>Satellite Position:</strong>
        </p>
        <p>
          Lat: {satPos[0].toFixed(2)}°, Lng: {satPos[1].toFixed(2)}°
        </p>
      </div>
    </div>
  );
};

export default ItemPopup;
