import asyncio


async def wait_sec(l):
    print("Before wait")
    await asyncio.sleep(1)
    print("After wait")
    l[0] = False

async def main():
    # await asyncio.gather(wait_sec([True]), wait_sec([True]), wait_sec([True]))

    run = [True]
    asyncio.create_task(wait_sec(run))
    await asyncio.sleep(0)
    print("continuing main")
    while run[0]:
        print(".")
        await asyncio.sleep(0.1)
        

    # for i in range(10):
    #     print(i)
    #     # time.sleep(0.2)
    #     # await asyncio.sleep(0)
    #     await asyncio.sleep(0.2)


if __name__ == "__main__":
    import time
    s = time.perf_counter()
    asyncio.run(main())
    

    # Completing unfinished tasks (throws a warning)
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(main())
    # pending = asyncio.Task.all_tasks()
    # loop.run_until_complete(asyncio.gather(*pending))

    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")
