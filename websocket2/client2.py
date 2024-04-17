from websocket import create_connection
import threading
import json
import time

def on_message(ws):
    start_time = time.time()
    message_count = 0

    while True:
        message = ws.recv()
        message_count += 1
        elapsed_time = time.time() - start_time

        if elapsed_time >= 1.0:
            throughput = message_count / elapsed_time
            message_count = 0
            start_time = time.time()
            print(f"{message}")
            print(f"Throughput: {throughput:.2f} messages/sec")

def run_client():
    ws = create_connection("ws://localhost:8765")
    thread = threading.Thread(target=on_message, args=(ws,))
    thread.start()

if __name__ == "__main__":
    run_client()
