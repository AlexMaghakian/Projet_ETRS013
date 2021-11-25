from logging import info
import urllib.request, json
from geopy.geocoders import Nominatim
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def parsage(data):
    infos = ""
    for items in data["records"]:
        infos += str(items["fields"]["ad_station"])+" à "+str(round(float(items["fields"]["dist"])))+"m.\n"
        #print ("Distance vers borne  "+str(items["fields"]["dist"]))  si je veux distance vers borne, c ici (pour distance totale)
    return infos ## return to nearbornes


def nearBornes(lat, long, peri):    
    # Récupération du json avec les params.
    with urllib.request.urlopen("https://opendata.reseaux-energies.fr/api/records/1.0/search/?dataset=bornes-irve&q=&facet=region&geofilter.distance="+str(lat)+"%2C"+str(long)+"%2C"+str(peri)+"") as url:
        data = json.loads(url.read().decode())
    
   # Vérification de la présence de bornes dans le périmetre.
    if data["nhits"] == 0:
        peri = peri + 5000
        ## au dessus , ça augmente la largeur de périmètre recherche de borne
        ## if peri > xx , mettre une limite au périmètre de recherche ==> 
        #infos = "Pas de borne à moins de "+peri+"km"
        #break 
        infos = nearBornes(lat, long, peri)
    else:
        infos = parsage(data)
        
    return infos ## return vers need break



def trajectory(departure, arrival, carautonomy, marginseekingborne):

    departure = requestCoordonates(departure)
    arrival = requestCoordonates(arrival)
    coord = str(departure.latitude)+","+str(departure.longitude)+";"+str(arrival.latitude)+","+str(arrival.longitude)

    Trajectorydistancereq = "http://router.project-osrm.org/route/v1/driving/"+coord+"?overview=false"
    with urllib.request.urlopen(Trajectorydistancereq) as url:
        data = json.loads(url.read().decode())

    for items in data["routes"]:
        for elements in items["legs"]:
            distance = elements["distance"]
    distance = distance/1000

    listStop = needBreak(departure.latitude, departure.longitude, arrival.latitude, arrival.longitude, distance, carautonomy, marginseekingborne)
  
    print("\n\nDistance a parcourir :"+str(distance)+"  hors écart pour les bornes\n\n")
    print("Liste des arrêtes:\n\n"+str(listStop))
   ## print("Distance a parcourir : en prenant en compte les détours pour les bornes") si somme des distances relevés vers bornes +*2 (écart route, retour sur route...)
    return "\n\nDistance a parcourir :"+str(distance)+"\n\n"+str(listStop)  ## reutrn vers affichage principal


def needBreak(latDep, longDep, latArr, longArr, dist, carautonomy, marginseekingborne ):
## c ici qu'on peut ajouter la pec de la marge (en % ou fixée) (car = car-marge , ce qui force ajout de marge dans recherche des bornes)
    distcar= carautonomy - marginseekingborne
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

            #print("########## \n\n\n"+str(latDep)+"\n"+str(longDep)+"\n\n\n##########\n")
            listStop += "Arret n°"+str(nbr)+": \n\n"+str(nearBornes (latDep, longDep, 5000))+"\n\n"
            nrbBreak = nrbBreak - 1
        return listStop ## return vers trajectory




def requestCoordonates(city):
    geolocator = Nominatim(user_agent="ATR")
    coord = geolocator.geocode(city)
    return coord


trajectory("Lyon","Nantes",200,50)
## 400 autonomy
## 50 margin (how many km before running out of electrecity do we devy to get to "recharger")