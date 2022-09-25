import asyncio
from sqlite3 import connect
import asyncpg
from asyncpg.transaction import Transaction


async def main():
    connection = await asyncpg.connect(host='127.0.0.1',
                                       port=5432,
                                       user='postgres',
                                       password='ly0013',
                                       database='products')

    transaction: Transaction = connection.transaction()
    await transaction.start()
    try:
        await connect.execute("INSERT INTO brand "
                              "VALUES(DEFAULT, 'brand_1')")
        await connect.execute("INSERT INTO brand "
                              "VALUES(DEFAULT, 'brand_2')")
    except asyncpg.PostgresError:
        print('Errors,rolling back transaction')
        await transaction.rollback()
    else:
        print('No errors,committing transaction')
        await transaction.commit()

    query = """ SELECT brand_name FROM brand
                WHERE brand_name LIKE 'brand%' """

    brands = await connection.fetch(query)
    print(brands)

    await connection.close()

asyncio.run
