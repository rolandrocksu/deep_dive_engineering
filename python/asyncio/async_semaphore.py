import random
import asyncio


async def simple_function(index, sem):
    async with sem:
        print(f"function started {index}")

        await asyncio.sleep(random.randint(1, 5))
        print(f"function finished {index}")
        return index


async def main():
    sem = asyncio.Semaphore(3)

    tasks = [asyncio.create_task(simple_function(indx, sem)) for indx in range(20)]
    results = await asyncio.gather(*tasks)

    print(results)

if __name__ == "__main__":
    asyncio.run(main())