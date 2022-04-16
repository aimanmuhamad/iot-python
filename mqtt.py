import random
import time
import paho.mqtt.client

brokerAddress = "brokerAddress"
username = "userName"
password = "password"

topic = "Sensor/Temperature/TMP36"

min = 20
max = 30

def on_connect(client,userdata,msg):
    if rc == 0 :
        print("Connected")
    else:
        print("Connect return result code : "+src(rc))

def on_message(client,userdata,msg):
    print("Received message : "+ msg.topic+" "+msg.payload.decode("utf-8"))


#create client
client=mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.tls_set(tls_version=mqtt.ssl.PROTOCOL_TLS)
client.username_pw_set(userName,password)
client.connect(brokerAddress,8883)

wait = 20
while True :
    data = random.randint(min,max)
    print(data)
    client.publish(topic,data)
    time.sleep(wait)