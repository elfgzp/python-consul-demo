# -*- coding: utf-8 -*-

import tornado.ioloop
import tornado.web

from config import GREETING

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write(GREETING)


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
