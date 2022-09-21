from A_decorator_for_timing_coroutine import async_timed, delay
import asyncio


async def main():
    result = await asyncio.gather(delay(3), delay(5))
    print(result)

asyncio.run(main())
