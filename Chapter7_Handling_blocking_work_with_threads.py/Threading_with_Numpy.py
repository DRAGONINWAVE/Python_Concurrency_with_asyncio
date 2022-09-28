import functools
from concurrent.futures import ThreadPoolExecutor
import numpy as np
import asyncio
from A_decorator_for_timing_coroutine import async_timed


def mean_for_row(arr, row):
    return np.mean(arr[row])


data_points = 400000000
rows = 50
columns = int(data_points/rows)

matrix = np.arange(data_points).reshape(rows, columns)


@async_timed()
async def main():
    loop = asyncio.get_running_loop()
    with ThreadPoolExecutor() as pool:
        tasks = []
        for i in range(rows):
            mean = functools.partial(mean_for_row, matrix, i)
            tasks.append(loop.run_in_executor(pool, mean))

        results = asyncio.gather(*tasks)

asyncio.run(main())
