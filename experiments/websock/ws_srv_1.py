#!/usr/bin/env python

# WS server example

import asyncio
import websockets


async def pinger(websocket):
    while True:
        try:
            await websocket.send("PING !!!")
            print("> PING !!!")
        except websockets.exceptions.ConnectionClosedOK as ex:
            print("alx: connection closed ok", ex)
            break
        await asyncio.sleep(5)
        


async def hello(websocket, path):
    asyncio.create_task(pinger(websocket))
    # message = await websocket.recv()

    async for message in websocket:
        print(f"< {message}")
        greeting = f"Hello {message}!"
        await websocket.send(greeting)
        print(f"> {greeting}")
        await asyncio.sleep(0)
        


print("starting server")
start_server = websockets.serve(hello, "localhost", 8765)
asyncio.get_event_loop().run_until_complete(start_server)
# asyncio.run(start_server)
asyncio.get_event_loop().run_forever()