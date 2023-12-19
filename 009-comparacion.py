class Coordenadas:
    def __init__(self, lat , lon):
        self.lat = lat
        self.lon = lon

    def __eq__(self, otro):
        return self.lat == otro.lat and self.lon == otro.lon
    
    def __ne__(self, otro):
        return self.lat != otro.lat and self.lon != otro.lon

    def __lt__(self, otro):
        return self.lat + self.lon < otro.lat + otro.lon
    
    def __le__(self, otro):
        return self.lat + self.lon <= otro.lat + otro.lon

coord1 = Coordenadas(10, 10)
coord2 = Coordenadas(10, 10)

print (coord1 == coord2)
print (coord1 != coord2)
print(coord1 > coord2)
print(coord1 <= coord2)
