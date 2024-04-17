import tornado.ioloop
import tornado.web
import tornado.websocket
import json
import datetime
import asyncio

class SimpleWebSocket(tornado.websocket.WebSocketHandler):
    clients = set()

    def open(self):
        SimpleWebSocket.clients.add(self)
        print("Server started and WebSocket opened")

    def on_close(self):
        SimpleWebSocket.clients.remove(self)
        print("WebSocket closed and Server stopped")

    def check_origin(self, origin):
        return True

    @classmethod
    async def send_time_to_all(cls):
        while True:
            now = datetime.datetime.now(datetime.timezone.utc).isoformat() + "Z"
            message = json.dumps({"time": now, "data": "Here is some data"})
            for client in cls.clients:
                client.write_message(message)
            await asyncio.sleep(0)

def make_app():
    return tornado.web.Application([(r"/", SimpleWebSocket),])

if __name__ == "__main__":
    app = make_app()
    app.listen(8765)

    asyncio.ensure_future(SimpleWebSocket.send_time_to_all())
    
    tornado.ioloop.IOLoop.current().start()
