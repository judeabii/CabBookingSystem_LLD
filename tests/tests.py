import unittest
from Rider import Rider
from Cab import Cab
from Trip import Trip
from Location import Location
from CabBooking import CabBooking
from exception.exceptions import NoTripAvailable, NoRidesException, TripNotStartedException, \
    AvailabilityValueException


class TestRiders(unittest.TestCase):
    def setUp(self) -> None:
        self.rider = Rider(name="Jude", id=123)

    def test_add_location(self):
        self.rider.setLocation((0, 4))
        self.assertEqual(self.rider.location, (0, 4))

    def test_invalid_location(self):
        with self.assertRaises(ValueError):
            self.rider.setLocation(123)

    def test_get_no_rides(self):
        with self.assertRaises(NoRidesException):
            self.rider.getRides()

    def test_bookRides_no_cab(self):
        location_service = Location()
        cab_cooking_service = CabBooking(location_service)
        trip_service = Trip()
        self.rider.setLocation((0, 2))
        with self.assertRaises(NoTripAvailable):
            self.rider.bookRide(cab_cooking_service, trip_service)

    def test_rider_attributes(self):
        self.assertEqual(self.rider.name, "Jude")
        self.assertEqual(self.rider.id, 123)


class TestCabs(unittest.TestCase):
    def setUp(self) -> None:
        self.cab = Cab(id=23, driverName="Abishek", carNumber="KA03MR1042")

    def test_add_location(self):
        self.cab.setLocation((0, 4))
        self.assertEqual(self.cab.location, (0, 4))
        self.assertEqual(isinstance(self.cab.location, tuple), True)

    def test_invalid_location(self):
        with self.assertRaises(ValueError):
            self.cab.setLocation(1)

    def test_set_availability(self):
        self.cab.setAvailability(True)
        self.assertEqual(self.cab.availability, True)
        self.cab.setAvailability(False)
        self.assertEqual(self.cab.availability, False)

    def test_invalid_availability(self):
        with self.assertRaises(AvailabilityValueException):
            self.cab.setAvailability("True")

    def test_end_invalid_trip(self):
        trip_service = Trip()
        with self.assertRaises(TripNotStartedException):
            self.cab.endTrip(trip_service)

    def test_rider_attributes(self):
        self.assertEqual(self.cab.id, 23)
        self.assertEqual(self.cab.driverName, "Abishek")
        self.assertEqual(self.cab.carNumber, "KA03MR1042")


class TestTrips(unittest.TestCase):
    def setUp(self) -> None:
        self.trip = Trip()
        self.rider = Rider(name="Jude", id=123)
        self.cab = Cab(id=23, driverName="Abishek", carNumber="KA03MR1042")

    def test_create_trip(self):
        self.trip.createTrip(self.rider, self.cab)
        self.assertEqual(self.trip.rider, self.rider)
        self.assertEqual(self.trip.cab, self.cab)
        self.assertEqual(self.cab.availability, False)
        self.assertEqual(self.trip.tripStatus, "InProgress")


class TestCabService(unittest.TestCase):
    def setUp(self) -> None:
        self.location_service = Location()
        self.cabBooking = CabBooking(self.location_service)
        self.cab = Cab(id=23, driverName="Abishek", carNumber="KA03MR1042")
        self.cab.setLocation((0, 4))

    def test_register_cab(self):
        self.cabBooking.registerCab(self.cab)
        self.assertIn(self.cab, self.cabBooking.cabs)

    def test_get_cab(self):
        rider = Rider(id=12, name="Jude")
        rider.setLocation((0, 0))
        self.cabBooking.registerCab(self.cab)
        available_cab = self.cabBooking.getCab(rider)
        self.assertEqual(available_cab, self.cab)


class TestCabBooking(unittest.TestCase):
    def setUp(self) -> None:
        self.rider = Rider(id=123, name="Jude")
        self.cab = Cab(id=23, driverName="Abishek", carNumber="KA03MR1042")
        self.location_service = Location()
        self.trip_service = Trip()
        self.cab_service = CabBooking(self.location_service)
        self.cab_service.registerCab(self.cab)

    def test_success_booking(self):
        self.cab.setLocation((0, 4))
        self.rider.setLocation((0, 0))
        trip = self.rider.bookRide(self.cab_service, self.trip_service)
        self.assertIsInstance(trip, Trip)
        self.assertEqual(trip.tripStatus, "InProgress")
        self.assertEqual(self.cab.availability, False)
        self.assertIn(trip, self.rider.rides)

    def test_end_booking(self):
        self.cab.setLocation((0, 4))
        self.rider.setLocation((0, 0))
        trip = self.rider.bookRide(self.cab_service, self.trip_service)
        self.cab.endTrip(self.trip_service)
        self.assertEqual(self.cab.availability, True)
        self.assertEqual(trip.tripStatus, "Ended")


if __name__ == "__main__":
    unittest.main()
