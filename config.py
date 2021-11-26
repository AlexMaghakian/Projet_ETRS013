# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 11:53:34 2021

@author: user
"""

import requests
import json
from logging import info
import urllib.request, json
from geopy.geocoders import Nominatim
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)




#fonction qui permet de recuperer les coordonnées gps (longitude,latitude) d'une destination 
def get_destination(adresse_dest):
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

#fonction qui permet de retourner les coordonnées gps (longitude,latitude) d'une source
def get_source(adresse_src): 
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

#fonction qui permet de calculer la durée d'un trajet à partir des cordonnées gps récupérées par les fonction get_source et get_destination
def duration(coordDest,coordSrc):

        #coordDest=get_destination('Valence')
        #coordSrc=get_source('Lyon')
        r = requests.get(f"http://router.project-osrm.org/route/v1/car/{coordDest[0]},{coordDest[1]};{coordSrc[0]},{coordSrc[1]}?overview=false""")
        # then you load the response using the json libray
        # by default you get only one alternative so you access 0-th element of the `routes`
        routes = json.loads(r.content)
        route_1 = routes.get("routes")[0]
        print('route_1',route_1)
        print('routes',routes)
        #print(route_1)
        time=(route_1["duration"])
        min=time/60
        heure=min/60
        print('min',min)
        print('heure',heure)
        return heure


#Récuperer les valeurs de l'api https://opendata.reseaux-energies.fr/explore/dataset/bornes-irve/api/?disjunctive.region&geofilter.distance=48.8520930694,2.34738897685,1000&geofilter.polygon=&refine.region=%C3%8Ele-de-France&dataChart=eyJxdWVyaWVzIjpbeyJjaGFydHMiOlt7InR5cGUiOiJjb2x1bW4iLCJmdW5jIjoiQ09VTlQiLCJ5QXhpcyI6ImNvZGVfaW5zZWUiLCJzY2llbnRpZmljRGlzcGxheSI6dHJ1ZSwiY29sb3IiOiIjNjZjMmE1In1dLCJ4QXhpcyI6InJlZ2lvbiIsIm1heHBvaW50cyI6IiIsInRpbWVzY2FsZSI6IiIsInNvcnQiOiJzZXJpZTEtMSIsImNvbmZpZyI6eyJkYXRhc2V0IjoiYm9ybmVzLWlydmUiLCJvcHRpb25zIjp7ImRpc2p1bmN0aXZlLnJlZ2lvbiI6dHJ1ZSwiZ2VvZmlsdGVyLmRpc3RhbmNlIjoiNDguODUyMDkzMDY5NCwyLjM0NzM4ODk3Njg1LDEwMDAiLCJnZW9maWx0ZXIucG9seWdvbiI6IiIsInJlZmluZS5yZWdpb24iOiJcdTAwQ0VsZS1kZS1GcmFuY2UifX19XSwiZGlzcGxheUxlZ2VuZCI6dHJ1ZSwiYWxpZ25Nb250aCI6dHJ1ZSwidGltZXNjYWxlIjoiIn0%3D
#geofilter.distance=48.8520930694,2.34738897685,1000 == ile de france
def bornes(adresse_src,adresse_dest,dist):
        coordSrc=get_source(adresse_src)
        coordDest=get_destination(adresse_dest)
        url = "https://opendata.reseaux-energies.fr/api/records/1.0/search/?dataset=bornes-irve&q=&facet=region&refine.region=%C3%8Ele-de-France&geofilter.distance={long},{lat},{dist}"
        content=requests.get(url)
        data=content.json()
        for distance in data["records"]:
                #afficher les distances du json
                print(distance["fields"]["dist"])
                #afficher les adresses du json
                print(distance["fields"]["ad_station"])
                print(distance["fields"]["xlongitude"])
               
"""
coordDest[0]='4.9259615'
coordDest[1]='44.9488295'
coordSrc[0]='5.860020160675049'
coordSrc[1]='45.64720916748047'
duration(coordDest[0],coordDest[1],coordSrc[0],coordSrc[1])
"""


def parseur(data):
    infos = ""
    for items in data["records"]:
        infos += str(items["fields"]["ad_station"])+" à "+str(round(float(items["fields"]["dist"])))+"m.\n"
        #print ("Distance vers borne  "+str(items["fields"]["dist"]))  si je veux distance vers borne, c ici (pour distance totale)
    return infos ## return to BorneClose


