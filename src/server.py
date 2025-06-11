import socket
import time
import json
import random

HOST = 'localhost'
PORT = 9999

COMMON_PORTS = [80, 443, 22, 8080]
SUSPICIOUS_PORTS = [1337, 9999, 6666]
PROTOCOLS = ["TCP", "UDP", "ICMP", "UNKNOWN"]

def generate_normal_data():
    return {
        "src_port": random.choice(COMMON_PORTS),
        "dst_port": random.randint(1024, 65535),
        "packet_size": random.randint(100, 1500),
        "duration_ms": random.randint(50, 500),
        "protocol": random.choice(["TCP", "UDP"])
    }

def generate_anomaly_data():
    anomaly_type = random.choice(["port", "packet", "duration", "protocol"])
    if anomaly_type == "port":
        return {
            "src_port": random.choice(SUSPICIOUS_PORTS),
            "dst_port": random.randint(60000, 65535),
            "packet_size": random.randint(100, 1500),
            "duration_ms": random.randint(50, 500),
            "protocol": "TCP"
        }
    elif anomaly_type == "packet":
        return {
            "src_port": 443,
            "dst_port": random.randint(1024, 65535),
            "packet_size": random.randint(2000, 10000),
            "duration_ms": random.randint(50, 500),
            "protocol": "TCP"
        }
    elif anomaly_type == "duration":
        return {
            "src_port": 80,
            "dst_port": random.randint(1024, 65535),
            "packet_size": random.randint(100, 1500),
            "duration_ms": random.randint(2000, 5000),
            "protocol": "TCP"
        }
    else:  # unknown protocol
        return {
            "src_port": 443,
            "dst_port": random.randint(1024, 65535),
            "packet_size": random.randint(100, 1500),
            "duration_ms": random.randint(50, 500),
            "protocol": "UNKNOWN"
        }

def get_data():
    return generate_anomaly_data() if random.random() < 0.2 else generate_normal_data()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)

print("Server running and waiting for client...")
conn, addr = server.accept()
print(f"Connected by {addr}")

try:
    while True:
        data = get_data()
        conn.sendall((json.dumps(data) + '\n').encode())
        time.sleep(2)
except KeyboardInterrupt:
    print("Server stopped.")
finally:
    conn.close()
    server.close()
