import paho.mqtt.client as mqtt

def on_message(client, userdata, message):
    print(f"Message received: {message.payload.decode()}")

client = mqtt.Client()
client.on_message = on_message
client.connect("test.mosquitto.org", 1883, 60)
client.subscribe("test/topic")
client.loop_start()

# Publisher
def publish_message(message):
    client.publish("test/topic", message)

# Example usage
publish_message("Hello Subscribers!")