#fonction qui cherche et retourne la liste des arrêts pour chaque etapes dans un certain perimètre
def BorneClose(lat, long, peri):    
    # Récupération du json avec les params.
    with urllib.request.urlopen("https://opendata.reseaux-energies.fr/api/records/1.0/search/?dataset=bornes-irve&q=&facet=region&geofilter.distance="+str(lat)+"%2C"+str(long)+"%2C"+str(peri)+"") as url:
        data = json.loads(url.read().decode())
    
   # Vérification de la présence de bornes dans le périmetre.
    if data["nhits"] == 0:
        peri = peri + 5000
        infos = BorneClose(lat, long, peri)
    else:
        infos = parseur(data)
        
    return infos

#fonction qui permet de calculer la distance entre 2 villes
#je recupere les coordonnée gps lat long des fonctions get_source et get_destination et je les inseère dans l'url de l'api
def calcul_distance(depart, arrive):
        coordSrc=get_source(depart)
        coordDest=get_destination(arrive)
        r = requests.get(f"http://router.project-osrm.org/route/v1/car/{coordDest[0]},{coordDest[1]};{coordSrc[0]},{coordSrc[1]}?overview=false""")
        dist = json.loads(r.content)
        dist_1 = dist.get("routes")[0]
        for items in dist["routes"]:
            for elements in items["legs"]:
                distance = elements["distance"]
                distance=distance/1000
                #print('distance',distance)
        #distance=(dist_1["distance"])
        #distance = dist.get("distance")
        #print('distance',distance)
        return distance

    
#fonction qui peret de tracer une ligne droite et de couper en part egale à l'autonomie
#permet de trouver des bornes pour chaque etapes
def trajectoire(depart, arrivee, autonomy, marge):

    depart = requestCoordonates(depart)
    arrivee = requestCoordonates(arrivee)
    coord = str(depart.latitude)+","+str(depart.longitude)+";"+str(arrivee.latitude)+","+str(arrivee.longitude)

    Trajectoiredistancereq = "http://router.project-osrm.org/route/v1/driving/"+coord+"?overview=false"
    with urllib.request.urlopen(Trajectoiredistancereq) as url:
        data = json.loads(url.read().decode())

    for items in data["routes"]:
        for elements in items["legs"]:
            distance = elements["distance"]
    distance = distance/1000

    listStop = needBreak(depart.latitude, depart.longitude, arrivee.latitude, arrivee.longitude, distance, autonomy, marge)
  
    print("\n\nDistance a parcourir :"+str(distance)+"  hors écart pour les bornes\n\n")
    print("Liste des arrêts:\n\n"+str(listStop))
    #print("Distance a parcourir : en prenant en compte les détours pour les bornes")
    return "\n\nDistance a parcourir :"+str(distance)+"\n\n"+str(listStop)

#fonction permet de diviser diviser la trajectoire en plusieurs etapes et donner la localisation des etapes pour les reutiliser dans la fonction trajectoire 
def needBreak(latDep, longDep, latArr, longArr, dist, autonomy, marge ):
## c ici qu'on peut ajouter la pec de la marge (en % ou fixée) (car = car-marge , ce qui force ajout de marge dans recherche des bornes)
    distcar= autonomy - marge
    if dist < distcar:
        return 0
    else:
        nrbBreak = round(dist/distcar)
        latDist = latDep - latArr
        longDist = longDep - longArr

        latEtapedist = latDist / nrbBreak
        longEtapedist = longDist / nrbBreak

        nbr = 0
        listStop = ""
        while nrbBreak != 0:
            nbr += 1

            if latDep < latArr:
                latDep = latDep + latEtapedist
            else: 
                latDep = latDep - latEtapedist
            if longDep > longArr:
                longDep = longDep + longEtapedist
            else:
                longDep = longDep - longEtapedist

            listStop += "Arret n°"+str(nbr)+": \n\n"+str(BorneClose (latDep, longDep, 5000))+"\n\n"
            nrbBreak = nrbBreak - 1
        return listStop ## return vers trajectoire




def requestCoordonates(city):
    geolocator = Nominatim(user_agent="ATR")
    coord = geolocator.geocode(city)
    return coord


#trajectoire("Lyon","Nantes",200,50)
## 400 autonomy
## 50 margin (how many km before running out of electrecity do we devy to get to "recharger")
#coordDest=get_destination('Valence')
#coordSrc=get_source('Lyon')
#duration(coordSrc,coordDest)
#calcul_distance('Chambéry', 'Valence')