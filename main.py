import os
import tornado.httpserver
import tornado.ioloop
from tornado.ioloop import IOLoop
import tornado.web
from tornado import autoreload
import json

from controllers import PredictionHandler

autoreload.start() 
print 'App Auto Reload...'
 
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello world! New code here")
        print "MainHandler get request"

# class HomeHandler(tornado.web.RequestHandler):
#     def post(self):
#         data = json.loads(self.request.body)
#         print data
#         self.write(data)
#     def get(self):
#         print "Homehandler get request"
#         self.write("Home")
#
# def make_app():
#     application = tornado.web.Application([
#         (r"/", MainHandler),
#         (r"/home", HomeHandler)
#     ])
#     return application

class WebApp(tornado.web.Application):
    def __init__(self):
        autoreload.start()
        rest_path = r'/api/001/'
        handlers = [(r"/?", MainHandler),
                    (rest_path + 'predict/', PredictionHandler)
                    ]
        settings = {
        }
        tornado.web.Application.__init__(self, handlers) #, **settings)

    def run(self, port = None, host = None):
        port = int(os.environ.get("PORT", 8080))
        self.listen(port)
        IOLoop.instance().start()


def Main():
    webapp = WebApp()
    webapp.run()
 
if __name__ == "__main__":
    Main()
    # app = make_app()
    # http_server = tornado.httpserver.HTTPServer(make_app())
    # port = int(os.environ.get("PORT", 8080))
    # http_server.listen(port)
    # print"Listening on port : "+(str(port))
    # tornado.ioloop.IOLoop.current().start()
