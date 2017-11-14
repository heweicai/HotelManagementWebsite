#!/usr/bin/env python
# coding=utf-8


# import tornado.web
# import wenxintang.methods.readdb as mrd
#
# class IndexHandler(tornado.web.RequestHandler):
#     def get(self):
#         greeting = self.get_argument('greeting', 'V2.0版本，Hello')
#         self.write(greeting + '， 欢迎来到温馨堂! 温馨之家，温暖大家。。。')
#
#         self.render("index.html")
#
#     # post方法
#     def post(self):
#         username = self.get_argument("username")
#         password = self.get_argument("password")
#         user_infos = mrd.select_table(table="users", column="*", condition="username", value=username)
#         if user_infos:
#             db_pwd = user_infos[0][2]
#             if db_pwd == password:
#                 self.write("欢迎您: " + username)
#             else:
#                 self.write("您的密码不正确.")
#         else:
#             self.write("尚未注册的用户，请注册.")
import tornado.escape
import wenxintang.methods.readdb as mrd
from wenxintang.handlers.base import BaseHandler

class IndexHandler(BaseHandler):    #继承base.py中的类BaseHandler
    def get(self):
        usernames = mrd.select_columns(table="users", column="username")
        one_user = usernames[0][0]
        #current_time = mrd.select_time()
        #administrator = mrd.select_tab(table="administrator", column="*", condition="name")
        #new_administrator = administrator[0][0]
        greeting = self.get_argument('greeting', 'V2.0版本')
        self.write(greeting + '， 欢迎登录温馨堂大酒店管理系统')
        #self.render("index.html", admin = new_administrator, user = one_user)
        self.render("index.html", user=one_user)

    def post(self):
        username = self.get_argument("username")
        password = self.get_argument("password")
        user_infos = mrd.select_table(table="users", column="*", condition="username", value=username)
        if user_infos:
            db_pwd = user_infos[0][2]
            if db_pwd == password:
                self.set_current_user(username)    # 将当前用户名写入cookie，方法见下面
                self.write("欢迎您: " + username)
            else:
                self.write("您的密码不正确.")
        else:
            self.write("尚未注册的用户，请注册.")

    def set_current_user(self, user):
        if user:
            self.set_secure_cookie('user', tornado.escape.json_encode(user))    # 注意这里使用了tornado.escape.json_encode()方法
        else:
            self.clear_cookie("user")


class HomeHandler(BaseHandler):
    def get(self):
        self.render("home.html")

    def post(self):
        pass

class ErrorHandler(BaseHandler):    # 增加了一个专门用来显示错误的页面
    def get(self):                                        # 但是后面不单独讲述，读者可以从源码中理解
        self.render("error.html")