from django.test import TestCase
from django.contrib.auth.models import User
from .models import Movie, Seat, Booking
from rest_framework.test import APIClient
from rest_framework import status

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

class APITest(TestCase):

    def setUp(self):
        # making HTTP requests to REST API.
        self.client = APIClient()

        # Create a test user
        self.user = User.objects.create_user(
            username="testuser",
            password="testpassword"
        )

        # Create a movie that can be used by multiple tests.
        self.movie = Movie.objects.create(
            title="The Lord of the Rings: The Fellowship of the Ring (Extended edition)",
            description="The best movie of all time about Frodo Baggins and his journey to destroy the one ring.",
            release_date="2001-12-19",
            duration=228
        )

        # Create an available seat for booking tests.
        self.seat = Seat.objects.create(
            seat_number="A1",
            is_booked=False
        )

    def test_get_movies(self):
        # Send a GET request to the movie API endpoint.
        response = self.client.get('/api/movies/')

        # Verify that the API returned HTTP 200 OK.
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        # Verify that one movie was returned.
        self.assertEqual(len(response.data), 1)

        # Verify that the returned movie has the expected title.
        self.assertEqual(
            response.data[0]['title'],
            "The Lord of the Rings: The Fellowship of the Ring (Extended edition)",
        )

    def test_create_movie(self):
        # Data that will be sent to the API as a new movie.
        movie_data = {
            "title": "Inception",
            "description": "A film about weird dreams",
            "release_date": "2010-07-16",
            "duration": 148
        }

        # Send a POST request to create the movie.
        response = self.client.post(
            '/api/movies/',
            movie_data,
            format='json'
        )

        # A successful REST creation should return HTTP 201.
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        # Verify that the new movie was actually saved.
        self.assertEqual(Movie.objects.count(), 2)

    def test_get_seats(self):
        # Request the list of seats.
        response = self.client.get('/api/seats/')

        # Verify that the endpoint responds successfully.
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        # Verify that our test seat was returned.
        self.assertEqual(len(response.data), 1)

    def test_create_booking(self):
        # A Booking uses the database IDs of the related
        # Movie, Seat, and User objects.
        booking_data = {
            "movie": self.movie.id,
            "seat": self.seat.id,
            "user": self.user.id
        }

        # Send a POST request to the bookings endpoint.
        response = self.client.post(
            '/api/bookings/',
            booking_data,
            format='json'
        )

        # Verify that the booking was created successfully.
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        # Verify that one Booking now exists.
        self.assertEqual(Booking.objects.count(), 1)

        # Refresh the seat object from the database so we
        # receive its newest is_booked value.
        self.seat.refresh_from_db()

        # Verify that making the booking marked the seat booked.
        self.assertEqual(self.seat.is_booked, True)

    def test_double_booking_prevention(self):

        # Mark the seat as already booked.
        self.seat.is_booked = True
        self.seat.save()

        # Attempt to create another booking using that seat.
        booking_data = {
            "movie": self.movie.id,
            "seat": self.seat.id,
            "user": self.user.id
        }

        response = self.client.post(
            '/api/bookings/',
            booking_data,
            format='json'
        )

        # A validation failure should return HTTP 400 Bad Request.
        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )

        # Verify that no booking was created.
        self.assertEqual(
            Booking.objects.count(),
            0
        )
