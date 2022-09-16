import asyncio
#from unittest import result
from A_reusable_delay_function import delay

async def main():
    task = asyncio.create_task(delay(10))

    try:
        result = await asyncio.wait_for(asyncio.shield(task),5)
        print(result)
    except asyncio.exceptions.TimeoutError:
        print("Task took longer than five seconds,it will finish soon!")
        result = await task 
        print(result)

asyncio.run(main())