import asyncio

async def delay(delay_seconds:int) -> int:
    print(f'sleeping for {delay_seconds}second(s)')
    await asyncio.sleep(delay_seconds)
    print(f'finish sleeping for {delay_seconds} second(s)')
    return delay_seconds