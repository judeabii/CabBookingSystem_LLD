from abc import ABC, abstractmethod


class CabBookingService(ABC):
    @abstractmethod
    def getCab(self, rider):
        pass
