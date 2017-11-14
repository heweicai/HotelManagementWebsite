#!/usr/bin/env python
# coding=utf-8

# from wenxintang.url import url
#
# import tornado.web
# import os
#
# settings = dict(
#     template_path = os.path.join(os.path.dirname(__file__), "templates"),
#     static_path = os.path.join(os.path.dirname(__file__), "statics"),
#     debug = True      # 用于开发调试方便
#     )
#
# application = tornado.web.Application(
#     handlers = url,
#     **settings
#     )


from wenxintang.url import url

import tornado.web
import os

setting = dict(
    template_path = os.path.join(os.path.dirname(__file__), "templates"),
    static_path = os.path.join(os.path.dirname(__file__), "statics"),
    cookie_secret = "bZJc2sWbQLKos6GkHn/VB9oXwQt8S0R0kRvJ5/xJ89E=",
    xsrf_cookies = True,
    login_url = '/',
    debug = True      # 用于开发调试方便
)


application = tornado.web.Application(
    handlers = url,
    **setting
)
