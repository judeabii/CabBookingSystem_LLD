from abstract.TripService import TripService
from exception.exceptions import AvailabilityValueException, TripNotStartedException


class Cab:
    def __init__(self, id, driverName, carNumber):
        self.id = id
        self.driverName = driverName
        self.carNumber = carNumber
        self.availability = True
        self.location = None

    def setLocation(self, location):
        if isinstance(location, tuple):
            self.location = location
            return f"Cab location set to {self.location}"
        else:
            raise ValueError("Location must be a tuple")

    def getLocation(self):
        return self.location

    def setAvailability(self, available):
        if isinstance(available, bool):
            self.availability = available
        else:
            raise AvailabilityValueException(available)

    def endTrip(self, trip_service: TripService):
        if trip_service.getTripStatus() != "InProgress":
            raise TripNotStartedException()
        else:
            trip_service.setTripStatus("Ended")
            self.setAvailability(True)
            return "Trip Ended successfully."

    def __str__(self):
        return f"Cab ID: {self.id}\n" \
               f"Driver Name: {self.driverName}\n" \
               f"Car Number: {self.carNumber}\n" \
               f"Cab Location: {self.location}"
