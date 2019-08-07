# -*- coding: utf-8 -*-
""".

@file: baidu.py
@guid: 47a4d75e776949d5a2bf96e85f3f3b49

@author: Yue Peng
@email: yuepaang@gmail.com
@date: 2019-07-29 22:46:40
@modified:

@brief:
"""
__author__ = "Yue Peng"
from lxml import etree

from panda.social_media.base import SocialMedia
from panda.social_media.helper import get_text


class Baidu(SocialMedia):
    BAIDU_REDIAN = "http://top.baidu.com/buzz?b=1"

    @classmethod
    def get_trending(cls):
        r = get_text(cls.BAIDU_REDIAN)
        r.encoding = 'gb2312'
        soup = etree.HTML(r.text)
        for soup_a in soup.xpath("//a[@class='list-title']"):
            bd_title = soup_a.text
            bd_url = soup_a.get('href')
            print(f"Name: {bd_title}, URL: {bd_url}")
