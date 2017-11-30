from gevent import monkey; monkey.patch_all()
from wsgiref import simple_server

import falcon

# resources
from resources import *

# middleware #
from middleware import JSONTranslator, RequireJSON

middleware = [RequireJSON(), JSONTranslator()]

app = falcon.API(middleware=middleware)

app.add_route('/symptoms', SymptomResource())

if __name__ == '__main__':
    httpd = simple_server.make_server('0.0.0.0', 5555, app)
    httpd.serve_forever()
