import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from .models import Velocity, Storage, Power, Position, Omega, Attitude, AttErr, Gpstemperaturesensor, Obctemperaturesensor # Ensure these models are imported

class TelemetryConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Accept the WebSocket connection
        await self.accept()
        print("MOS WebSocket Connected!")

    async def disconnect(self, close_code):
        print("WebSocket Disconnected")

    @database_sync_to_async
    def save_velocity(self, timestep, x, y, z):
        # Save the velocity data to the database in a synchronous manner
        return Velocity.objects.create(
            timestep=timestep,
            x=x,
            y=y,
            z=z
        )
    
    @database_sync_to_async
    def save_gps_temp(self, tempsensor, epochtime, timest, synthetictime):
        return Gpstemperaturesensor.objects.create(
            tempsensor=tempsensor,
            epochtime=epochtime,
            timest=timest,
            synthetictime=synthetictime
        )
    
    @database_sync_to_async
    def save_obc_temp(self, tempsensor, epochtime, timest, synthetictime):
        return Obctemperaturesensor.objects.create(
            tempsensor=tempsensor,
            epochtime=epochtime,
            timest=timest,
            synthetictime=synthetictime
        )
    
    @database_sync_to_async
    def save_att_err(self, timestep, x, y, z):
        return AttErr.objects.create(
            timestep=timestep,
            x=x,
            y=y,
            z=z
        )
    
    @database_sync_to_async
    def save_attitude(self, timestep, roll, pitch, yaw):
        return Attitude.objects.create(
            timestep=timestep,
            roll = roll,
            pitch = pitch, 
            yaw = yaw, 
        )

    @database_sync_to_async
    def save_omega(self, timestep, x, y, z):
        return Omega.objects.create(
            timestep=timestep,
            x=x,
            y=y,
            z=z
        )

    @database_sync_to_async
    def save_storage(self, timestep, instant_data_gen, instant_data_down, ssd_storage, ssd_capacity):
        # Save the storage data to the database
        return Storage.objects.create(
            timestep=timestep,
            instant_data_gen=instant_data_gen,
            instant_data_down=instant_data_down,
            ssd_storage=ssd_storage,
            ssd_capacity=ssd_capacity
        )

    @database_sync_to_async
    def save_power(self, timestep, net_power, solar, storage):
        # Save the power data to the database
        return Power.objects.create(
            timestep=timestep,
            net_power=net_power,
            solar=solar,
            storage=storage
        )

    @database_sync_to_async
    def save_position(self, timestep, x, y, z):
        # Save the position data to the database
        return Position.objects.create(
            timestep=timestep,
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
            timestep = velocity_data.get('timestep')
            x = velocity_data.get('x')
            y = velocity_data.get('y')
            z = velocity_data.get('z')
            # Save velocity data to the database asynchronously
            await self.save_velocity(timestep, x, y, z)

        # Extract storage data
        storage_data = data.get('storage', {})
        if storage_data:
            timestep = storage_data.get('timestep')
            instant_data_gen = storage_data.get('instant_data_gen')
            instant_data_down = storage_data.get('instant_data_down')
            ssd_storage = storage_data.get('ssd_storage')
            ssd_capacity = storage_data.get('ssd_capacity')
            # Save storage data to the database asynchronously
            await self.save_storage(timestep, instant_data_gen, instant_data_down, ssd_storage, ssd_capacity)

        # Extract power data
        power_data = data.get('power', {})
        if power_data:
            timestep = power_data.get('timestep')
            net_power = power_data.get('net_power')
            solar = power_data.get('solar')
            storage = power_data.get('storage')
            # Save power data to the database asynchronously
            await self.save_power(timestep, net_power, solar, storage)

        # Extract position data
        position_data = data.get('position', {})
        if position_data:
            timestep = position_data.get('timestep')
            x = position_data.get('x')
            y = position_data.get('y')
            z = position_data.get('z')
            # Save position data to the database asynchronously
            await self.save_position(timestep, x, y, z)

        att_err_data = data.get('attErr', {})
        if att_err_data:
            timestep = att_err_data.get('timestep')
            x = att_err_data.get('x')
            y = att_err_data.get('y')
            z = att_err_data.get('z')
            # Save velocity data to the database asynchronously
            await self.save_att_err(timestep, x, y, z)

        attitude_data = data.get('attitude', {})
        if attitude_data:
            timestep = attitude_data.get('timestep')
            roll = attitude_data.get('roll')
            pitch = attitude_data.get('pitch')
            yaw = attitude_data.get('yaw')
            # Save velocity data to the database asynchronously
            await self.save_velocity(timestep, roll, pitch, yaw)

        omegas_data = data.get('omega', {})
        if omegas_data:
            timestep = omegas_data.get('timestep')
            x = omegas_data.get('x')
            y = omegas_data.get('y')
            z = omegas_data.get('z')
            # Save velocity data to the database asynchronously
            await self.save_omega(timestep, x, y, z)

        gps_temp_data = data.get('gpsTemp', {})
        if gps_temp_data:
            temp = gps_temp_data.get('TempSensor')
            epochtime = gps_temp_data.get('EpochTime')
            timest = gps_temp_data.get('timest')
            synthetictime = gps_temp_data.get('SyntheticTime')
            await self.save_gps_temp(temp, epochtime, timest, synthetictime)

        obc_temp_data = data.get('obcTemp', {})
        if obc_temp_data:
            temp = obc_temp_data.get('TempSensor')
            epochtime = obc_temp_data.get('EpochTime')
            timest = obc_temp_data.get('timest')
            synthetictime = obc_temp_data.get('SyntheticTime')
            await self.save_obc_temp(temp, epochtime, timest, synthetictime)

        # Optionally, send a message back to the WebSocket client (acknowledging the received data)
        await self.send(text_data=json.dumps({
            'message': 'Data received and saved to database successfully!'
        }))