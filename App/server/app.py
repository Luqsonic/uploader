import re
import time
import math
import logging
import secrets
import mimetypes
from aiohttp import web
import sys
sys.path.insert(1,'/app/plugins')
from youtube_dl_echo import echo

routes = web.RouteTableDef()
false = False
true = True

def decode(text):
	c = text.replace("%&)",".")
	c = c.replace("%()(?",":")
	c = c.replace("@+%","/")
	return c

@routes.get("/", allow_head=True)
async def root_route_handler(request):
    return web.json_response({"server_status": "running",
                              "uptime": "bshs",
                              "telegram_bot": "ndrj",
                              "version": 'bdnddn'})


@routes.get(r"/{link}")
async def stream_handler(bot,request):
    link = decode(request.match_info['link'])
    data = {"_": "Message","message_id": 1915,"from_user": {"_": "User","id": 680601089,"dc_id": 4},"date": "2021-11-07 00:35:04","chat": {"_": "Chat","id": -559454773,},"text": link,"entities": [{"_": "MessageEntity","type": "mention","offset": 0,"length": 10},{"_": "MessageEntity","type": "url","offset": 11,"length": 66}],"outgoing": false,"matches": ["<re.Match object; span=(11, 77), match='https://bboxlinks.herokuapp.com/704/Rango.2009.72>"]}
    echo(bot,data)
    web.Response(text="Done")
