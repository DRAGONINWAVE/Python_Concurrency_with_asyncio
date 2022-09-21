import asyncio
import aiohttp
from aiohttp import ClientSession
from A_decorator_for_timing_coroutine import async_timed
from Making_an_atihttp_web_request import fetch_status


@async_timed()
async def main():
    async with aiohttp.ClientSession() as session:
        urls = ['https://example.com' for _ in range(10000)]
        requests = [fetch_status(session, url) for url in urls]
        status_code = await asyncio.gather(*requests)
        print(status_code)

asyncio.run(main())
