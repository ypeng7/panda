# -*- coding: utf-8 -*-
""".

@file: github.py
@guid: b1b51f54503c4d309bc254b7b0886400

@author: Yue Peng
@email: yuepaang@gmail.com
@date: 2019-08-07 10:46:11
@modified:

@brief:
"""
__author__ = "Yue Peng"

from lxml import etree

from panda.social_media.base import SocialMedia
from panda.social_media.helper import get_text


class GitHub(SocialMedia):
    GITHUB_REDIAN = "https://github.com/trending"
    GITHUB_HEADERS = {
        "Host": "github.com",
        "Referer": "https://github.com/explore"
    }

    @classmethod
    def get_trending(cls):
        r = get_text(cls.GITHUB_REDIAN, options=cls.GITHUB_HEADERS)
        soup = etree.HTML(r.text)
        for soup_a in soup.xpath("//article[@class='Box-row']"):
            gh_title = soup_a.xpath('string(./h1/a)').strip()
            gh_url = "https://github.com/" + soup_a.xpath('./h1/a/@href')[0]
            print(f"Name: {gh_title}, URL: {gh_url}")
