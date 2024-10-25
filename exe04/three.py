import asyncio

async def main():
    for i in range(1, 8):
        print (i)
        await asyncio.sleep(1)

loop = asyncio.get_event_loop()

loop.run_until_complete(main())