import asyncio
from A_reusable_delay_function import delay

def call_later():
    print("I'm being called in the future!")
async def main():
    loop = asyncio.get_running_loop()
    loop.call_soon(call_later)
    await delay(1)

asyncio.run(main())