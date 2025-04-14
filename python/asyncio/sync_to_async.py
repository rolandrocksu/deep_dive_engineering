import time
import asyncio

def sync_function():
    print("Function started")
    time.sleep(3)
    print("Function finished")
    return "sync function result"


async def sync_to_async_executor():
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(None, sync_function)


async def main():
    results = await asyncio.gather(sync_to_async_executor(), sync_to_async_executor(), sync_to_async_executor())
    print(results)


if __name__ == "__main__":
    asyncio.run(main())