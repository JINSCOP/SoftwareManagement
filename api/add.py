from flask.ext.restful import Resource, Api
from funcs.calc import calc
class add(Resource):
    def get(self, a,b):
        return {'result': calc.add(a,b)}
