# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 09:07:04 2021

@author: user
"""

from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

userlist={}

class Usersimple(Resource):
    def get(self, user_id):
        return {user_id: userlist[user_id]}

    def put(self, user_id):
        userlist[user_id] = request.form['data']
        return {'hello to you': userlist[user_id]}

api.add_resource(Usersimple, '/direbonjouraqqun')
api.add_resource(HelloWorld, '/direbonjour')

if __name__ == '__main__':
    app.run(debug=True)