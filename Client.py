from Cab import Cab
from Location import Location
from CabBooking import CabBooking
from Rider import Rider
from Trip import Trip
from exception.exceptions import NoRidesException, NoTripAvailable, TripNotStartedException, AvailabilityValueException


def main():
    try:
        location_service = Location()
        trip_service = Trip()
        cab_service = CabBooking(location_service)
        rider1 = Rider(name="Jude", id=123)
        rider1.setLocation((0, 0))
        cab1 = Cab(id=23, driverName="Abishek", carNumber="KA03MR1042")
        cab1.setLocation((0, 4))

        print(rider1)
        print(cab1)

        print(cab_service.registerCab(cab1))

        print(rider1.bookRide(cab_service, trip_service))
        print(cab1.endTrip(trip_service))
    except NoTripAvailable as e:
        print(str(e))
    except ValueError as e:
        print(str(e))
    except NoRidesException as e:
        print(str(e))
    except TripNotStartedException as e:
        print(str(e))
    except AvailabilityValueException as e:
        print(str(e))


if __name__ == "__main__":
    main()