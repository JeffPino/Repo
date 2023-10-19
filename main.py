<<<<<<< HEAD
import paho.mqtt.client as mqtt 
import time
def on_message(client, obj, msg):    
	print(msg.topic + " " + str(msg.qos) + " " + msg.payload)
mqttc = mqtt.Client() 
mqttc.on_message = on_message 
mqttc.username_pw_set("jeffersson.pino@gmail.com/test","Pepino123") 
mqttc.connect("maqiatto.com", 1883) 
mqttc.subscribe("jeffersson.pino@gmail.com/test", 0)
rc=0
print("Inicio...")
while rc == 0:
      time.sleep(2)
      rc = mqttc.loop()
=======
import paho.mqtt.client as mqtt 
import time
def on_message(client, obj, msg):    
	print(msg.topic + " " + str(msg.qos) + " " + msg.payload)
mqttc = mqtt.Client() 
mqttc.on_message = on_message 
mqttc.username_pw_set("jeffersson.pino@gmail.com/test","Pepino123") 
mqttc.connect("maqiatto.com", 1883) 
mqttc.subscribe("jeffersson.pino@gmail.com/test", 0)
rc=0
print("Inicio...")
while rc == 0:
      time.sleep(2)
      rc = mqttc.loop()
>>>>>>> e9991f0ab4d9aaf256110801f30cd2c1198c030f
	  