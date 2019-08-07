# -*- coding: utf-8 -*-
""".

@file: zhihu.py
@guid: 17627f42e6ed4defb8b26bcaa124322e

@author: Yue Peng
@email: yuepaang@gmail.com
@date: 2019-07-29 22:51:35
@modified:

@brief:
"""
__author__ = "Yue Peng"

from lxml import etree

from panda.social_media.base import SocialMedia
from panda.social_media.helper import get_text


class Zhihu(SocialMedia):
    ZHIHU_REDIAN = "https://www.zhihu.com/hot"
    HEADERS = {
        "user-agent": "Baiduspider",
        "cookie": f"_zap=c9245bd9-4c33-4336-8ba8-5b3dd669f112; "
        f"_xsrf=25zbdplpf8g1eOTx8liThpJvjXIKNFpU; d_c0=\""
        f"AHCjLZP2vA-PTm5R4BJliqFfV0GHoca7-pc=|1563159142\"; "
        f"q_c1=03225c2e9e0c496fbd456e6b19b22d2c|1563358352000|1563358352000; "
        f"__utmv=51854390.100-1|2=registration_date=20161012=1^3=entry_date="
        f"20161012=1; tst=h; __utma=51854390.1006290711.1563358355.1563358355."
        f"1563540380.2; __utmz=51854390.1563540380.2.2.utmcsr=360doc.com"
        f"|utmccn="
        f"(referral)|utmcmd=referral|utmcct="
        f"/content/18/0119/13/25592655_723341899."
        f"shtml; tgw_l7_route=060f637cd101836814f6c53316f73463; tshl=; "
        f"capsion_ticket=\"2|1:0|10:1563586609|14:capsion_ticket|44:"
        f"ODIwNzM4N2I0YWJjNDczMzgyNjllNmUwZjZlZGJjMjc="
        f"|54fa40fb14fc3e8fdf90a1e36c33278a6b2b872de7d9c914e"
        f"a71eab9942d14b6\"; "
        f"z_c0=\"2|1:0|10:1563586611|4:z_c0|92:"
        f"Mi4xQXBPUEF3QUFBQUFBY0tNdGtfYThEeVlBQUFCZ0FsVk5NNzRmWGdEaDl6NnJndHB2"
        f"M3RCSlJIb3o4LTJlc0lKU05B|4c3cb58a8ea6615d1d6"
        f"db372165a0199daed52f908ec"
        f"02cd7665a41abe166a2b\""
    }

    @classmethod
    def get_trending(cls):
        r = get_text(cls.ZHIHU_REDIAN, cls.HEADERS)
        r.encoding = "utf-8"
        soup = etree.HTML(r.text)
        for soup_a in soup.xpath("//div[@class='HotItem-content']/a"):
            zhihu_title = soup_a.get('title')
            zhihu_url = soup_a.get('href')
            print(f"Name: {zhihu_title}, URL: {zhihu_url}")
