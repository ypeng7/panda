# -*- coding: utf-8 -*-
""".

@file: test.py
@guid: 08da7a52d0024fc1a5c14b459f6affc5

@author: Yue Peng
@email: yuepaang@gmail.com
@date: 2019-07-29 23:11:15
@modified:

@brief:
"""
__author__ = "Yue Peng"
from panda.social_media.weibo import Weibo
from panda.social_media.baidu import Baidu
from panda.social_media.zhihu import Zhihu
from panda.social_media.v2ex import V2EX
from panda.social_media.github import GitHub

Weibo.get_trending()
Baidu.get_trending()
Zhihu.get_trending()
V2EX.get_trending()
GitHub.get_trending()
