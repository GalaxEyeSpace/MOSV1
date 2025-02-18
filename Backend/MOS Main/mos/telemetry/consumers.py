import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from .models import Velocity, Storage, Power, Position  # Ensure these models are imported

class TelemetryConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Accept the WebSocket connection
        await self.accept()
        print("MOS WebSocket Connected!")

    async def disconnect(self, close_code):
        print("WebSocket Disconnected")

    @database_sync_to_async
    def save_velocity(self, timestamp, x, y, z):
        # Save the velocity data to the database in a synchronous manner
        return Velocity.objects.create(
            timestamp=timestamp,
            x=x,
            y=y,
            z=z
        )

    @database_sync_to_async
    def save_storage(self, timestamp, instant_data_gen, instant_data_down, ssd_storage, ssd_capacity):
        # Save the storage data to the database
        return Storage.objects.create(
            timestamp=timestamp,
            instant_data_gen=instant_data_gen,
            instant_data_down=instant_data_down,
            ssd_storage=ssd_storage,
            ssd_capacity=ssd_capacity
        )

    @database_sync_to_async
    def save_power(self, timestamp, net_power, solar, storage):
        # Save the power data to the database
        return Power.objects.create(
            timestamp=timestamp,
            net_power=net_power,
            solar=solar,
            storage=storage
        )

    @database_sync_to_async
    def save_position(self, timestamp, x, y, z):
        # Save the position data to the database
        return Position.objects.create(
            timestamp=timestamp,
            x=x,
            y=y,
            z=z
        )

    async def receive(self, text_data):
        print(f"Received Data from Simulator")

        # Parse the received JSON data
        data = json.loads(text_data)

        # Extract velocity data
        velocity_data = data.get('velocity', {})
        if velocity_data:
            timestamp = velocity_data.get('timestamp')
            x = velocity_data.get('x')
            y = velocity_data.get('y')
            z = velocity_data.get('z')
            # Save velocity data to the database asynchronously
            await self.save_velocity(timestamp, x, y, z)

        # Extract storage data
        storage_data = data.get('storage', {})
        if storage_data:
            timestamp = storage_data.get('timestamp')
            instant_data_gen = storage_data.get('instant_data_gen')
            instant_data_down = storage_data.get('instant_data_down')
            ssd_storage = storage_data.get('ssd_storage')
            ssd_capacity = storage_data.get('ssd_capacity')
            # Save storage data to the database asynchronously
            await self.save_storage(timestamp, instant_data_gen, instant_data_down, ssd_storage, ssd_capacity)

        # Extract power data
        power_data = data.get('power', {})
        if power_data:
            timestamp = power_data.get('timestamp')
            net_power = power_data.get('net_power')
            solar = power_data.get('solar')
            storage = power_data.get('storage')
            # Save power data to the database asynchronously
            await self.save_power(timestamp, net_power, solar, storage)

        # Extract position data
        position_data = data.get('position', {})
        if position_data:
            timestamp = position_data.get('timestamp')
            x = position_data.get('x')
            y = position_data.get('y')
            z = position_data.get('z')
            # Save position data to the database asynchronously
            await self.save_position(timestamp, x, y, z)

        # Optionally, send a message back to the WebSocket client (acknowledging the received data)
        await self.send(text_data=json.dumps({
            'message': 'Data received and saved to database successfully!'
        }))