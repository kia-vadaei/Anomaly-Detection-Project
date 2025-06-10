import socket
import json
import pandas as pd
import joblib

HOST = 'localhost'
PORT = 9999

model = joblib.load("anomaly_model.joblib")

def pre_process_data(data):
    # Convert data to DataFrame for model prediction
    df = pd.DataFrame([data])
    #TODO 2: Here you have to add code to pre-process the data as per your model requirements.
    return df

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    buffer = ""
    print("Client connected to server.\n")

    while True:
        chunk = s.recv(1024).decode()
        if not chunk:
            break
        buffer += chunk

        while '\n' in buffer:
            line, buffer = buffer.split('\n', 1)
            try:
                data = json.loads(line)
                print(f'Data Received:\n{data}\n')

                #TODO 3: Here you have to add code to process the received data and detect anomalies using a trained model.

                #TODO 4: Here you have to connect to a LLM using together ai with your api code to caption the alert for data and anomalies detected.

            except json.JSONDecodeError:
                print("Error decoding JSON.")
