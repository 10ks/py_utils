#!/usr/bin/env python

# WS client example

import asyncio
import websockets
import random

async def hello():
    uri = "ws://localhost:8765"

    async with websockets.connect(uri) as websocket:
        # name = ""
        while True:
            # await websocket.send("begin")
            # name = input("What's your name? ")
            # await asyncio.sleep(1)  # give micro time to process sending, otherwise input will block
            name = str(random.randint(1, 100))
            try:
                await websocket.send(name)
                print(f"> {name}")
                await asyncio.sleep(2)
                
                greeting = await websocket.recv()
                print(f"< {greeting}")
                await asyncio.sleep(2)                
            except websockets.exceptions.ConnectionClosed as identifier:
                print("alx: connection closed", identifier)
                break

# exceptions.ConnectionClosed
# websockets.exceptions.ConnectionClosedError: code = 1006 (connection closed abnormally [internal]), no reason
# asyncio.get_event_loop().run_until_complete(hello())
asyncio.run(hello())