from abstract.LocationService import LocationService


class Location(LocationService):
    def calcDistance(self, locationA, locationB):
        x1, x2 = locationA
        y1, y2 = locationB
        return int(((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5)
