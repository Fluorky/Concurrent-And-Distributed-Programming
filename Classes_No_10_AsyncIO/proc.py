import asyncio


async def call_ls():
    await asyncio.gather(asyncio.create_subprocess_exec('/bin/ls','-l'), asyncio.create_subprocess_exec('/bin/ps', 'aux'))
    print('Ls-ed')

asyncio.run(call_ls())
