import time
import secrets
from aiohttp import web
from datetime import datetime
from pymongo import MongoClient
from bson import json_util
import json
import base64
mongo = MongoClient(port=27017)
fakeweb_db = mongo.logs

web_page = open("/var/www/html/index.nginx-debian.html","r").read()


async def handler_get(request):
    
    global fakeweb_db

    content = await request.content.read(-1)
    content = base64.b64decode(content)
    url = request.raw_path
    http =  request.scheme + " " + "".join([str(s) for s in request.version])

    result = {
        "http":http,
        "request": f"{request.method} {url}",
        "ip": request.headers.get('X-Real-IP'),
        "headers": request.headers,
        "content": content,
    }
    if url.strip() != '/' or content:
        fakeweb_db.requests.insert_one(result)

    return web.Response(status=200, body=web_page, content_type='text/html')


def init():
    app = web.Application()
    app.router.add_route("GET", "/{tail:.*}", handler_get)
    app.router.add_route("POST", "/{tail:.*}", handler_get)
    return app


web.run_app(init(), host="127.0.0.1", port=7000)
