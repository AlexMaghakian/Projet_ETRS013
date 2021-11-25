# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 15:59:52 2021

@author: Alex
"""
import zeep
import psycopg2

#Connexion à la base de donnée heroku
def autonomie():
    try:
        conn = psycopg2.connect(
            user = "NcgkvMjQrX",
            password = "NcgkvMjQrX",
            host = "sql11.freesqldatabase.com",
            port = "3306",
            database = "sql11454096"
        )
        cur = conn.cursor()

        # recupère le temps de chargement de la voiture où l'id=1
        cur.execute ("SELECT autonomie FROM car WHERE id=1") 
        #on stock le temps de chargement dans la variable temps_chargement1
        autonomie = cur.fetchall() 
        print(autonomie)
        
        #fermeture de la connexion à la base de données


    except (Exception, psycopg2.Error) as error :
        print ("Erreur lors de la connexion à PostgreSQL", error)
     
wsdl = 'http://127.0.0.1:8000/?wsdl'
client = zeep.Client(wsdl=wsdl)
#result = client.service.say_hello('Alex',9)
#print(result)
result_time_addition = client.service.time_calculation(10,2)
print(result_time_addition)