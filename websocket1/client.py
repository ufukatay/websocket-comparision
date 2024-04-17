import asyncio
import websockets
import json
from datetime import datetime, timezone
import time

async def listen():
    uri = "ws://localhost:8765"
    message_count = 0
    start_time = time.time()
    async with websockets.connect(uri) as websocket:
        try:
            while True:
                message = await websocket.recv()
                message_count += 1
                if time.time() - start_time >= 1:
                    print(message)
                    print(f"Throughput: {message_count} messages/sec")
                    message_count = 0
                    start_time = time.time()
        except websockets.ConnectionClosed:
            print("Connection closed by the server")

asyncio.run(listen())
