import asyncio
from asyncio import CancelledError
from A_reusable_delay_function import delay

async def main():
    long_task = asyncio.create_task(delay(10))

    seconds_elapsed = 0

    while not long_task.done():
        print('Task not finish,checked again in a second.')
        await asyncio.sleep(1)
        seconds_elapsed = seconds_elapsed + 1
        if seconds_elapsed == 5:
            long_task.cancel()

    try:
        await long_task

    except CancelledError:
        print('Our task was cancelled')

asyncio.run(main())
