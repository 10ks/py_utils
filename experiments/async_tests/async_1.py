import asyncio

async def count():
    print("One")
    await asyncio.sleep(1)
    print("Two")

def count_sync():
    print("One")
    time.sleep(1)
    print("Two")

async def main():
    # await asyncio.gather(count(), count(), count())
    # for _ in range(3):
    #     count_sync()
    await count()
    await count()

if __name__ == "__main__":
    import time
    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")