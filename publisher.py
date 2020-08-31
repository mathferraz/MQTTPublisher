import context
import paho.mqtt.client as mqtt
import time

#define broker IP
broker="192.168.0.104"

#define port
port =1883

def on_log(client, userdata, level, buf):
    print(buf)
def on_connect(client, userdata, flags, rc):
    if rc==0:
        client.connected_flag=True #set flag
        print("connected OK")
    else:
        print("Bad connection Returned code=",rc)
        client.loop_stop()
def on_disconnect(client, userdata, mid):
    print("In on_pub callback mid=" ,mid)
def on_publish(client, userdata, mid):
    print("In on_pub callback mid=" ,mid)

# create flag in class
mqtt.Client.connected_flag=False
client = mqtt.Client("P1") # create a new instance
client.on_log=on_log
client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_publish = on_publish
client.username_pw_set(username="rootbroker",password="rootbroker")

# start connection
client.connect(broker,port)
client.loop_start()
while True:
    data = ("Temperatura: 31 graus / Umidade: 21 %")
    print("publishing")
    ret=client.publish("casa/temperatura",data,0) # Publish Data
    print("published return=" ,ret)
    
    #time to reset sensor
    time.sleep(60)
    
# finish connection
client.disconnect()
client.loop_stop()