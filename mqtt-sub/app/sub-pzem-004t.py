import paho.mqtt.client as mqtt
import datetime, time
import random, json

#mqtt settings
broker = '192.168.101.236'
port = 1883

topic = "elec110"
Keep_Alive_Interval = 60
client_id = f'python-mqtt-{random.randint(0, 1000)}'
now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

def on_connect(client, userdata, flags, rc):
  mqttc.subscribe(topic, 0)

def on_subscribe(mosq, obj, mid, granted_qos):
  pass

def on_message(mosq, obj, msg):

    m_decode = str(msg.payload.decode('utf-8', 'ignore'))
    #print("message received",m_decode)
    #print(type(m_decode) )
    m_in=json.loads(m_decode)
    m_in['v']=round(m_in['v'],2)
    m_in['i']=round(m_in['i'],2)
    m_in['active_power'] = round(m_in['active_power'], 2)
    m_in['freq'] = round(m_in['freq'], 2)
    m_in['pf'] = round(m_in['pf'], 2)
    print(m_in)
    #dt_string = datetime.datetime.now()
    #print(dt_string)
    return True

print (client_id)
print ("Hello")
print ('===================')
#MAIN
mqttc = mqtt.Client(client_id=client_id)

# Assign event callbacks
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_subscribe = on_subscribe

# Connect
#mqttc.tls_set(ca_certs="ca.crt", tls_version=ssl.PROTOCOL_TLSv1_2)
mqttc.connect(broker, int(port), int(Keep_Alive_Interval))

# Continue the network loop & close db-connection
mqttc.loop_forever()
connection.close()
