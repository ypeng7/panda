# -*- coding: utf-8 -*-
""".

@file: hupu.py
@guid: a80ffd5f5930459d8af8fe5c83fcf456

@author: Yue Peng
@email: yuepaang@gmail.com
@date: 2019-07-29 16:14:39
@modified:

@brief:
"""
__author__ = "Yue Peng"

from urllib import request
from bs4 import BeautifulSoup

from panda.social_media.base import SocialMedia


class Hupu(SocialMedia):

    @classmethod
    def get_trending(cls, keyword):
        for page in range(3):
            news_list = cls.get_new_list(page)
            news_urls = cls.get_news_urls(news_list)
            for url in news_urls:
                title, content = cls.news_content(url)
                if keyword in title:
                    print(content)

    @staticmethod
    def get_html(url):
        rs = request.urlopen(url)
        return rs.read()

    @classmethod
    def get_new_list(cls, page):
        html = cls.get_html("https://voice.hupu.com/nba/"+str(page))
        soup = BeautifulSoup(html, "html.parser")
        news_list = soup.select(".list-hd")
        return news_list

    @staticmethod
    def get_news_title(news_list):
        return [news.h4.a.text for news in news_list]

    @staticmethod
    def get_news_urls(news_list):
        return [news.h4.a["href"] for news in news_list]

    @classmethod
    def news_content(cls, url):
        html = cls.get_html(url)
        soup = BeautifulSoup(html, "html.parser")
        title = soup.select(
            ".headline")[0].get_text(strip=True).encode('utf-8')
        content = soup.select(
            ".artical-main-content")[0].get_text(strip=True).encode('utf-8')
        return title.decode("utf-8"), content.decode("utf-8")
