import falcon
import ujson as json

class SymptomResource:

    def on_get(self, req, resp):

        resp.status = falcon.HTTP_200
        resp.body = json.dumps({
            "test": True
        })
