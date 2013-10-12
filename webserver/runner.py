import logging
import tornado.httpserver
import tornado.ioloop
import tornado.web
import json
from tornado.options import define, options

# Define options that can be changed as we run this via the command line
define("port", default=8888, help="Run server on a specific port", type=int)
define("dbuser", default='hotdogsalad', help='Database username', type=str)
define('dbhost', default='localhost', help='Database server host/IP', type=str)
define('dbpassword', default='')


class TryJoinHandler(tornado.web.RequestHandler):
    def post(self):
        logging.info("Request to TryJoinHandler")
        request = None
        try:
            request = json.loads(self.request.body)
        except:
            logging.info("Bad JSON: " + self.request.body)
        if not hasattr(request, 'uuid') or not hasattr(request, 'username') or not hasattr(request, 'topic'):
            logging.info("Bad request")
            self.set_status(400)
            self.finish()
        self.write("hello")

    def get(self):
        self.write("hello")


application = tornado.web.Application([
                                          (r'/tryjoin', TryJoinHandler),
                                      ])

if __name__ == "__main__":
    http_server = tornado.httpserver.HTTPServer(application)
    tornado.options.parse_command_line()
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()