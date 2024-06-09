from abstract.CabBookingService import CabBookingService
from abstract.TripService import TripService
from exception.exceptions import NoRidesException, NoTripAvailable
from Cab import Cab


class Rider:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.rides = []
        self.location = None

    def getRides(self):
        if len(self.rides) == 0:
            raise NoRidesException()
        else:
            return self.rides

    def bookRide(self, cab_booking_service: CabBookingService, trip_service: TripService):
        cab = cab_booking_service.getCab(self)
        if isinstance(cab, Cab):
            tripCreated = trip_service.createTrip(self, cab)
            self.rides.append(tripCreated)
            return tripCreated
        else:
            raise NoTripAvailable()

    def setLocation(self, location):
        if isinstance(location, tuple):
            self.location = location
            return f"Rider location set to {self.location}"
        else:
            raise ValueError("Location must be a tuple")

    def getLocation(self):
        return self.location

    def __str__(self):
        return f"Rider Name: {self.name}\n" \
               f"Rider Location: {self.location}"
