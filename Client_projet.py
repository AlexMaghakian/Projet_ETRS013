# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 15:59:52 2021

@author: Alex
"""
import zeep
import psycopg2
from config import *
#Connexion à la base de donnée heroku
conn = psycopg2.connect(user = "ilawzmnlunxuiy",password = "5104cead965e1a18bc822c7611725f5e67cf99eb68f2db1c403ccc1d3b5f0050",host = "ec2-52-213-119-221.eu-west-1.compute.amazonaws.com",port = "5432",database = "damtnm2jbpjhko")
def infos_database():
    conn = psycopg2.connect(user = "ilawzmnlunxuiy",password = "5104cead965e1a18bc822c7611725f5e67cf99eb68f2db1c403ccc1d3b5f0050",host = "ec2-52-213-119-221.eu-west-1.compute.amazonaws.com",port = "5432",database = "damtnm2jbpjhko")
    cur = conn.cursor()
    # recupère le temps de chargement de la voiture où l'id=1
    cur.execute ("SELECT * from car where nom=nom")
    cur.execute ("SELECT * from car")
    #on stock le temps de chargement dans la variable temps_chargement1
    data = cur.fetchall()
    print(data[0])
    cur.close()
    conn.close()
    return data

def autonmie1():
    cur = conn.cursor()
    # recupère le temps de chargement de la voiture où l'id=1
    cur.execute ("SELECT autonomie from car where id=1")
    #on stock le temps de chargement dans la variable temps_chargement1
    autonomie1 = cur.fetchall()
    cur.close()
    conn.close()
    return autonomie1

def autonmie2():
    conn = psycopg2.connect(user = "ilawzmnlunxuiy",password = "5104cead965e1a18bc822c7611725f5e67cf99eb68f2db1c403ccc1d3b5f0050",host = "ec2-52-213-119-221.eu-west-1.compute.amazonaws.com",port = "5432",database = "damtnm2jbpjhko")
    cur = conn.cursor()
    # recupère le temps de chargement de la voiture où l'id=1
    cur.execute ("SELECT * from car where nom=nom")
    cur.execute ("SELECT * from car")
    #on stock le temps de chargement dans la variable temps_chargement1
    data = cur.fetchall()
    print(data[0])
    cur.close()
    conn.close()
    return data
#fermeture de la connexion à la base de données

    
#wsdl = 'http://127.0.0.1:8080/?wsdl'
#client = zeep.Client(wsdl=wsdl)

#infos=client.service.infos('Chambery', 'Valence',4)
#result = client.service.say_hello('Alex',9)
#print(result)
#result_time_addition = client.service.time_calculation(10,2)
#print(result_time_addition)

#time=client.service.time_calculation('200','2','1')
#print('time',time)
#infos_database('Renault Zoe')