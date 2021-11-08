import re
import time
import math
import logging
import secrets
import mimetypes
import asyncio
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


def main():
	@routes.get(r"/{link}")
	async def stream_handler(request):
	    link = decode(request.match_info['link'])
	    data = {"_": "Message","message_id": 1915,"from_user": {"_": "User","id": 680601089,"dc_id": 4},"date": "2021-11-07 00:35:04","chat": {"_": "Chat","id": -559454773,},"text": link,"entities": [{"_": "MessageEntity","type": "mention","offset": 0,"length": 10},{"_": "MessageEntity","type": "url","offset": 11,"length": 66}],"outgoing": false,"matches": ["<re.Match object; span=(11, 77), match='https://bboxlinks.herokuapp.com/704/Rango.2009.72>"]}
	    await bot.send_message(
	    chat_id=680601089,
	    text="jjsj")

if __name__ == "__main__":
    	#asyncio.run(echo(bot,data))
    	asyncio.run(main())  	
