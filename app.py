import os
from aiohttp import web

app = web.Application()


async def hello_post(request):
    return web.Response(text='POST request')


async def hello_get(request):
    return web.Response(text='GET request')


app.router.add_post('/payment/bib/check/', hello_post)
app.router.add_get('/payment/bib/check/', hello_get)

port = int(os.environ.get('PORT', 5030))
web.run_app(app, port=port)
