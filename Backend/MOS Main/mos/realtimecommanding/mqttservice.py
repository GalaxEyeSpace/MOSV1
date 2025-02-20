import paho.mqtt.client as mqtt
import json
import queue
import threading
import time
from django.conf import settings

# Global variables
client = None  
mqtt_connected = False  
response_queue = queue.Queue()  

def on_connect(client, userdata, flags, rc):
    """Handles MQTT connection and subscribes to topics."""
    global mqtt_connected
    if rc == 0:
        # print("✅ Connected to MQTT Broker!")
        mqtt_connected = True
        subscribe_topics(client)
    else:
        print(f"❌ Connection failed with error code {rc}")

def subscribe_topics(client):
    """Subscribes to the required topics."""
    sub_topic = settings.MQTT_BROKER["SUBSCRIBE_TOPIC"]
    pub_topic = settings.MQTT_BROKER["PUBLISH_TOPIC"]
    # print(f"📡 Subscribing to: {sub_topic} and {pub_topic}...")
    client.subscribe(sub_topic, qos=1)
    client.subscribe(pub_topic, qos=1)
    # print("✅ Subscribed successfully!")

def on_message(client, userdata, msg):
    """Handles incoming messages and places them in the response queue."""
    decoded_msg = msg.payload.decode()
    print(f"📩 Received Message: {decoded_msg} on topic {msg.topic}")
    response_queue.put(decoded_msg)

def start_mqtt():
    """Ensures MQTT client is connected before publishing."""
    global client, mqtt_connected

    if client is None:
        client = mqtt.Client(client_id="django_mqtt_client", clean_session=True)
        client.username_pw_set(settings.MQTT_BROKER["USERNAME"], settings.MQTT_BROKER["PASSWORD"])
        client.tls_set()
        client.on_connect = on_connect
        client.on_message = on_message

        try:
            client.connect(settings.MQTT_BROKER["HOST"], settings.MQTT_BROKER["PORT"], keepalive=60)
            client.loop_start()  # Start MQTT loop in background thread
        except Exception as e:
            print(f"❌ MQTT Connection Error: {e}")
            return

    # 🔹 **NEW: Wait for MQTT connection before continuing**
    max_wait_time = 5  # Max 5 seconds
    start_time = time.time()

    while not mqtt_connected:
        if time.time() - start_time > max_wait_time:
            print("⛔ MQTT Connection Timeout!")
            return
        print("⏳ Waiting for MQTT connection...")
        time.sleep(0.5)  # Wait for connection

def publish_and_wait_for_response(topic, payload, timeout=10):
    """Publishes a message and waits for a response from the downlink."""
    start_mqtt()  # Ensure MQTT is running

    if not mqtt_connected:
        return {"error": "MQTT is not connected"}

    try:
        message = json.dumps(payload)
        print(f"📤 Publishing to {topic}: {message}")
        result = client.publish(topic, message, qos=1)

        if result.rc != mqtt.MQTT_ERR_SUCCESS:
            print(f"❌ Failed to publish message with error code {result.rc}")
            return {"error": "Failed to publish message"}

        print("⏳ Waiting for response from loopback...")
        try:
            response = response_queue.get(timeout=timeout)
            print(f"✅ Received response: {response}")
            return json.loads(response)  # Convert response to JSON
        except queue.Empty:
            return {"error": "No response received within timeout"}

    except Exception as e:
        return {"error": str(e)}