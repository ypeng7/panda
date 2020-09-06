# -*- coding: utf-8 -*-
""".

@file: 4ea7fa6f6a9d422f8c592ec314b4ce90
@guid: bb6244ba662a433abca4e9ab36d9ca09

@author: Yue Peng
@email: yuepaang@gmail.com
@date: 2019-08-07 10:50:12
@modified:

@brief:
"""
__author__ = "Yue Peng"
import os
import random
import time
from functools import wraps

import requests
from requests.exceptions import ConnectionError

HEADERS_FN = os.path.join(os.path.dirname(__file__), "headers.txt")

# 随机头信息
USER_AGENTS = [line.strip() for line in open(HEADERS_FN, "r").readlines()]


# 请求头
BASE_HEADERS = {
    "User-Agent": random.choice(USER_AGENTS),
    "Accept-Encoding": "gzip, deflate, sdch",
    "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
}


def retry(func, max_retry_times=3, wait_time=5):
    @wraps(func)
    def deco(*args, **kwargs):
        for i in range(max_retry_times):
            result = func(*args, **kwargs)
            if result is None:
                print(f"retry {i} time")
                time.sleep(wait_time)
                continue
            else:
                return result

    return deco


@retry
def get_text(url, options={}):
    headers = {**BASE_HEADERS, **options}
    print(f"Fetching {url}...")
    try:
        resp = requests.get(url, headers=headers, timeout=5)
        if resp.status_code == 200:
            return resp
    except ConnectionError:
        return None
