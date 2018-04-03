from flask import Flask, request
from flask.ext.restful import Resource, Api
todos = {"todo1":"你好","todo2":"问好","todo3":"test"}
class TodoSimple(Resource):
    def get(self, todo_id):
        return {todo_id: todos[todo_id]}

    def put(self, todo_id):
        todos[todo_id] = request.form['data']
        return {todo_id: todos[todo_id]}
