# -*- coding: utf-8 -*-
""".

@file: f755487895a14cdeb3f39fbfb3d56be8
@guid: 53a3f873cb4948188f27f136f49e025a

@author: Yue Peng
@email: yuepaang@gmail.com
@date: 2019-07-29 16:17:13
@modified:

@brief:
"""
__author__ = "Yue Peng"

import requests
from lxml import etree

from panda.social_media.base import SocialMedia


class Weibo(SocialMedia):
    WEIBO_URL = "https://s.weibo.com"
    WEIBO_REDIAN = "https://s.weibo.com/top/summary?cate=realtimehot"

    @classmethod
    def parse(cls):
        r = requests.get(cls.WEIBO_REDIAN)
        r.encoding = 'utf-8'
        soup = etree.HTML(r.text)
        for soup_a in soup.xpath("//td[@class='td-02']/a"):
            wb_title = soup_a.text
            wb_url = cls.WEIBO_URL + soup_a.get('href')
            if "javascript:void(0)" in wb_url:
                continue
            print(f"Name: {wb_title}, URL: {wb_url}")
