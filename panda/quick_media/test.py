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
from panda.quick_media.weibo import Weibo
from panda.quick_media.baidu import Baidu
from panda.quick_media.zhihu import Zhihu
from panda.quick_media.v2ex import V2EX

Weibo.parse()
Baidu.parse()
Zhihu.parse()
V2EX.parse()
