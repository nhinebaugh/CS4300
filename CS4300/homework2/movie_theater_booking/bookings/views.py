from django.shortcuts import render
from rest_framework import viewsets
from .models import Movie, Seat, Booking
from .serializers import MovieSerializer, SeatSerializer, BookingSerializer
# Create your views here.
#defines the django view function
def movie_list(request):
    #tell django to give all rows in movie table
    movies = Movie.objects.all()
    #loads the list and saves to variable called movies
    return render(
        request,
        'bookings/movie_list.html',
        {'movies': movies}
    )

def seat_booking(request):
    #tell django to give all rows in seats table
    seats = Seat.objects.all()
    #loads the list and saves to variable called seats
    return render(
        request,
        'bookings/seat_booking.html',
        {'seats': seats}
    )

def booking_history(request):
    #tell django to give all rows in booking table
    bookings = Booking.objects.all()
    #loads the list and saves to variable called bookings
    return render(
        request,
        'bookings/booking_history.html',
        {'bookings': bookings}
    )

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class SeatViewSet(viewsets.ModelViewSet):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    #function to ensure that when a seat is reserved it shows in the seats page as booked.
    def perform_create(self, serializer):
        booking = serializer.save()
        booking.seat.is_booked = True
        booking.seat.save()