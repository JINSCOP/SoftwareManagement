from flask.ext import restful
from da.user import hello_world

class HelloWorld(restful.Resource):
    def get(self):
        return {'hello': 'world'}
