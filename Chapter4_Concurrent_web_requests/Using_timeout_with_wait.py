import aiohttp
import asyncio
import logging
from Using_as_completed import fetch_status
from A_decorator_for_timing_coroutine import async_timed


@async_timed()
async def main():
    async with aiohttp.ClientSession() as session:
        url = 'https://example.com'
        fetchers = [asyncio.create_task(fetch_status(session, url)),
                    asyncio.create_task(fetch_status(session, url)),
                    asyncio.create_task(fetch_status(session, url, delay=3))]

        done, pending = await asyncio.wait(fetchers, timeout=1)

        print(f'Done task count:{len(done)}')
        print(f'Pending task count:{len(pending)}')

        for done_task in done:
            result = await done_task
            print(result)

asyncio.run(main())
