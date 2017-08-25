from aiomysql.sa import create_engine

async def init_db(app):
    conf = app['config']
    print(conf)
    engine = await create_engine(
        db=conf['database'],
        user=conf['user'],
        password=conf['password'],
        host=conf['host'],
        port=conf['port'],
        loop=app.loop)
    app['db'] = engine


async def close_db(app):
    app['db'].close()
    await app['db'].wait_closed()
