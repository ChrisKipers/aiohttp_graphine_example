import yaml
from aiohttp import web

from .routes import setup_routes
from .db_hooks import init_db, close_db


def load_config():
    filepath = "/Users/ckipers/Documents/graphine-test/config/app_cfg.yaml"
    with open(filepath) as f:
        return yaml.load(f)


if __name__ == "__main__":
    app = web.Application()

    app['config'] = load_config()

    setup_routes(app)
    app.on_startup.append(init_db)
    app.on_cleanup.append(close_db)

    web.run_app(app, host='127.0.0.1', port=8080)
