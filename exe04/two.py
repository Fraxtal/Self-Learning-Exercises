import asyncio

async def onesec():
    await asyncio.sleep(1)
    print("1 second")

async def twosec():
    await asyncio.sleep(2)
    print("2 second")

async def threesec():
    await asyncio.sleep(3)
    print("3 second")

async def allsec():
    await onesec()
    await twosec()
    await threesec()

asyncio.run(allsec())