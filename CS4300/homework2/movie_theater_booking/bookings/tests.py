from django.test import TestCase
from django.contrib.auth.models import User
from .models import Movie, Seat, Booking

# creating tests
#Class for movie tests 
class MovieModelTest(TestCase):
    #function to test that the movie is created successfully in test database
    def test_movie_creation(self):
        movie = Movie.objects.create(
            title="The Lord of the Rings: The Fellowship of the Ring (Extended edition)",
            description="The best movie of all time about Frodo Baggins and his journey to destroy the one ring.",
            release_date="2001-12-19",
            duration=228
        )
        #verifys title and duration are stored correctly.
        self.assertEqual(movie.title, "The Lord of the Rings: The Fellowship of the Ring (Extended edition)")
        self.assertEqual(movie.duration, 228)

class SeatModelTest(TestCase):
    #creates temporary seats in test database
    def test_seat_creation(self):
        seat = Seat.objects.create(
            seat_number="A1"
        )
        #verifys that number and seat is not booked
        self.assertEqual(seat.seat_number, "A1")
        self.assertEqual(seat.is_booked, False)
    

class BookingModelTest(TestCase):
    #creates temporary booking with temp user
    def test_booking_creation(self):
        user = User.objects.create_user(
            username="testuser",
            password="testpassword"
        )
        #creates a movie
        movie = Movie.objects.create(
            title="The Lord of the Rings: The Fellowship of the Ring (Extended edition)",
            description="The best movie of all time about Frodo Baggins and his journey to destroy the one ring.",
            release_date="2001-12-19",
            duration=228
        )
        #creates a seat
        seat = Seat.objects.create(
            seat_number="A1"
        )
        #creates a booking that ties movie seat and user together
        booking = Booking.objects.create(
            movie=movie,
            seat=seat,
            user=user
        )
        #verifys all are pointed to the right record
        self.assertEqual(booking.movie, movie)
        self.assertEqual(booking.seat, seat)
        self.assertEqual(booking.user, user)
