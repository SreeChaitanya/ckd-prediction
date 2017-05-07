
# --- Tornado web framework libraries ---
import tornado.httpserver
import tornado.ioloop
from tornado.ioloop import IOLoop
import tornado.web
from tornado import autoreload
from tornado.options import define, options

# --- Misc python libraries ---
import sys, os

# --- Config file library ---
import ConfigParser

# --- API Controllers ---
from controllers.PredictionHandler import PredictionHandler

# ===============================================================================
#   Initialization Steps
# ===============================================================================
app_path = os.path.abspath(os.path.dirname(sys.argv[0]))
appcfg_filename = app_path + '/predictapi.cfg'
app_config = {}

# ---> Define command line parameters for the tornado arg parser
define("port", default=8000, help='run on the given port', type=int)

# ===============================================================================
#   Helper Functions
# ===============================================================================
def load_config(filename):
    appcfg = ConfigParser.ConfigParser()
    try:
        appcfg.read(filename)
    except:
        raise
    appcfg_sections = appcfg.sections()
    for sec_name in appcfg_sections:
        app_config[sec_name] = {}
        appcfg_options = appcfg.options(sec_name)
        for opt_name in appcfg_options:
            app_config[sec_name][opt_name] = appcfg.get(sec_name, opt_name)
    return app_config


class DemoHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello world!")
        print "Demo Handler get request"


class WebApp(tornado.web.Application):
    def __init__(self, config):
        self.config = config
        autoreload.start()
        print 'Application  Auto Reload...'
        rest_path = r'/api/001/'
        handlers = [('/?', DemoHandler),
                    (rest_path + r'predict/?', PredictionHandler.make_api())
                    ]
        settings = {
             'static_path': config['static_path']
             , 'template_path': config['template_path']
        }
        tornado.web.Application.__init__(self, handlers, **settings)

    def run(self, port=None, host=None):
        #port = int(os.environ.get("PORT", 8080))
        if host is None:
            host = self.config['bind_host']
        if port is None:
            port = self.config['bind_port']
        #http_server = tornado.httpserver.HTTPServer(self)
        #http_server.listen(port)
        self.listen(port)
        IOLoop.instance().start()
        #IOLoop.current().start()


def Main():
    tornado.options.parse_command_line()

    # ---> Load the app config data
    app_config = load_config(appcfg_filename)
    web_cfg = {}
    web_cfg['app_config'] = app_config
    web_cfg['template_path'] = os.path.join(os.path.dirname(__file__), 'templates')
    web_cfg['static_path'] = os.path.join(os.path.dirname(__file__), 'static')
    web_cfg['bind_host'] = app_config['server']['bind_host']
    web_cfg['bind_port'] = options.port
    if web_cfg['bind_port'] == 8000:
        web_cfg['bind_port'] = app_config['server']['bind_port']

    webapp = WebApp(web_cfg)
    # webapp = WebApp()
    webapp.run()
 
if __name__ == "__main__":
    Main()
    # app = make_app()
    # http_server = tornado.httpserver.HTTPServer(make_app())
    # port = int(os.environ.get("PORT", 8080))
    # http_server.listen(port)
    # print"Listening on port : "+(str(port))
    # tornado.ioloop.IOLoop.current().start()
