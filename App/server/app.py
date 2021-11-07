import re
import time
import math
import logging
import secrets
import mimetypes
from aiohttp import web

routes = web.RouteTableDef()

@routes.get("/", allow_head=True)
async def root_route_handler(request):
    return web.json_response({"server_status": "running",
                              "uptime": "bshs",
                              "telegram_bot": "ndrj",
                              "version": 'bdnddn'})


@routes.get(r"/{message_id:\S+}")
async def stream_handler(request):
    message_id = request.match_info['message_id']
    message_id = int(re.search(r'(\d+)(?:\/\S+)?', message_id).group(1))
     
