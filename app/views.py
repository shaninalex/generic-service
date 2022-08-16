from aiohttp import web


def health(request):
    return web.json_response({'status': True})
