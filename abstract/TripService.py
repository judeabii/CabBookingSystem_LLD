from abc import ABC, abstractmethod


class TripService(ABC):
    @abstractmethod
    def createTrip(self, rider, cab):
        pass

    @abstractmethod
    def setTripStatus(self, tripStatus):
        pass

    @abstractmethod
    def getTripStatus(self):
        pass
