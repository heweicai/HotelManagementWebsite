#!/usr/bin/env python
# coding=utf-8

from wenxintang.methods.db import *

def select_table(table, column, condition, value ):
    sql = "select " + column + " from " + table + " where " + condition + "='" + value + "'"
    cur.execute(sql)
    lines = cur.fetchall()
    return lines

def select_columns(table, column ):
    sql = "select " + column + " from " + table
    cur.execute(sql)
    lines = cur.fetchall()
    return lines

def select_time( ):
    sql = "select now()"
    cur.execute(sql)
    lines = cur.fetchall()
    return lines

def select_tab(table, column, condition):
    sql = "select" + column + "from" + table + "where" + condition + "is not null order by id"
    cur.execute(sql)
    lines = cur.fetchall()
    return lines