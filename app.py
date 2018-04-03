#http://www.pythondoc.com/Flask-RESTful/quickstart.html
#http://flask-restful.readthedocs.io/en/latest/quickstart.html

from flask import Flask, request
from flask.ext import restful
from flask.ext.restful import Resource, Api

from api.hello import HelloWorld
from api.todo import TodoSimple
from api.add import add

app = Flask(__name__)
api = restful.Api(app)


api.add_resource(HelloWorld, '/','/index')
api.add_resource(TodoSimple, '/<string:todo_id>')
api.add_resource(add, '/calc/add/<int:a>/<int:b>', endpoint='sss')

if __name__ == '__main__':
    app.run(debug=True)
