import os
import tornado.httpserver
import tornado.ioloop
import tornado.web
from tornado import autoreload
import json

autoreload.start() 
print 'App Auto Reload...'
 
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello world")
        print "MainHandler get request"

class HomeHandler(tornado.web.RequestHandler):
    def post(self):
        data = json.loads(self.request.body)
        print data
        self.write(data)

    def get(self):
        print "Homehandler get request"
        self.write("Home")
 
def make_app():
    application = tornado.web.Application([
        (r"/", MainHandler),
        (r"/home", HomeHandler)
    ])
    return application

    http_server = tornado.httpserver.HTTPServer(application)
    port = int(os.environ.get("PORT", 5000))
    http_server.listen(port)
    tornado.ioloop.IOLoop.instance().start()
 
if __name__ == "__main__":
    app = make_app()
    #http_server = tornado.httpserver.HTTPServer(make_app())
    port = int(os.environ.get("PORT", 5000))
    #http_server.listen(port)
    app.listen(5000)
    print"Listening on port 5000"
    tornado.ioloop.IOLoop.current().start()
