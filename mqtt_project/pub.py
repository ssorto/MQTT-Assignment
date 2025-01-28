import paho.mqtt.client as mqtt
import json
import time
import random

# Define the broker and topic
broker = "test.mosquitto.org"
port = 1883
topic = "teamdashboard"

# Create MQTT publisher client
publisher = mqtt.Client()
publisher.connect(broker, port)

# Define initial tasks with dynamic statuses
tasks = [
    {"team_member": "Alice", "task": "Prepare slides", "status": "Not Started"},
    {"team_member": "Bob", "task": "Submit report", "status": "Not Started"},
    {"team_member": "Charlie", "task": "Research data", "status": "Not Started"},
]

# Define possible statuses for tasks
statuses = ["Not Started", "In Progress", "Completed"]

try:
    while True:
        for task in tasks:
            # Randomly update task statuses to simulate real-world progress
            if task["status"] == "Not Started":
                task["status"] = "In Progress"
            elif task["status"] == "In Progress":
                task["status"] = "Completed"

            # Randomize updates to keep it dynamic
            if random.random() < 0.3:  # 30% chance of changing status back
                task["status"] = random.choice(statuses)

            # Publish updated task to MQTT topic
            publisher.publish(topic, json.dumps(task))
            print(f"Published: {json.dumps(task)}")

        # Wait a bit before sending the next set of updates
        time.sleep(5)

except KeyboardInterrupt:
    print("Publisher stopped.")