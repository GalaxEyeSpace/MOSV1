import paho.mqtt.client as mqtt
import json
import queue
import time
from django.conf import settings
from .models import UplinkMessage, DownlinkMessage
import threading

# Queue to store responses from the subscription topic
response_queue = queue.Queue()

connect_count = 0  # Track how many times `on_connect` is triggered

def on_connect(client, userdata, flags, rc):
    global connect_count
    connect_count += 1

    if rc == 0:
        print(f"✅ Connected to MQTT Broker! (Connection count: {connect_count})")

        # Ensure we unsubscribe before subscribing to prevent duplicates
        client.unsubscribe(settings.MQTT_BROKER["SUBSCRIBE_TOPIC"])
        client.subscribe(settings.MQTT_BROKER["SUBSCRIBE_TOPIC"], qos=1)

        print(f"📡 Subscribed to {settings.MQTT_BROKER['SUBSCRIBE_TOPIC']} with QoS 1")
    else:
        print(f"❌ Connection failed with error code {rc}")


from datetime import datetime

def on_message(client, userdata, msg):
    decoded_msg = msg.payload.decode()
    print(f"📩 Received Message: {decoded_msg} on topic {msg.topic}")

    try:
        # Parse message into JSON
        message_data = json.loads(decoded_msg)

        # Extract timestamp from the received message
        timestamp = message_data.get("timestamp")

        if not timestamp:
            print("⚠️ Warning: Received message without a timestamp! Inserting anyway.")
        else:
            # Convert timestamp to datetime (optional, for consistency)
            timestamp_dt = datetime.fromisoformat(timestamp)

            # Check if this timestamp already exists in the database
            if DownlinkMessage.objects.filter(payload__contains=timestamp).exists():
                print(f"⚠️ Duplicate message detected with timestamp {timestamp}, ignoring...")
                return  # Ignore duplicate message

        # ✅ Store downlink message if it's unique
        store_downlink_message(decoded_msg)

        # Put the message in the queue (for the function waiting for response)
        response_queue.put(decoded_msg)

    except json.JSONDecodeError:
        print("❌ Error: Received an invalid JSON message, ignoring...")

# Create MQTT Client
client = mqtt.Client(client_id="django_mqtt_client", clean_session=True)

# Set username & password
client.username_pw_set(settings.MQTT_BROKER["USERNAME"], settings.MQTT_BROKER["PASSWORD"])

# Enable SSL/TLS for secure connection
client.tls_set()

# Assign callbacks
client.on_connect = on_connect
client.on_message = on_message

mqtt_started = False

# Connect to the broker
def start_mqtt():
    global mqtt_started
    if mqtt_started:
        print("⚠️ MQTT client already running. Skipping duplicate start.")
        return
    
    mqtt_started = True

    if not client.is_connected():
        print("🚀 Starting MQTT Client...")
        client.connect(settings.MQTT_BROKER["HOST"], settings.MQTT_BROKER["PORT"], keepalive=60)
        client.loop_start()  # Start loop in a separate thread

# Function to publish a message & wait for response
def publish_and_wait_for_response(topic, payload, timeout=5):
    """
    Publishes a message to `topic` and waits for a response from the subscription topic.
    """
    try:
        # Convert payload to JSON
        message = json.dumps(payload)

        # ✅ Store uplink message before publishing
        store_uplink_message(message)

        print(f"📤 Publishing to {topic}: {message}")
        client.publish(topic, message)

        # ✅ Wait for a response from the queue (timeout in seconds)
        try:
            response = response_queue.get(timeout=timeout)
            return response
        except queue.Empty:
            return "No response received"

    except Exception as e:
        return f"Error: {str(e)}"

# Store uplink messages in the DB
def store_uplink_message(payload):
    UplinkMessage.objects.create(payload=payload)

# Store downlink messages in the DB
def store_downlink_message(payload):
    DownlinkMessage.objects.create(payload=payload)




# curl
# curl -X POST http://127.0.0.1:8000/mqtt/publish/ \
#      -H "Content-Type: application/json" \
#      -d '{"message": {"Task1": "Command", "Task2": "Test Command"}}'
