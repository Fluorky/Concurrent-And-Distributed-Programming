import asyncio


async def exec_later(secs, msg):
    print(f'Entering task: {msg}')
    await asyncio.sleep(secs)
    print(f'Leaving task: {msg}')


async def main():
    await exec_later(2, "Hello")
    await exec_later(1, "World")

asyncio.run(main())
