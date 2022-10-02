import asyncpg
from aiohttp import web
from aiohttp.web_app import Application
from aiohttp.web_request import Request
from aiohttp.web_response import Response
from asyncpg import Record
from asyncpg.pool import Pool


routes = web.RouteTableDef()
DB_KEY = 'database'


@routes.get('/products/{id}')
async def get_products(request: Request) -> Response:
    try:
        str_id = request.match_info['id']
        product_id = int(str_id)

        query = \
            """
            SELECT
            product_id
            product_name
            brand_id
            FROM product
            WHERE product_id = $1
            """
        connection: Pool = request.app[DB_KEY]
        result: Record = await connection.fetchrow(query, product_id)

        if result is not None:
            return web.json_response(dict(result))
        else:
            raise web.HTTPNotFound()
    except ValueError:
        raise web.HTTPBadRequest()


async def create_database_pool(app: Application):
    print('Creating database pool.')
    pool: Pool = await asyncpg.create_pool(host='127.0.0.1',
                                           port=5432,
                                           user='postgres',
                                           database='products',
                                           password='ly0013',
                                           # min_size=6,
                                                    # max_size=6
                                           )
    app[DB_KEY] = pool


async def destroy_database_pool(app: Application):
    print('Destroying database Pool')
    pool: Pool = app[DB_KEY]
    await pool.close()

app = web.Application()
app.on_startup.append(create_database_pool)
app.on_cleanup.append(destroy_database_pool)

app.add_routes(routes)
web.run_app(app,
            host='127.0.0.1')
