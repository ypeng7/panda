# -*- coding: utf-8 -*-
""".

@file: base.py
@guid: bcb341edca6042748a54a96ef28fe2af

@author: Yue Peng
@email: yuepaang@gmail.com
@date: 2019-07-29 18:04:36
@modified:

@brief:
"""
__author__ = "Yue Peng"


class SocialMedia(object):

    @classmethod
    def parse(cls):
        raise NotImplementedError
