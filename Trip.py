from abstract.TripService import TripService


class Trip(TripService):
    def __init__(self):
        self.rider = None
        self.cab = None
        self.tripStatus = None

    def createTrip(self, rider, cab):
        self.rider = rider
        self.cab = cab
        cab.setAvailability(False)
        self.setTripStatus("InProgress")
        return self

    def setTripStatus(self, tripStatus):
        self.tripStatus = tripStatus

    def getTripStatus(self):
        return self.tripStatus

    def __str__(self):
        return f"Trip Details:\n" \
               f"{self.cab}\n" \
               f"{self.rider}\n" \
               f"{self.tripStatus}"
