import React, { useRef } from 'react';
import { Canvas, useFrame, useLoader } from '@react-three/fiber';
import { GLTFLoader } from 'three/examples/jsm/loaders/GLTFLoader';

export default function ThreeDMonitorwall() {
  const modelRef = useRef();
  const satelliteGltf = useLoader(GLTFLoader, '/satellite.gltf'); // Load satellite model

  useFrame((_, delta) => {
    if (modelRef.current) modelRef.current.rotation.y += delta * 0.5; // Rotate model
  });

  return (
    <Canvas style={{ width: '100vw', height: '100vh', background: '#000' }}>
      <ambientLight intensity={0.5} />
      <pointLight position={[10, 10, 10]} intensity={1} />
      <primitive ref={modelRef} object={satelliteGltf.scene} scale={1} />
    </Canvas>
  );
}
