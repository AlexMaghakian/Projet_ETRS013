# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 15:59:52 2021

@author: Alex
"""
import zeep
import psycopg2

#Connexion à la base de donnée heroku
try:
    conn = psycopg2.connect(
          user = "ilawzmnlunxuiy",
          password = "5104cead965e1a18bc822c7611725f5e67cf99eb68f2db1c403ccc1d3b5f0050",
          host = "ec2-52-213-119-221.eu-west-1.compute.amazonaws.com",
          port = "5432",
          database = "damtnm2jbpjhko"
    )
    cur = conn.cursor()

    # recupère le temps de chargement de la voiture où l'id=1
    cur.execute ("SELECT temps_chargement FROM car WHERE id=1") 
    #on stock le temps de chargement dans la variable temps_chargement1
    temps_chargement1 = cur.fetchall() 
    print(temps_chargement1)
    
    #fermeture de la connexion à la base de données


except (Exception, psycopg2.Error) as error :
    print ("Erreur lors de la connexion à PostgreSQL", error)
    
    
wsdl = 'http://127.0.0.1:8000/?wsdl'
client = zeep.Client(wsdl=wsdl)
result = client.service.say_hello('Alex',9)
print(result)
#♥result_time_addition = client.service.time_calculation(1,9, 2)
#print(result_time_addition)