#!/usr/bin/env python
# coding=utf-8

import pymysql

conn = pymysql.connect(
    host="localhost",    # 本地数据库,等同于localhost
    user="chinaoly",
    password="654123",
    db="testbase",
    port=3306,
    charset="utf8"
)    # 连接对象

cur = conn.cursor()    # 游标对象