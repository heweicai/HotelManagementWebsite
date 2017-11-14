#!/usr/bin/env python
# coding=utf-8

# import tornado.web
# import wenxintang.methods.readdb as mrd
#
# class UserHandler(tornado.web.RequestHandler):
#     def get(self):
#         username = self.get_argument("user")
#         user_infos = mrd.select_table(table="users", column="*", condition="username", value=username)
#         self.render("user.html", user=user_infos)



import tornado.web
import tornado.escape
import wenxintang.methods.readdb as mrd
from wenxintang.handlers.base import BaseHandler

class UserHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        # username = self.get_argument("user")
        username = tornado.escape.json_decode(self.current_user)
        user_infos = mrd.select_table(table="users", column="*", condition="username", value=username)
        self.render("user.html", users=user_infos)


class GetUser(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        # username = self.get_argument("user")
        username = tornado.escape.json_decode(self.current_user)
        user_infos = mrd.select_table(table="users", column="*", condition="username", value=username)
        self.render("home.html", users=user_infos)


class UserContacts(BaseHandler):
    url = 'user/linkman.html'
    def get(self):
        self.render(self.url)
    def post(self):
        pass


class UserCulture(BaseHandler):
    def get(self):
        self.render("culture.html")
    def post(self):
        pass

class UserUs(BaseHandler):
    url = 'user/us.html'
    def get(self):
        self.render(self.url)
    def post(self):
        pass

class UserTools(BaseHandler):
    url = 'user/tools.html'
    def get(self):
        self.render(self.url)
    def post(self):
        pass

class UserLodge(BaseHandler):
    url = 'user/lodge.html'
    def get(self):
        self.render(self.url)
    def post(self):
        pass

class UserHelp(BaseHandler):
    url = 'user/userhelp.html'
    def get(self):
        self.render(self.url)
    def post(self):
        pass

class UserReservation(BaseHandler):
    url = 'user/reservation.html'
    def get(self):
        self.render(self.url)
    def post(self):
        pass