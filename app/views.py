from aiohttp import web
from app.controller import controller_get_logs
import app.db


async def health(request):
    return web.json_response({'status': True})


# async def create_log(request):
#     data = await request.post()
#     return web.json_response({'status': True})
#
#
# async def get_log_by_id(request):
#     log_id = int(request.match_info['log_id'])
#     return web.json_response({'status': True})


async def get_logs_list(request):
    async with request.app['db'].acquire() as conn:
        try:
            logs = await controller_get_logs(conn)
        except app.db.RecordNotFound as e:
            raise web.HTTPNotFound(text=str(e))

        return {
            'logs': logs,
        }

        # return web.json_response({'status': True})
