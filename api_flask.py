 # -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 09:07:02 2021

@author: user
"""
from flask import Flask
from flask_restful import Resource, Api
from flask import Flask, redirect, url_for, render_template, request, flash
from config import *

app = Flask(__name__)
api = Api(app)
"""
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/')

class Response():
    status = 200
    mimetype = "text/html"
   
class Usersimple(Resource):
    def get(self, user_id):
        return Response(response=render_template('index.html'))

    def put(self, user_id):
        userlist[user_id] = request.form['data']
        return {'hello to you': userlist[user_id]}
"""

coordDest=get_destination('Valence')
coordSrc=get_source('Paris')
@app.route("/")
def index():
    return render_template("index.html");


@app.route('/test',methods=['GET', 'POST'])
def resultat():
    duree=''
    if request.method == 'GET':
        #depart = request.args.get('depart')
        #arrivee = request.args.get('arrivee')
        return render_template("index.html")
    else:             
        depart = request.form.get("depart")
        arrivee = request.form.get("arrivee")
        
        #arrivee=get_destination(arrivee)
        #depart=get_source(depart)
        #print(arrivee)
        #print(depart)
        coordDest=get_destination(arrivee)
        coordSrc=get_destination(depart)
        distance=calcul_distance(depart,arrivee)
        bornes=trajectory(depart, arrivee, 200, 50)
        #bornes=nearBornes(coordSrc[0], coordSrc[1], 50)
        duree=duration(coordDest,coordSrc)
        return render_template("index.html",depart=depart,arrivee=arrivee, duree=duree, distance=distance,bornes=bornes)

    

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)