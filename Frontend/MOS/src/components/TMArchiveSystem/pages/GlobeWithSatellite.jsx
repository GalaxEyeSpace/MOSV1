// GlobeWithSatellite.js
import React, { useEffect, useRef, useState } from "react";
import { Canvas } from "@react-three/fiber";
import * as THREE from "three";

const GlobeWithSatellite = ({ positionData, velocityData }) => {
  const [satellitePosition, setSatellitePosition] = useState(null);
  
  const satelliteRef = useRef();
  
  useEffect(() => {
    if (positionData && positionData.length > 0) {
      const lastPosition = positionData[positionData.length - 1]; // Take latest position
      setSatellitePosition(lastPosition); // Set satellite position (latitude, longitude, altitude)
    }
  }, [positionData]);

  const createGlobe = () => {
    const geometry = new THREE.SphereGeometry(5, 32, 32);  // Create a sphere (globe)
    const material = new THREE.MeshBasicMaterial({
      color: 0xeeeeee,
      wireframe: true,
    });
    return new THREE.Mesh(geometry, material);
  };

  const createSatellite = () => {
    const geometry = new THREE.SphereGeometry(0.2, 8, 8); // Satellite shape
    const material = new THREE.MeshBasicMaterial({ color: 0xff0000 }); // Satellite color
    const satellite = new THREE.Mesh(geometry, material);
    satellite.position.set(satellitePosition?.x, satellitePosition?.y, satellitePosition?.z);
    return satellite;
  };

  return (
    <Canvas camera={{ position: [0, 0, 20], fov: 75 }}>
      {/* Create the globe */}
      <mesh>
        {createGlobe()}
      </mesh>

      {/* Create the satellite */}
      <mesh ref={satelliteRef}>
        {satellitePosition && createSatellite()}
      </mesh>
      
      {/* Orbit Controls for interactivity */}
      <orbitControls />
    </Canvas>
  );
};

export default GlobeWithSatellite;
