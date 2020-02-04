import paho.mqtt.client as mqtt

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    # client.subscribe("AALL")
    # client.subscribe("$SYS/#")
    # client.subscribe("#")  # too much messages

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

print("starting")
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

print("before connect")
client.connect("mqtt.eclipse.org", 1883, 10)
print("after connect")

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
print("before loop")
client.loop_forever()
print("after loop")


# TODO read https://www.hivemq.com/tags/mqtt-essentials/
