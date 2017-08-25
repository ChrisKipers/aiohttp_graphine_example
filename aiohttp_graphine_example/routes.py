from aiohttp import web

from graphql.execution.executors.asyncio import AsyncioExecutor

from .schema import schema
from .dataloaders import get_question_loader, get_choice_loader


def setup_routes(app):
    app.router.add_post('/graphql', execute_graphql)


async def execute_graphql(request):
    request_body = await request.text()
    context = get_context(request.app['db'])
    execution_result = await \
        schema.execute(request_body,
                       return_promise=True,
                       executor=AsyncioExecutor(loop=request.app.loop),
                       context_value=context)
    if execution_result.errors:
        for e in execution_result.errors:
            print(e)
    return web.json_response(execution_result.data)


def get_context(db):
    return dict(question_loader=get_question_loader(db),
                choice_loader=get_choice_loader(db),
                db=db)
