from aiohttp import web


async def index(request):
    return web.Response(text="Welcome home!")


async def post(request):
    params = await request.post()
    print("#############Params##################")
    print(params)
    return web.json_response(params["challenge"])


doit = web.Application()
doit.router.add_get("/", index)
doit.router.add_post("/slack", post)
