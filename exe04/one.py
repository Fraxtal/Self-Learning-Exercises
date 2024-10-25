import asyncio

async def asioprint():
    await asyncio.sleep(2)
    print("Python Exercises!")

asyncio.run(asioprint())