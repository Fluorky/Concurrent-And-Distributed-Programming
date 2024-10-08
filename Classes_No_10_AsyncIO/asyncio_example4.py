import asyncio
import time


async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)


async def main():
    task1 = asyncio.create_task(
        say_after(4, 'hello'))

    task2 = asyncio.create_task(
        say_after(6, 'world'))

    print(f"started at {time.strftime('%X')}")

    # Wait until both tasks are completed (should take
    # around 2 seconds.)
    time.sleep(5)
    await task1
    print(f"between at {time.strftime('%X')}")
    await task2

    print(f"finished at {time.strftime('%X')}")

asyncio.run(main())