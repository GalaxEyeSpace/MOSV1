# from sgp4.api import Satrec, jday
# from datetime import datetime

# def propagate_orbit(tle_line1, tle_line2, future_time):
#     """
#     Propagates the orbit of a satellite using the SGP4 model.
    
#     :param tle_line1: First line of the TLE
#     :param tle_line2: Second line of the TLE
#     :param future_time: Target datetime object for propagation
#     :return: Position (km) and velocity (km/s) at the target time
#     """

#     # Create satellite object from TLE
#     satellite = Satrec.twoline2rv(tle_line1, tle_line2)

#     # Extract the TLE epoch from the satellite object (in Julian Date format)
#     jd_epoch, fr_epoch = satellite.jdsatepoch, satellite.jdsatepochF

#     # Convert future time to Julian Date
#     jd_target, fr_target = jday(future_time.year, future_time.month, future_time.day,
#                                 future_time.hour, future_time.minute, future_time.second)

#     # Compute the time difference in days
#     delta_days = (jd_target + fr_target) - (jd_epoch + fr_epoch)

#     # Propagate the orbit to the target time
#     error_code, position, velocity = satellite.sgp4(jd_epoch, delta_days)

#     if error_code == 0:
#         return position, velocity
#     else:
#         raise ValueError(f"SGP4 propagation error: {error_code}")

# if __name__ == "__main__":
#     # Example TLE (Replace with actual TLE)
#     tle_line1 = "1 25544U 98067A   24049.26817470  .00004225  00000-0  82442-4 0  9990"
#     tle_line2 = "2 25544  51.6417  18.6951 0001465 306.0283  53.8712 15.40423262451378"

#     # Define future target time for propagation
#     future_time = datetime(2026, 2, 20, 12, 0, 0)  # Example: 20 Feb 2024 at 12:00 UTC

#     # Propagate and print results
#     print("Script is running...")

#     try:
#         position, velocity = propagate_orbit(tle_line1, tle_line2, future_time)
#         print(f"Satellite position at {future_time} (km): {position}")
#         print(f"Satellite velocity at {future_time} (km/s): {velocity}")
#     except ValueError as e:
#         print(e)

# import json
# from sgp4.api import Satrec, jday
# from datetime import datetime, timedelta

# def multistep_propagation(tle, start_time, end_time, step_seconds):
#     """ Propagate the orbit in small steps from start_time to end_time. """
    
#     # Load satellite TLE
#     satellite = Satrec.twoline2rv(tle[0], tle[1])

#     # Convert start and end times to datetime
#     start_time = datetime.fromisoformat(start_time.replace("Z", ""))
#     end_time = datetime.fromisoformat(end_time.replace("Z", ""))

#     # Time step setup
#     time_step = timedelta(seconds=step_seconds)
#     current_time = start_time

#     results = []  # Store results for output

#     while current_time <= end_time:
#         # Convert current time to Julian date
#         jd, fr = jday(current_time.year, current_time.month, current_time.day,
#                       current_time.hour, current_time.minute, current_time.second)

#         # Propagate orbit
#         error_code, position, velocity = satellite.sgp4(jd, fr)

#         if error_code == 0:
#             results.append({
#                 "time": current_time.isoformat(),
#                 "position_km": position,
#                 "velocity_km_s": velocity
#             })
#             print(f"Time: {current_time}, Position: {position}, Velocity: {velocity}")
#         else:
#             print(f"SGP4 Error at {current_time}: {error_code}")
#             break

#         current_time += time_step  # Move to the next step

#     return results

# # ✅ Example Inputs
# tle_example = [
#     "1 25544U 98067A   24049.26817470  .00004225  00000-0  82442-4 0  9990",
#     "2 25544  51.6417  18.6951 0001465 306.0283  53.8712 15.40423262451378"
# ]

# start_time = "2024-02-20T12:00:00Z"  # Start propagation
# end_time = "2024-02-20T12:10:00Z"    # End propagation
# step_size = 30  # Step interval in seconds

# # ✅ Run propagation
# output = multistep_propagation(tle_example, start_time, end_time, step_size)

# # ✅ Print as JSON
# print(json.dumps(output, indent=2))

# from typing import List, Dict, Any

# def resource_estimation(initial_resources: Dict[str, float], 
#                         command_ids: List[str]) -> Dict[str, Any]:

#     # Lookup table for command IDs and associated resources
#     command_lookup = {
#         "CMD001": {"power": 50, "storage": 100},  # Command ID CMD001 requires 50W power and 100MB storage
#         "CMD002": {"power": 100, "storage": 50},  # Command ID CMD002 requires 100W power and 50MB storage
#         "CMD003": {"power": 150, "storage": 0},   # Command ID CMD003 requires 150W power and no storage
#         "CMD004": {"power": 70, "storage": 100},  # Command ID CMD004 requires 70W power and 120MB storage
#         # Add more command IDs with their respective resource needs here
#     }

#     resources_over_time = []  # List to store resource states over time

#     # Initialize the current resources to the provided initial state
#     current_resources = initial_resources.copy()

#     # Process each command ID in the list
#     for command_index, command_id in enumerate(command_ids):
#         print(f"Processing Command ID {command_id}")
        
#         # Fetch the resources for the current command ID from the lookup table
#         task_resources = command_lookup.get(command_id)

#         if not task_resources:
#             print(f"Invalid Command ID: {command_id}. Skipping...")
#             continue

#         # Extract resource requirements for the current task
#         power_required = task_resources.get("power", 0)
#         storage_required = task_resources.get("storage", 0)
        
#         # Check if the satellite has enough resources to perform the task
#         if current_resources["power"] >= power_required and current_resources["storage"] >= storage_required:
#             # Update the resources after completing the task
#             current_resources["power"] -= power_required
#             current_resources["storage"] -= storage_required
#             # Track other resources (e.g., fuel, data, etc.) if necessary

#             # Log the resources after this task
#             resources_over_time.append({
#                 "command_index": command_index + 1,
#                 "command_id": command_id,
#                 "remaining_power": current_resources["power"],
#                 "remaining_storage": current_resources["storage"],
#             })
#             # print(f"Command ID {command_id} completed. Remaining Power: {current_resources['power']} W, Storage: {current_resources['storage']} MB")
#         else:
#             # Identify which resource is insufficient
#             if current_resources["power"] < power_required:
#                 insufficient_resource = "power"
#                 remaining_resource = current_resources["power"]
#             else:
#                 insufficient_resource = "storage"
#                 remaining_resource = current_resources["storage"]

#             # Return failure message with the insufficient resource details
#             return {
#                 "status": "failure",
#                 "failed_command": command_id,
#                 "insufficient_resource": insufficient_resource,
#                 "required": task_resources[insufficient_resource],
#                 "remaining": remaining_resource,
#                 "remaining_resources": current_resources,
#                 "resources_over_time": resources_over_time
#             }

#     # If all commands are executed successfully, return the resources utilized
#     return {
#         "status": "success",
#         "resources_over_time": resources_over_time,
#         "final_resources": current_resources
#     }


# # Example usage:
# initial_resources = {
#     "power": 500,  # Satellite's initial power in watts
#     "storage": 1000,  # Satellite's initial storage in MB
#     # Add other resources like fuel, memory, etc. if necessary
# }

# command_ids = [
#     "CMD001",  # Image Processing
#     "CMD002",  # Data Transmission
#     "CMD003",  # Orbital Maneuvering
#     "CMD004",
#     "CMD004",
#     "CMD001",
# ]

# result = resource_estimation(initial_resources, command_ids)

# # Print the result
# print(result)