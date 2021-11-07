import re
import time
import math
import logging
import secrets
import mimetypes
from aiohttp import web
import sys
from pyrogram import Client
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

bot = Client(
    session_name= 'Web Streamer',
    api_id=7392881,
    api_hash="8c6390da22f0b6a34ee95ab5bf4ddd9f",
    bot_token="1412992512:AAHb8GUexB17g_v9O990SLRWM4OPf64QhnU",
    sleep_threshold="60",
    workers=3
)

@routes.get("/", allow_head=True)
async def root_route_handler(request):
    return web.json_response({"server_status": "running",
                              "uptime": "bshs",
                              "telegram_bot": "ndrj",
                              "version": 'bdnddn'})


 
