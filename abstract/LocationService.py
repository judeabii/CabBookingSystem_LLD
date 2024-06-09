from abc import abstractmethod, ABC


class LocationService(ABC):
    @abstractmethod
    def calcDistance(self, locationA, locationB):
        pass
