import React, { useEffect, useState } from "react";
import styled from "styled-components";

const AlertBox = styled.div`
  text-align: center;
  font-size: 16px;
  font-weight: bold;
  color: ${(props) => (props.$alert ? "#FF3B30" : "transparent")}; 
  background-color: ${(props) => (props.$alert ? "rgba(64, 141, 80, 0.2)" : "transparent")};
  padding: 8px;
  border-radius: 5px;
  transition: all 0.5s ease-in-out;
`;

const AlertComponent = ({ lastDataTime, dataReceived }) => {
  const [showAlert, setShowAlert] = useState(false);

  useEffect(() => {
    const checkNoData = setInterval(() => {
      if (dataReceived && Date.now() - lastDataTime > 5000) {
        setShowAlert(true); // Show alert only after data has been received at least once
      } else {
        setShowAlert(false);
      }
    }, 1000); // Check every second

    return () => clearInterval(checkNoData);
  }, [lastDataTime, dataReceived]);

  return (
    <AlertBox $alert={showAlert}>
      {showAlert ? "🚀 ALERT:Telemetry Data Received!" : ""}
    </AlertBox>
  );
};

export default AlertComponent;
