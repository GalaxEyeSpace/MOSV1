# MOSV1

## Steps to Run TM Simulator 

1. Activate venv in two terminals
2. Navigate to MOS in terminal 1 and run "python manage.py runserver"
3. MOS is now running on terminal 1
4. Navigate to TM Simulator in terminal 2 and run
   ````
   daphne -b 0.0.0.0 -p 9000 simulator.asgi:application"
   ````
5. Navigate to "localhost:9000/" in your browser
6. Open up console on "localhost:9000/" and run the following script to start generating telemetry
   ````
   const socket = new WebSocket("ws://localhost:9000/ws/telemetry/");
   socket.onmessage = function(event) {
   console.log("Telemetry Data Received:", JSON.parse(event.data));
   };
   ````
