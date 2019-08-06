# -*- coding: utf-8 -*-
""".

@file: __init__.py
@guid: 0c42850d5b4f463faaf1a7ab845b5af7

@author: Yue Peng
@email: yuepaang@gmail.com
@date: 2019-07-29 18:00:51
@modified:

@brief:
"""
import importlib

__author__ = "Yue Peng <yuepaang@gmail.com>"
__version__ = "0.0.1"
__doc__ = "Self-use python scripts"
__name__ = "panda"

__all__ = ["social_media"]


def __getattr__(name):
    if name in __all__:
        return importlib.import_module("."+name, __name__)
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
