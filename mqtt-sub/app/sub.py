import paho.mqtt.client as mqtt
import datetime, time
import random, json

# MQTT settings
broker = '192.168.101.236'
port = 1883

topic = "elec110"
keepalive_interval = 60  # Use lowercase for consistency
client_id = f'python-mqtt-{random.randint(0, 1000)}'
now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

def on_connect(client):  # Removed unused variables
    client.subscribe(topic, 0)  # Properly indented

def on_subscribe(client, userdata, mid, granted_qos):  # Removed unused arguments
    pass  # Placeholder for potential subscription handling

def on_message(client, userdata, msg):  # Removed unused arguments
    try:
        message = msg.payload.decode('utf-8')  # Attempt decoding
        data = json.loads(message)
        data['v'] = round(data['v'], 2)
        data['i'] = round(data['i'], 2)
        data['active_power'] = round(data['active_power'], 2)
        data['freq'] = round(data['freq'], 2)
        data['pf'] = round(data['pf'], 2)
        print(data)
    except UnicodeDecodeError:
        print("Error decoding message payload. Skipping.")

# MAIN
mqttc = mqtt.Client(client_id=client_id)

# Assign event callbacks
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_subscribe = on_subscribe

# Connect to the broker
mqttc.connect(broker, port, keepalive_interval)  # Use correct parameter name

# Run the MQTT loop in a blocking manner
mqttc.loop_forever()
