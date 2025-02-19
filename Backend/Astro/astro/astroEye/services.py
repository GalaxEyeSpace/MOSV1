import json
from sgp4.api import Satrec, jday
from datetime import datetime, timedelta

def propagate_orbit(request_body):
    print("Processing request body:", request_body)

    # ✅ Parse JSON correctly
    if isinstance(request_body, str):  
        data = json.loads(request_body)
    else:
        data = request_body

    print("Extracted data:", data)

    # ✅ Extract values using correct keys
    tle_data = data.get("tle", [])  
    target_time_str = data.get("time")  # "2024-02-20T12:00:00Z"
    target_time = datetime.fromisoformat(target_time_str.replace("Z", "")) 

    print("Target Time: ", target_time)

    # ✅ Ensure TLE contains exactly two lines
    if not (isinstance(tle_data, list) and len(tle_data) == 2):
        return {"error": "Invalid TLE format. Expected list with 2 elements."}

    tle_line1, tle_line2 = tle_data  # Unpack list into separate variables

    # ✅ Check required fields
    if not all([tle_line1, tle_line2, target_time]):
        return {"error": "Missing required fields: tle (array of 2 lines), time"}
    
    satellite = Satrec.twoline2rv(tle_line1, tle_line2)
    print("TLE Loaded successfully")

    # Create satellite object from TLE
    satellite = Satrec.twoline2rv(tle_line1, tle_line2)

    jd_epoch, fr_epoch = satellite.jdsatepoch, satellite.jdsatepochF

    jd_target, fr_target = jday(target_time.year, target_time.month, target_time.day,
                                target_time.hour, target_time.minute, target_time.second)
    
    delta_days = (jd_target + fr_target) - (jd_epoch + fr_epoch)

    error_code, position, velocity = satellite.sgp4(jd_epoch, delta_days)

    if error_code == 0:
        return position, velocity
    else:
        raise ValueError(f"SGP4 propagation error: {error_code}")

from datetime import datetime, timedelta
import json
from sgp4.api import Satrec, jday

def multistep_propagation(request_body): 
    print("Processing request body:", request_body)

    # ✅ Parse JSON correctly
    if isinstance(request_body, str):  
        data = json.loads(request_body)
    else:
        data = request_body

    print("Extracted data:", data)

    tle_data = data.get("tle", [])  

    tle_line1, tle_line2 = tle_data

    start_time_str = data.get("start_time")  # "2024-02-20T12:00:00Z"
    start_time = datetime.fromisoformat(start_time_str.replace("Z", "")) 

    end_time_str = data.get("end_time")  # "2024-02-20T12:00:00Z"
    end_time = datetime.fromisoformat(end_time_str.replace("Z", "")) 

    step_size = data.get("step_size")  # Correct the key if needed (it should match the name used in your request)
    
    if not step_size:
        return {"error": "step_size is missing or invalid in the request."}
    
    # Convert step_size to a timedelta object
    time_step = timedelta(seconds=step_size)
    
    current_time = start_time
    results = []

    satellite = Satrec.twoline2rv(tle_line1, tle_line2)

    while current_time <= end_time:
        # Convert current time to Julian date
        jd, fr = jday(current_time.year, current_time.month, current_time.day,
                      current_time.hour, current_time.minute, current_time.second)

        # Propagate orbit
        error_code, position, velocity = satellite.sgp4(jd, fr)

        if error_code == 0:
            results.append({
                "time": current_time.isoformat(),
                "position_km": position,
                "velocity_km_s": velocity
            })
            print(f"Time: {current_time}, Position: {position}, Velocity: {velocity}")
        else:
            print(f"SGP4 Error at {current_time}: {error_code}")
            break

        current_time += time_step  # Increment current_time by the time step

    return results

def resource_estimation(request_body):

    command_lookup = {
    "CMD001": {"power": 50, "storage": 100},  # Command ID CMD001 requires 50W power and 100MB storage
    "CMD002": {"power": 100, "storage": 50},  # Command ID CMD002 requires 100W power and 50MB storage
    "CMD003": {"power": 150, "storage": 0},   # Command ID CMD003 requires 150W power and no storage
    "CMD004": {"power": 70, "storage": 100},  # Command ID CMD004 requires 70W power and 120MB storage
    # Add more command IDs with their respective resource needs here
    }

    print("Processing request body:", request_body)

    # ✅ Parse JSON correctly
    if isinstance(request_body, str):  
        data = json.loads(request_body)
    else:
        data = request_body

    print("Extracted data:", data)

    current_resources = data.get("initial_resources", [])

    command_list = data.get("command_ids", [])

    resources_over_time = [] 

    for command_index, command_id in enumerate(command_list):
        print(f"Processing Command ID {command_id}")
        
        # Fetch the resources for the current command ID from the lookup table
        task_resources = command_lookup.get(command_id)

        if not task_resources:
            print(f"Invalid Command ID: {command_id}. Skipping...")
            continue

        # Extract resource requirements for the current task
        power_required = task_resources.get("power", 0)
        storage_required = task_resources.get("storage", 0)
        
        # Check if the satellite has enough resources to perform the task
        if current_resources["power"] >= power_required and current_resources["storage"] >= storage_required:
            # Update the resources after completing the task
            current_resources["power"] -= power_required
            current_resources["storage"] -= storage_required
            # Track other resources (e.g., fuel, data, etc.) if necessary

            # Log the resources after this task
            resources_over_time.append({
                "command_index": command_index + 1,
                "command_id": command_id,
                "remaining_power": current_resources["power"],
                "remaining_storage": current_resources["storage"],
            })
            # print(f"Command ID {command_id} completed. Remaining Power: {current_resources['power']} W, Storage: {current_resources['storage']} MB")
        else:
            # Identify which resource is insufficient
            if current_resources["power"] < power_required:
                insufficient_resource = "power"
                remaining_resource = current_resources["power"]
            else:
                insufficient_resource = "storage"
                remaining_resource = current_resources["storage"]

            # Return failure message with the insufficient resource details
            return {
                "status": "failure",
                "failed_command": command_id,
                "insufficient_resource": insufficient_resource,
                "required": task_resources[insufficient_resource],
                "remaining": remaining_resource,
                "remaining_resources": current_resources,
                "resources_over_time": resources_over_time
            }

    # If all commands are executed successfully, return the resources utilized
    return {
        "status": "success",
        "resources_over_time": resources_over_time,
        "final_resources": current_resources
    }