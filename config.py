# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 11:53:34 2021

@author: user
"""

import requests
import json

#Récuperer les valeurs de l'api https://opendata.reseaux-energies.fr/explore/dataset/bornes-irve/api/?disjunctive.region&geofilter.distance=48.8520930694,2.34738897685,1000&geofilter.polygon=&refine.region=%C3%8Ele-de-France&dataChart=eyJxdWVyaWVzIjpbeyJjaGFydHMiOlt7InR5cGUiOiJjb2x1bW4iLCJmdW5jIjoiQ09VTlQiLCJ5QXhpcyI6ImNvZGVfaW5zZWUiLCJzY2llbnRpZmljRGlzcGxheSI6dHJ1ZSwiY29sb3IiOiIjNjZjMmE1In1dLCJ4QXhpcyI6InJlZ2lvbiIsIm1heHBvaW50cyI6IiIsInRpbWVzY2FsZSI6IiIsInNvcnQiOiJzZXJpZTEtMSIsImNvbmZpZyI6eyJkYXRhc2V0IjoiYm9ybmVzLWlydmUiLCJvcHRpb25zIjp7ImRpc2p1bmN0aXZlLnJlZ2lvbiI6dHJ1ZSwiZ2VvZmlsdGVyLmRpc3RhbmNlIjoiNDguODUyMDkzMDY5NCwyLjM0NzM4ODk3Njg1LDEwMDAiLCJnZW9maWx0ZXIucG9seWdvbiI6IiIsInJlZmluZS5yZWdpb24iOiJcdTAwQ0VsZS1kZS1GcmFuY2UifX19XSwiZGlzcGxheUxlZ2VuZCI6dHJ1ZSwiYWxpZ25Nb250aCI6dHJ1ZSwidGltZXNjYWxlIjoiIn0%3D
url_ile_de_france = "https://opendata.reseaux-energies.fr/api/records/1.0/search/?dataset=bornes-irve&q=&facet=region&refine.region=%C3%8Ele-de-France&geofilter.distance=48.8520930694%2C2.34738897685%2C1000"
content=requests.get(url_ile_de_france)
data=content.json()
for distance in data["records"]:
        #afficher les distances du json
        print(distance["fields"]["dist"])
        #afficher les adresses du json
        print(distance["fields"]["ad_station"])
        

#Récuperer les valeurs de l'api https://opendata.reseaux-energies.fr/explore/dataset/bornes-irve/api/?disjunctive.region&geofilter.distance=48.8520930694,2.34738897685,1000&geofilter.polygon=&refine.region=%C3%8Ele-de-France&dataChart=eyJxdWVyaWVzIjpbeyJjaGFydHMiOlt7InR5cGUiOiJjb2x1bW4iLCJmdW5jIjoiQ09VTlQiLCJ5QXhpcyI6ImNvZGVfaW5zZWUiLCJzY2llbnRpZmljRGlzcGxheSI6dHJ1ZSwiY29sb3IiOiIjNjZjMmE1In1dLCJ4QXhpcyI6InJlZ2lvbiIsIm1heHBvaW50cyI6IiIsInRpbWVzY2FsZSI6IiIsInNvcnQiOiJzZXJpZTEtMSIsImNvbmZpZyI6eyJkYXRhc2V0IjoiYm9ybmVzLWlydmUiLCJvcHRpb25zIjp7ImRpc2p1bmN0aXZlLnJlZ2lvbiI6dHJ1ZSwiZ2VvZmlsdGVyLmRpc3RhbmNlIjoiNDguODUyMDkzMDY5NCwyLjM0NzM4ODk3Njg1LDEwMDAiLCJnZW9maWx0ZXIucG9seWdvbiI6IiIsInJlZmluZS5yZWdpb24iOiJcdTAwQ0VsZS1kZS1GcmFuY2UifX19XSwiZGlzcGxheUxlZ2VuZCI6dHJ1ZSwiYWxpZ25Nb250aCI6dHJ1ZSwidGltZXNjYWxlIjoiIn0%3D
#geofilter.distance=48.8520930694,2.34738897685,1000 == ile de france
url_ile_de_france = "https://opendata.reseaux-energies.fr/api/records/1.0/search/?dataset=bornes-irve&q=&facet=region&refine.region=%C3%8Ele-de-France&geofilter.distance=48.8520930694%2C2.34738897685%2C1000"
content=requests.get(url_ile_de_france)
data=content.json()
for distance in data["records"]:
        #afficher les distances du json
        print(distance["fields"]["dist"])
        #afficher les adresses du json
        print(distance["fields"]["ad_station"])
        print(distance["fields"]["xlongitude"])



def setDest(adresse_dest):
        # fonction 
        url = 'https://api-adresse.data.gouv.fr/search/?q='

        requete = url + adresse_dest
        requete += "&postcode="
        rqt = requests.get(requete)
        
        infosAddress = rqt.json() 
        
        features = infosAddress["features"]
        features_list = features[0]
        geometry = features_list["geometry"]
        coordonees = geometry["coordinates"]
        
        latitude_dst = str(coordonees[1])
        longitude_dst = str(coordonees[0])
        coordDest=[longitude_dst,latitude_dst]
        return  coordDest

def setSource(adresse_src):
        # fonction 
        url = 'https://api-adresse.data.gouv.fr/search/?q='

        requete = url + adresse_src
        requete += "&postcode="
        rqt = requests.get(requete)
        
        infosAddress = rqt.json() 
        
        features = infosAddress["features"]
        features_list = features[0]
        geometry = features_list["geometry"]
        coordonees = geometry["coordinates"]
        
        latitude_src = str(coordonees[1])
        longitude_src = str(coordonees[0])
        
        coordSrc=[longitude_src,latitude_src]
        return  coordSrc

      
###valence-bourget du lac
"""
lat=44.9488295
lon_1=4.9259615
lat_2=45.64720916748047
lon_2=5.860020160675049
"""

def  duration(coordDest,coordSrc):
        #coordDest=setDest('Valence')
        #coordSrc=setSource('Lyon')
        r = requests.get(f"http://router.project-osrm.org/route/v1/car/{coordDest[0]},{coordDest[1]};{coordSrc[0]},{coordSrc[1]}?overview=false""")
        # then you load the response using the json libray
        # by default you get only one alternative so you access 0-th element of the `routes`
        routes = json.loads(r.content)
        route_1 = routes.get("routes")[0]
        print('routes',routes)
        #print(route_1)
        time=(route_1["duration"])
        min=time/60
        heure=min/60
        print('min',min)
        print('heure',heure)
        return heure
        
"""
coordDest[0]='4.9259615'
coordDest[1]='44.9488295'
coordSrc[0]='5.860020160675049'
coordSrc[1]='45.64720916748047'
duration(coordDest[0],coordDest[1],coordSrc[0],coordSrc[1])
"""
