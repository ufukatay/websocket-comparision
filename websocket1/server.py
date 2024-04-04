# server.py
import asyncio
import websockets
import json
import datetime

async def time(websocket):
    while True:
        now = datetime.datetime.now(datetime.timezone.utc).isoformat() + "Z"
        message = json.dumps({"time": now, "data": "Here is some data"})
        await websocket.send(message)

start_server = websockets.serve(time, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
