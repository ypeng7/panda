# -*- coding: utf-8 -*-
""".

@file: v2ex.py
@guid: 6d039d0154c54976af321cf4d1b3cf0b

@author: Yue Peng
@email: yuepaang@gmail.com
@date: 2019-07-29 23:07:37
@modified:

@brief:
"""
__author__ = "Yue Peng"
import requests
from lxml import etree

from panda.quick_media.base import SocialMedia


class V2EX(SocialMedia):
    V2EX_URL = "https://www.v2ex.com"
    V2EX_REDIAN = "https://www.v2ex.com/?tab=hot"

    @classmethod
    def parse(cls):
        r = requests.get(cls.V2EX_REDIAN)
        soup = etree.HTML(r.text)
        for soup_a in soup.xpath("//span[@class='item_title']/a"):
            vsite_name = soup_a.text
            vsite_url = cls.V2EX_URL + soup_a.get('href')
            print(f"Name: {vsite_name}, URL: {vsite_url}")
