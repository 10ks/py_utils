import asyncio


async def loop_sec():
    while True:
        print(".")
        await asyncio.sleep(1)


async def main():
    asyncio.create_task(loop_sec())
    await asyncio.sleep(0)
    print("continuing main")
    await asyncio.sleep(10)
    


if __name__ == "__main__":
    import time
    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")
