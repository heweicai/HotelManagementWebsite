#!/usr/bin/env python
# coding=utf-8
"""
the url structure of website

"""

# import importlib     # utf-8，兼容汉字
# importlib.reload(sys)
from wenxintang.handlers.index import IndexHandler    # 从index模块引入IndexHandler方法
from wenxintang.handlers.index import HomeHandler
from wenxintang.handlers.user import UserHandler      # 从user模块引入UserHandler方法
from wenxintang.handlers.user import UserContacts
from wenxintang.handlers.user import UserCulture
from wenxintang.handlers.user import UserUs
from wenxintang.handlers.user import UserTools
from wenxintang.handlers.user import UserLodge
from wenxintang.handlers.user import UserHelp
from wenxintang.handlers.user import GetUser
from wenxintang.handlers.user import UserReservation
from wenxintang.handlers.sysmanagement import SysManagementHome

url = [
    (r'/', HomeHandler),
    (r'/index', IndexHandler),
    (r'/home', GetUser),
    (r'/user', UserHandler),
    (r'/user/linkman', UserContacts),
    (r'/culture', UserCulture),
    (r'/user/us', UserUs),
    (r'/user/tools', UserTools),
    (r'/user/lodge', UserLodge),
    (r'/user/userhelp', UserHelp),
    (r'/user/reservation', UserReservation),
    (r'/sysmanagement/home', SysManagementHome)
]