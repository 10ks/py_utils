import paho.mqtt.client as mqtt
import time

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("AALL")
    # client.subscribe("$SYS/#")
    # client.subscribe("#")  # too much messages

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    time.sleep(5)
    # exit()
    print("after waiting in message callback")

print("starting")
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

print("before connect")
# TODO use connect_async?
client.connect("mqtt.eclipse.org", 1883, 60)
print("after connect")

client.publish("AALL", "hardcoded_value")

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
print("before loop")
# client.loop_forever()
client.loop_start()
print("after loop")

for i in range(100):
    print(i)
    time.sleep(1)



# TODO read https://www.hivemq.com/tags/mqtt-essentials/
# http://www.steves-internet-guide.com/understanding-mqtt-topics/