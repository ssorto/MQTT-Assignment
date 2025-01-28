# Collaborative Team Dashboard with MQTT and LLM-Powered Collaboration Insights

This project demonstrates a real-time collaborative team dashboard using MQTT for task updates and Google Gemini API for motivational and collaboration insights. The **publisher** sends task updates, while the **subscriber** displays the team dashboard and generates actionable suggestions for improving teamwork and motivation.

---

## Setup and Installation Instructions

### Prerequisites
- Python 3.7+ installed
- Required libraries: `paho-mqtt`, `python-dotenv`, `google-generativeai`

### Installation Steps
1. **Clone the Repository**:
   ```bash
   git clone <repository_url>
   cd mqtt_project

# Step 1: Create a virtual environment
python3 -m venv venv

# Step 2: Activate the virtual environment
source venv/bin/activate  # For macOS/Linux
# .\venv\Scripts\activate  # For Windows

# Step 3: Install required libraries
pip install paho-mqtt python-dotenv google-generativeai

# Step 4: Create a .env file to store the Gemini API key
Open a text editor and save the following line as a file named .env in the project directory:
GEMINI_API_KEY=your_gemini_api_key

# Step 5: Verify that the libraries are installed
pip list  # Check if paho-mqtt, python-dotenv, and google-generativeai are listed

# Step 6: Verify functionality by running the scripts
# Start the subscriber script in one terminal
python mqtt_project/sub.py

# In another terminal, activate the virtual environment again
source venv/bin/activate  # For macOS/Linux
# .\venv\Scripts\activate  # For Windows

# Start the publisher script
python mqtt_project/pub.py

---

# Example Usage of MQTT Script and LLM Interaction

# Start the Subscriber Script
# Open a terminal and run:
python mqtt_project/sub.py

# Output (Subscriber):
# Subscriber connects to the broker and listens for messages on the 'teamdashboard' topic.
Successfully connected to broker
Subscribed to topic: teamdashboard

# Start the Publisher Script
# Open another terminal and run:
python mqtt_project/pub.py

# Output (Publisher):
# Publisher sends dynamic updates to the 'teamdashboard' topic.
Published: {"team_member": "Alice", "task": "Prepare slides", "status": "In Progress"}
Published: {"team_member": "Bob", "task": "Submit report", "status": "Not Started"}
Published: {"team_member": "Charlie", "task": "Research data", "status": "Completed"}

# Output (Subscriber):
# Subscriber receives and processes the updates. It displays the Team Dashboard and generates insights using the LLM.
### Team Dashboard ###
Alice: Task - Prepare slides, Status - In Progress
Bob: Task - Submit report, Status - Not Started
Charlie: Task - Research data, Status - Completed

### Gemini Insights ###
Based on the provided updates, here are some suggestions for better collaboration and motivation:

**Collaboration:**
- **Regular Check-ins:** Implement short, regular team meetings (e.g., daily stand-ups) to discuss progress, roadblocks, and dependencies.
- **Clear Communication Channels:** Establish a clear communication channel (e.g., Slack, project management tool).
- **Dependency Management:** Define and discuss task dependencies to avoid delays.
- **Shared Workspace:** Use a shared document to foster transparency and collaboration.

**Motivation:**
- **Acknowledge Completion:** Celebrate Charlie's completed task to boost morale.
- **Address 'Not Started' Tasks:** Reach out to Bob to understand and resolve potential roadblocks.
- **Break Down Large Tasks:** Break down Bob's "Submit report" into smaller subtasks for better progress visibility.
- **Set Clear Expectations:** Ensure all team members understand their roles and deadlines.

# Summary
# The system combines MQTT's real-time communication with Gemini's LLM capabilities
# to enhance team collaboration and motivation effectively.
