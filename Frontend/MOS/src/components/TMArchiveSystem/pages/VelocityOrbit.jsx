import React, { useEffect, useState, useRef } from "react";

const SatelliteOrbit = () => {
  const centerX = 400;  // Center of the canvas (X axis)
  const centerY = 300;  // Center of the canvas (Y axis)
  const radius = 150;   // Radius of the orbit

  const [velocity, setVelocity] = useState({ velocity_x: 0, velocity_y: 0, velocity_z: 0 }); // Velocity data for the satellite
  
  const satelliteRef = useRef(null);
  const angleRef = useRef(0);  // Use ref to store the angle value
  const lastTimeRef = useRef(0);  // Use ref to store the last time for time-based animation

  const orbitSpeed = 0.001; // Adjust this value to control the orbit speed

  // Fetch velocity data from the API
  useEffect(() => {
    fetch("http://localhost:8000/telemetry/get-data/?table=velocity")
      .then((response) => response.json())
      .then((data) => {
        if (Array.isArray(data)) {
          setVelocity({
            velocity_x: parseFloat(data[0].velocity_x),
            velocity_y: parseFloat(data[0].velocity_y),
            velocity_z: parseFloat(data[0].velocity_z), // Include z component
          });
        }
      })
      .catch((error) => console.error("Error fetching velocity data:", error));
  }, []);

  // Animation loop for the satellite movement
  useEffect(() => {
    const animateSatellite = (currentTime) => {
      const deltaTime = currentTime - lastTimeRef.current; // Time difference between frames
      lastTimeRef.current = currentTime; // Update the last time

      // Increment the angle based on the time delta and orbit speed
      angleRef.current += orbitSpeed * deltaTime; // Slower or faster based on orbitSpeed

      // Loop the angle value between 0 and 360
      if (angleRef.current > 360) angleRef.current -= 360;

      // Calculate the new position of the satellite
      const x = centerX + radius * Math.cos((angleRef.current * Math.PI) / 180); // Calculate x based on angle
      const y = centerY + radius * Math.sin((angleRef.current * Math.PI) / 180); // Calculate y based on angle

      // Calculate the satellite's velocity magnitude
      const velocityMagnitude = Math.sqrt(
        (velocity.velocity_x || 0) ** 2 +
        (velocity.velocity_y || 0) ** 2 +
        (velocity.velocity_z || 0) ** 2
      );

      // Ensure the size is a valid number and set it (fallback to 10 if NaN)
      const size = isNaN(velocityMagnitude) || velocityMagnitude < 0 ? 10 : 10 + velocityMagnitude / 10; // Size formula

      // Update the satellite's position and size based on velocity magnitude
      if (satelliteRef.current) {
        satelliteRef.current.setAttribute("cx", x);
        satelliteRef.current.setAttribute("cy", y);
        satelliteRef.current.setAttribute("r", size); // Set the radius dynamically
      }

      // Request the next frame to continue the animation
      requestAnimationFrame(animateSatellite);
    };

    // Start the animation loop
    requestAnimationFrame(animateSatellite);

    // Cleanup on component unmount
    return () => {
      cancelAnimationFrame(animateSatellite);
    };
  }, [velocity]);  // Dependency array is only velocity, as angle is handled with ref

  return (
    <svg width="800" height="600" >
      {/* Orbit path */}
      <circle 
        cx={centerX} 
        cy={centerY} 
        r={radius} 
        stroke="blue" 
        strokeWidth="2" 
        fill="none" 
      />
      {/* Center of the orbit */}
      <circle 
        cx={centerX} 
        cy={centerY} 
        r="5" 
        fill="red" 
      />
      {/* Satellite */}
      <circle 
        ref={satelliteRef} 
        cx={centerX + radius} 
        cy={centerY} 
        r="10" 
        fill="green" 
      />
    </svg>
  );
};

export default SatelliteOrbit;

