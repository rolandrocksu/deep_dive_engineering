import asyncio


async def main():
    async def f():
        await g_task

    async def g():
        await f_task

    f_task = asyncio.create_task(f())
    g_task = asyncio.create_task(g())
    await f_task


asyncio.run(main())
