import paho.mqtt.client as mqtt
import os
import json
import google.generativeai as genai
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

# Configure Gemini API using the API key
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Define your model
model = genai.GenerativeModel("gemini-1.5-flash")

# Team dashboard dictionary to store task updates
team_dashboard = {}

# Callback for when the client connects to the broker
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Successfully connected to broker")
        client.subscribe("teamdashboard")  # Subscribing to the topic
    else:
        print(f"Connection failed with code {rc}")

# Callback for when a message is received
def on_message(client, userdata, msg):
    # Decode the MQTT message payload
    payload = msg.payload.decode()
    print(f"Received message on topic {msg.topic}: {payload}")

    try:
        # Parse the JSON payload
        data = json.loads(payload)
        team_member = data.get("team_member", "Unknown")
        task = data.get("task", "Unknown Task")
        status = data.get("status", "Unknown Status")

        # Update the team dashboard
        team_dashboard[team_member] = {"task": task, "status": status}

        # Generate a collaborative recommendation or motivational insight
        prompt = f"Based on these updates, suggest ways the team can collaborate better or stay motivated: {team_dashboard}"

        # Send the prompt to Gemini
        response = model.generate_content(prompt)

        # Access the generated text from the response
        gemini_response = response.text  # Corrected attribute usage

        # Print the response
        print(f"\nGemini's suggestion: {gemini_response}")

        # Display the team dashboard and Gemini response
        print("\n### Team Dashboard ###")
        for member, info in team_dashboard.items():
            print(f"{member}: Task - {info['task']}, Status - {info['status']}")
        print("\n### Gemini Insights ###")
        print(gemini_response)
        print("########################\n")

    except Exception as e:
        print("Error processing message:", e)

# Create MQTT subscriber client
subscriber = mqtt.Client()
subscriber.on_connect = on_connect
subscriber.on_message = on_message

# Connect to public broker
print("Connecting to broker...")
subscriber.connect("test.mosquitto.org", 1883, 60)

# Start the subscriber loop
try:
    subscriber.loop_forever()
except KeyboardInterrupt:
    print("Stopping subscriber...")
    subscriber.disconnect()