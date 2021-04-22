import paho.mqtt.client as mqtt 
import time
import RPi.GPIO as GPIO
import datetime

GPIO.setmode(GPIO.BCM)
GPIO.setup (20, GPIO.IN)
GPIO.setup (19, GPIO.IN)
GPIO.setup (4, GPIO.OUT)
GPIO.setup (5, GPIO.OUT)
f=open("sensor.txt","w")


def on_message(client, obj, msg):    
	mensaje=(msg.payload.decode("utf-8"))
	print(mensaje)
	ident=(msg.payload.decode("utf-8")).split(" ")[0]
	datos=(msg.payload.decode("utf-8")).split(" ")[1]
	if mensaje=="historial":
		f=open("sensor","r")
		men= f.read()
		mqttc.publish("wlady_hp66@hotmail.com/tema1", men)



mqttc = mqtt.Client() 
mqttc.on_message = on_message 
mqttc.username_pw_set("wlady_hp66@hotmail.com","DiegoWladimir")
mqttc.connect("maqiatto.com", 1883)
mqttc.subscribe("wlady_hp66@hotmail.com/tema2", 0)

rc=0
print("Inicio de conexion")
i = 0
while rc == 0:
	time.sleep(1)
	rc = mqttc.loop()
	Fechahora=datetime.datetime.now().strftime('%d-%m-%Y     %H:%M:%S    ')
	if GPIO.input(20):
		GPIO.output(18, True)
		men=("Sensor1 Activado")
		mqttc.publish("wlady_hp66@hotmail.com/tema2", "S1 activo")
		print(men)
		f=open("sensor.txt","a")
		f.write("H1"+Fechahora  +men +"\n")
		f.close()
	else:
		GPIO.output(18, False)
		mqttc.publish("wlady_hp66@hotmail.com/tema2", "S1 desactivado")

	if GPIO.input(19):
		GPIO.output(17, True)
		men=("Sensor2 Activado")
		mqttc.publish("wlady_hp66@hotmail.com/tema2", "S2 activo")
		print(men)
		f=open("sensor.txt","a")
		f.write("H2"+Fechahora  +men +"\n")
		f.close()
	else:
		GPIO.output(17, False)
		mqttc.publish("wlady_hp66@hotmail.com/tema2", "S2 desactivado")

