# -*- coding: utf-8 -*-
""".

@file: with_pairs_distance.py
@guid: 11141ac0825a4b9e8c5085ddff02aabe

@author: Yue Peng
@email: yuepaang@gmail.com
@date: 2019-07-26 17:54:23
"""
__author__ = "Yue Peng"
import sys
import time

import asyncio
import aiohttp
from concurrent.futures import ProcessPoolExecutor


async def fetch_json(params, session):
    async with session.get(url, params=params[2], timeout=60*60) as response:
        response_json = response.json()
        return params[0], params[1], await response_json


def process_response(response_json):
    dist = str(response_json["result"]["dist"])
    return dist


async def process(params, session, pool):
    start, end, response_json = await fetch_json(params, session)
    return start, end, await asyncio.wrap_future(
        pool.submit(process_response, response_json))


async def dispatch(params_list):
    pool = ProcessPoolExecutor()
    async with aiohttp.ClientSession() as session:
        distances = (process(params, session, pool) for params in params_list)
        return await asyncio.gather(*distances)


start = time.time()
#  result = asyncio.get_event_loop().run_until_complete(dispatch(params_list))
result = asyncio.run(dispatch(params_list))

print("Duration: {}s".format(time.time()-start))
