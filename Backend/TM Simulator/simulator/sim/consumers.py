# import asyncio
# import json
# from channels.generic.websocket import AsyncWebsocketConsumer
# from asgiref.sync import sync_to_async
# from sim.models import Velocity, Storage, Power, Position

# class TelemetryConsumer(AsyncWebsocketConsumer):
#     async def connect(self):
#         """Handles WebSocket connection and starts sending telemetry data."""
#         await self.accept()  # Accept WebSocket Connection
#         self.is_connected = True  # Flag to control loop

#         while self.is_connected:
#             telemetry_data = await self.get_latest_data()
#             await self.send(json.dumps(telemetry_data))
#             await asyncio.sleep(1)  # Send data every second

#     async def disconnect(self, close_code):
#         """Handles WebSocket disconnection."""
#         self.is_connected = False  # Stop data loop

#     @sync_to_async
#     def get_latest_data(self):
#         """Fetch the latest telemetry data from the database asynchronously."""
#         velocity = Velocity.objects.order_by('-timestep').first()
#         storage = Storage.objects.order_by('-timestep').first()
#         power = Power.objects.order_by('-timestep').first()
#         position = Position.objects.order_by('-timestep').first()

#         return {
#             "velocity": {
#                 "timestep": str(velocity.timestep) if velocity else None,
#                 "x": velocity.x if velocity else None,
#                 "y": velocity.y if velocity else None,
#                 "z": velocity.z if velocity else None,
#             },
#             "storage": {
#                 "timestep": str(storage.timestep) if storage else None,
#                 "instant_data_gen": storage.instant_data_gen if storage else None,
#                 "instant_data_down": storage.instant_data_down if storage else None,
#                 "ssd_storage": storage.ssd_storage if storage else None,
#                 "ssd_capacity": storage.ssd_capacity if storage else None,
#             },
#             "power": {
#                 "timestep": str(power.timestep) if power else None,
#                 "net_power": power.net_power if power else None,
#                 "solar": power.solar if power else None,
#                 "storage": power.storage if power else None,
#                 "threshold": power.threshold if power else None,
#                 "power_consumed": power.power_consumed if power else None,
#             },
#             "position": {
#                 "timestep": str(position.timestep) if position else None,
#                 "x": position.x if position else None,
#                 "y": position.y if position else None,
#                 "z": position.z if position else None,
#             },
#         }

import asyncio
import json
import random
from datetime import datetime
import websockets
from channels.generic.websocket import AsyncWebsocketConsumer

class TelemetryConsumer(AsyncWebsocketConsumer):
    enabled_telemetry = {
        "velocity": True,
        "storage": True,
        "power": True,
        "position": True,
        "omega": True, 
        "attitude": True,
        "attErr": True, 
    }

    async def connect(self):
        await self.accept()
        # We can safely start listening for terminal input in a background task
        asyncio.create_task(self.listen_for_terminal_input())  # Start listening for terminal input
        asyncio.create_task(self.send_to_mos())  # Send data to MOS
        print("Simulator WebSocket Server Started!")

    async def send_to_mos(self):
        """Send telemetry data to MOS WebSocket Server."""
        uri = "ws://localhost:8000/ws/telemetry/"  # Adjust if necessary
        print("Attempting to connect to MOS WebSocket...")
        async with websockets.connect(uri) as websocket:
            print("Connected to MOS WebSocket!")
            while True:
                telemetry_data = self.generate_fake_data()
                print(f"Sending telemetry data", telemetry_data)  # Log the data you're sending
                await websocket.send(json.dumps(telemetry_data))
                await asyncio.sleep(5)
                print("Telemetry Sent")

    async def receive(self, text_data):
        """Handle messages from WebSocket client (if needed)."""
        data = json.loads(text_data)
        if "toggle" in data and data["toggle"] in self.enabled_telemetry:
            key = data["toggle"]
            self.enabled_telemetry[key] = not self.enabled_telemetry[key]
            print(f"Toggled {key}: {'ON' if self.enabled_telemetry[key] else 'OFF'}")

    async def listen_for_terminal_input(self):
        """Listen for user input in the terminal and toggle telemetry accordingly."""
        while True:
            command = await asyncio.to_thread(input, "Enter toggle command (e.g., toggle_velocity): ")
            print(f"Received Command: {command}")  # Add this line to debug
            key = command.replace("toggle_", "").strip()
            if key in self.enabled_telemetry:
                self.enabled_telemetry[key] = not self.enabled_telemetry[key]
                print(f"{key} telemetry is now {'ON' if self.enabled_telemetry[key] else 'OFF'}")

    def generate_fake_data(self):
        """Generate random telemetry data with current timestamp."""
        print("Generating data...")  # Debug statement
        current_time = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]  # Format to match your request
        
        data = {}

        if self.enabled_telemetry["velocity"]:
            data["velocity"] = {
                "timestep": current_time,
                "x": random.uniform(-10, 10),
                "y": random.uniform(-10, 10),
                "z": random.uniform(-10, 10),
            }
        if self.enabled_telemetry["storage"]:
            data["storage"] = {
                "timestep": current_time,
                "instant_data_gen": random.randint(0, 100),
                "instant_data_down": random.randint(0, 100),
                "ssd_storage": random.randint(100, 1000),
                "ssd_capacity": 1024,
            }
        if self.enabled_telemetry["power"]:
            data["power"] = {
                "timestep": current_time,
                "net_power": random.uniform(0, 100),
                "solar": random.uniform(0, 50),
                "storage": random.uniform(0, 50),
            }
        if self.enabled_telemetry["position"]:
            data["position"] = {
                "timestep": current_time,
                "x": random.uniform(-100, 100),
                "y": random.uniform(-100, 100),
                "z": random.uniform(-100, 100),
            }
        if self.enabled_telemetry["attErr"]:
            data["attErr"] = {
                "timestep": current_time,
                "x": random.uniform(-10, 10),
                "y": random.uniform(-10, 10),
                "z": random.uniform(-10, 10),
            }
        if self.enabled_telemetry["omega"]:
            data["omega"] = {
                "timestep": current_time,
                "x": random.uniform(-10, 10),
                "y": random.uniform(-10, 10),
                "z": random.uniform(-10, 10),
            }
        if self.enabled_telemetry["attitude"]:
            data["attitude"] = {
                "timestep": current_time,
                "roll": random.uniform(-10, 10),
                "pitch": random.uniform(-10, 10),
                "yaw": random.uniform(-10, 10),
            }
        # print(f"Generated data: {data}")  # Debug print
        return data
    
# Server
# daphne -b 0.0.0.0 -p 8000 simulator.asgi:application

#  Client
#  const socket = new WebSocket("ws://localhost:8000/ws/telemetry/");
#  socket.onmessage = function(event) {
#    console.log("Telemetry Data Received:", JSON.parse(event.data));
#  };
