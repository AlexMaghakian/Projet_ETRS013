from enum import auto
from math import cos, asin, sqrt, pi
import googlemaps
from datetime import datetime
import json


class GPS_Computer():
    def __init__(self):
        self.gmaps = googlemaps.Client(key='AIzaSyDYnH0q6tP6wrhP5urfn43OFCAHbjI31mM')
        pass 

    def get_distance_between_coordinates(self, lat1: float, lon1: float, lat2: float, lon2: float):
        """
        Renvoie la distance en km entre deux coordoonnées GPS 
        """
        p = pi/180
        a = 0.5 - cos((lat2-lat1)*p)/2 + cos(lat1*p) * cos(lat2*p) * (1-cos((lon2-lon1)*p))/2
        return 12742 * asin(sqrt(a)) #2*R*asin...

    def get_coordinates_from_address(self, address: str) -> tuple[float,float]:
        """ Récupère les coordonnées GPS d'une addresse donnée en argument
        via l'API Google Maps """
        geocode_result = self.gmaps.geocode(address)
        lat = geocode_result[0].get("geometry").get("location").get("lat")
        lon = geocode_result[0].get("geometry").get("location").get("lng")
        return lat, lon

    def get_distance_between_addresses(self, address1: str, address2: str):
        lat, lon = self.get_coordinates_from_address(address1)
        lat2, lon2, = self.get_coordinates_from_address(address2)
        distance = self.get_distance_between_coordinates(lat,lon,lat2,lon2)
        return distance

    def get_travel_time(self, ville_depart: str, ville_arrivee: str, autonomie: int, temps_charge: int):
        """
        Args:
            autonomie: autonomie en km
            temps_charge: Temps de charge en minutes 

        Returns:
            Temps de trajet en minutes = temps sur la route + temps à charger
        """
        distance = self.get_distance_between_addresses(ville_depart,ville_arrivee)
        driving_time = self.get_driving_time_between_addresses(ville_depart,ville_arrivee)

        if distance < autonomie:
            travel_time = driving_time
            return travel_time

        if distance >= autonomie:
            #le temps de trajet sera égal au temps de conduite + de recharge 
            number_of_charges_needed = distance // autonomie
            travel_time = driving_time + number_of_charges_needed*temps_charge
            return travel_time

    def get_driving_time_between_addresses(self,address1,address2):
        dir = self.gmaps.directions(address1,address2)
        driving_time_seconds = dir[0]['legs'][0]['duration']['value']
        driving_time_minutes = driving_time_seconds/60
        return driving_time_minutes
    
    def get_coordinates_at_specific_distance_between_coordinates(
        self,distance: float, start_lat: float, start_lon: float, 
        end_lat: float, end_lon: float) -> tuple[float,float]:
        
        dist_btw_coords = self.get_distance_between_coordinates(start_lat,start_lon,end_lat,end_lon)
        
        #Ce ratio sert à calculer le vecteur pour calculer les coordonnées
        ratio = distance/dist_btw_coords

        #Calcule le vecteur de distance entre les points
        lat_vector = end_lat-start_lat
        lon_vector = end_lon-start_lon

        #Calcul du vecteur qui servira à obtenir les nouvelles coordonnées
        lat_vector*=ratio
        lon_vector*=ratio

        #On ajoute le nouveau vecteur aux coordonnées initiales 
        lon = start_lon + lon_vector
        lat = start_lat + lat_vector

        return lat, lon


if __name__ == "__main__":
    comp = GPS_Computer()
    time = comp.get_travel_time("Amancy","Paris", 200,0)
    print(time)





        

class Test_GPS_Computer():
    def test_get_distance_between_coordinates(self):
        computer = GPS_Computer()
        dist = computer.get_distance_between_coordinates(46.0642062,6.3010021,45.9273625,6.1629627)
        assert type(dist) == float
        return dist
    
    def test_get_coordinates_from_address(self):
        computer = GPS_Computer()
        lat,lon = computer.get_coordinates_from_address("Sopra Steria Annecy")
        assert type(lat) == float
        assert type(lon) == float
        return lat, lon
    
    def test_get_distance_between_addresses(self):
        computer = GPS_Computer()
        dist = computer.get_distance_between_addresses("Amancy", "Annecy")
        assert type(dist) == float 
        return dist
    
    def test_get_driving_time_between_addresses(self):
        computer = GPS_Computer()
        time = computer.get_driving_time_between_addresses("Amancy","Annecy")
        assert type(time) == float
        return time

    def test_get_coordinates_at_specific_distance_between_coordinates(self):
        computer = GPS_Computer()
        lat, lon = computer.get_coordinates_from_address("Amancy")
        lat2, lon2 = computer.get_coordinates_from_address("Annecy")
        lat3, lon3 = computer.get_coordinates_at_specific_distance_between_coordinates(20,lat,lon,lat2,lon2)
        assert type(lat3) == float
        assert type(lon3) == float 
        
        dist = computer.get_distance_between_coordinates(lat,lon, lat3,lon3)
        assert type(dist) == float
        assert dist > 19
        assert dist < 21

