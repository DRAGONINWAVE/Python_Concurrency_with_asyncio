import asyncio
import asyncpg
import logging


async def main():
    connection = await asyncpg.connect(host='127.0.0.1',
                                       port=5432,
                                       user='postgres',
                                       database='products',
                                       password='ly0013')

    async with connection.transaction():
        await connection.execute("INSERT INTO brand VALUES(DEFAULT,'my_new_brand')")

        try:
            async with connection.transaction():
                await connection.execute("INSERT INTO product_color VALUES(4,'black')")

        except Exception as ex:
            logging.warning('Ignoring error inserting product color',
                            exc_info=ex)

    await connection.close()

asyncio.run(main())
