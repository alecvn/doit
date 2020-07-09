from aiohttp import web


async def index(request):
    return web.Response(text="Welcome home!")


async def post(request):
    return web.Response(text="You called?!")


doit = web.Application()
doit.router.add_get("/", index)
doit.router.add_post("/slack", post)
