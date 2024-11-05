ODrive Motor Control System with Real-Time Data Visualization

Overview
This project aims to develop a cost-effective and eco friendly training device using the ODrive motor control system, Python, and DearPyGui for real-time data visualization. The system is designed to provide adjustable resistance and real-time feedback for users, making it suitable for students and people who have low income. By using a client-server architecture, this project enables remote control of the motor and data logging through two Python scripts: forceposition.py (server) and speed.py (client).

Features
- Real-time Control: The user adjusts resistance of the motor by giving the parameters.
- Data Visualization: Displays position, speed, and force in real-time using DearPyGui.
- Data Logging: Records time-stamped data for position, force, and speed.
- code communication: Enables communication between forceposition.py and speed.py.

Project Structure
forceposition.py: Acts as the server. Manages motor control using the ODrive library and visualizes real-time data using DearPyGui. Receives commands from `Johannes.py` and sends data back.
- speed.py: Acts as the client. Sends commands to adjust motor parameters, such as changing the frequency or toggling the motor state. It also requests data from `forceposition.py` for analysis.

Problem Statement
Existing motor control systems like Motion 1080 are effective but expensive and complex, making them inaccessible for many users such as students, researchers, and hobbyists. This project addresses this by creating a more affordable, user-friendly solution that offers adjustable resistance and data feedback in real-time.

Technical Approach
- Programming Language: Python
- Motor Control: ODrive motor controller for precise motor adjustments.
- Data Visualization: DearPyGui is used to create a graphical interface that displays position, force, and speed.
- Data Logging: Logs data including position, applied force, and speed for further analysis.

   Setup
   - Connect the ODrive motor to your PC via USB.
   - Clone this repository and navigate to the project directory.

User Interaction
- Adjusting Parameters: Users can adjust resistance, view real-time data, and start/stop logging using the GUI.
- Code: speed.py allows users to adjust motor parameters such as changing the update frequency or turning the motor on/off.
- Data Feedback: Position, speed, and applied force are displayed in real-time, providing immediate feedback to the user.

 Results
- Successful communication between `forceposition.py` and `Johannes.py`.
- Real-time data visualization with DearPyGui.
- Strong teamwork and effective debugging of communication errors.
- The project successfully implements real-time motor control with a user-friendly graphical interface.
- Data visualization allows users to monitor their training progress instantly.
- The client-server architecture enables flexible control over the motor and provides an effective way to log and analyze data.

Project Methodology
The project followed an iterative approach, focusing on:
- Initial research and hardware setup.
- Developing a stable client-server communication model.
- Implementing real-time data logging and visualization using DearPyGui.
- Testing the system with different motor parameters and refining the user interface.
  
Future
- Battery Integration: Adding a battery power source for portable use.
-App control: To develop app which can guide the user.
