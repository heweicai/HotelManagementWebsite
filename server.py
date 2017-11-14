#!/usr/bin/env python
# coding=utf-8

import tornado.ioloop
import tornado.options
import tornado.httpserver

from wenxintang.application import application

from tornado.options import define, options

define("port", default=8002, help="run on the given port", type = int)

def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)

    print("Development server is running at http://127.0.0.1:%s" % options.port)
    print("Quit the server with Ctrl+F2")

    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()