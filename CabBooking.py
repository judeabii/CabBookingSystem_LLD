from abstract.CabBookingService import CabBookingService
from abstract.LocationService import LocationService


class CabBooking(CabBookingService):
    def __init__(self, location_service: LocationService):
        self.cabs = []
        self.location_service = location_service

    def registerCab(self, cab):
        self.cabs.append(cab)
        return f"{cab.carNumber} successfully registered"

    def getCab(self, rider):
        max_distance = 10
        for cab in self.cabs:
            if self.location_service.calcDistance(rider.location, cab.location) < max_distance and cab.availability:
                return cab
        return None
