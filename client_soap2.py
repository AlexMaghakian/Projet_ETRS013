# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 15:59:52 2021

@author: Alex
"""
import zeep
import psycopg2
from config import *
import MySQLdb

#Connexion à la base de donnée heroku
#conn = mysql.connect(user = ,password = "NcgkvMjQrX",host = "sql11.freesqldatabase.com",port = "3306",database = "sql11454096")
db=MySQLdb.connect(host="sql11.freesqldatabase.com",user="sql11454096",passwd="NcgkvMjQrX",db="sql11454096")


def get_autonomie(car) -> tuple[str,int,int]:
    request = 'SELECT nom, chargement, autonomie FROM car WHERE nom ="'+car+'"'
    db.query(request)
    result= db.store_result()
    fetched_result = result.fetch_row(maxrows=0)
    print(fetched_result)      
    return fetched_result[0]

       


def get_time():
    wsdl = 'http://127.0.0.1:8080/?wsdl'
    client = zeep.Client(wsdl=wsdl)
    fetched_result=get_autonomie()
    time=client.service.time_calculation('200',fetched_result[2],fetched_result[1])
    return time
    

    
wsdl = 'http://127.0.0.1:8080/?wsdl'
client = zeep.Client(wsdl=wsdl)
fetched_result=get_autonomie('Renault Zoe')
time=client.service.time_calculation('200',fetched_result[2],fetched_result[1])
#all=get_autonomie('Renault Zoe')
#xxx=all[0]
#print(xxx)
