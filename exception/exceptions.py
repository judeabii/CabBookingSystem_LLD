class NoTripAvailable(Exception):
    def __init__(self):
        self.message = "No Cabs available right now. Please try again later!"
        super().__init__(self.message)


class NoRidesException(Exception):
    def __init__(self):
        self.message = "No rides available."
        super().__init__(self.message)


class TripNotStartedException(Exception):
    def __init__(self):
        self.message = "Cannot End Trip. Trip not Started Yet."
        super().__init__(self.message)


class AvailabilityValueException(Exception):
    def __init__(self, available):
        self.message = f"{available} is not valid. Availability should be a True/False."
        super().__init__(self.message)
