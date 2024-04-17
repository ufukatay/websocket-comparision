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


'''
async def main():
    async with websockets.serve(time, "localhost", 8765):
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())
'''