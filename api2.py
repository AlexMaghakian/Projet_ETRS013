# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 09:29:04 2021

@author: Alex
"""
from flask import Flask, jsonify, request
app=Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if (request.method == 'POST'):
        test_json  = request.get_json()
        return jsonify({'Hello': test_json}), 201
    else:
        return jsonify ({'Hello Alex'})
    
@app.route('/multi/<int:num>', methods=['GET'])
def get_multiply2(num): 
    return jsonify ({'result': num*2})



if __name__ == '__main__':
    app.run(debug=True)
