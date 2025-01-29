import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

# Configure Gemini API using the API key
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Define the model
model = genai.GenerativeModel("gemini-1.5-flash")

# Define a test prompt
test_prompt = "Explain MQTT and its use cases."

# Send the prompt to Gemini
response = model.generate_content(test_prompt)

# Print the response
print("\n### LLM Test Output ###")
print(response.text)  # Corrected attribute usage
print("########################\n")
