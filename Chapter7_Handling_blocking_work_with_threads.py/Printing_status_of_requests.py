import functools
import requests
import asyncio
from concurrent.futures import ThreadPoolExecutor
from threading import Lock
from A_decorator_for_timing_coroutine import async_timed

counter_lock = Lock()
counter: int = 0


def get_status_code(url: str) -> int:
    global counter
    response = requests.get(url)
    with counter_lock:
        counter += 1
    return response.status_code


async def reporter(request_count: int):
    while counter < request_count:
        print(f'Finished {counter}/{request_count}requests')
        await asyncio.sleep(2)


@async_timed()
async def main():
    loop = asyncio.get_running_loop()
    with ThreadPoolExecutor() as pool:
        request_count = 200
        urls = ['http://www.example.com' for _ in range(request_count)]
        reporter_task = asyncio.create_task(reporter(request_count))
        tasks = [loop.run_in_executor(pool, functools.partial(
            get_status_code, url)) for url in urls]
        result = await asyncio.gather(*tasks)
        await reporter_task
        print(result)

asyncio.run(main())
