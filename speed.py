import socket
import json
import time

HOST = '127.0.0.1'
PORT = 49674

def send_command(command):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect((HOST, PORT))
            client_socket.sendall(command.encode('utf-8'))
            response = client_socket.recv(1024).decode('utf-8')
            print(f"Response from server: {response}")
    except Exception as e:
        print(f"Error sending command: {e}")

def update_frequency(new_frequency):
    command = json.dumps({"command": "update_frequency", "value": new_frequency})
    send_command(command)

def toggle_motor(state):
    command = json.dumps({"command": "toggle_motor", "state": state})
    send_command(command)

def request_data():
    command = json.dumps({"command": "request_data"})
    send_command(command)

# Example usage
if __name__ == "__main__":
    time.sleep(1)  # Allow some time for the server to start

    print("Updating frequency to 0.05 seconds")
    update_frequency(0.05)  # Set update frequency to 0.05 seconds

    time.sleep(2)
    print("Turning motor off")
    toggle_motor("off")  # Turn off the motor

    time.sleep(2)
    print("Turning motor on")
    toggle_motor("on")  # Turn on the motor

    time.sleep(2)
    print("Requesting data from the server")
    request_data()  # Request position and force data from the server
