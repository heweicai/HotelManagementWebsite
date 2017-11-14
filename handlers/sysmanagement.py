#!/usr/bin/env python
# coding=utf-8

import tornado.web
import tornado.escape
import wenxintang.methods.readdb as mrd
from wenxintang.handlers.base import BaseHandler

class SysManagementHome(BaseHandler):
    url = 'sysmanagement/home.html'
    def get(self):
        self.render(self.url)

    def post(self):
        pass