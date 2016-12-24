#!usr/bin/env python3
#-*- coding:utf-8 -*-

# date: 2016-12-20
# author: WillieFoo
#


import asyncio
import os
import time
import json

import logging
logging.basicConfig(level=logging.INFO)

from datetime import datetime
from aiohttp import web


def index(request):

    # '
    # 在Response函数中添加 content_type='text/html' 的参数设置。
    # 不指定content_type的情况下，默认返回的是 'application/octet-stream'，即“.*”(二进制流，没有扩展名，浏览器无法识别的文件类型)。
    # '
    return web.Response(body=b'<h1>Python3-Webapp</h1>', content_type='text/html', charset='utf-8')

async def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
    srv = await loop.create_server(app.make_handler(), '127.0.0.1', 9000)
    logging.info('Server started at http://127.0.0.1:9000...')
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
