import asyncio

async def taskLists():
    print("standing in the queue")
    await asyncio.sleep(1)
    print("talked with father")

async def main():
    tl = taskLists()
    task = asyncio.create_task(tl)
    await asyncio.sleep(2)
    print("bought ticket")
    await task

asyncio.run(main())