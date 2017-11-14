#!/usr/bin/env python
# coding=utf-8

import wenxintang.methods.readdb as mrd
#from wenxintang.handlers.base import BaseHandler
class IndexHandler():    #继承base.py中的类BaseHandler
    def get(self):
        usernames = mrd.select_columns(table="users",column="username")
        one_user = usernames[0][0]
        print(one_user)

print(IndexHandler())