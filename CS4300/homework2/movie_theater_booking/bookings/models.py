from django.db import models
from django.contrib.auth.models import User

#creates class movie with necessary variables
class Movie(models.Model):
    #limits the movie title to 200 chars
    title = models.CharField(max_length=200)
    #TextField is used for longer texts
    description = models.TextField()
    #DateField stores a caldendar date
    release_date = models.DateField()
    #PIF is used to store duration in minutes
    duration = models.PositiveIntegerField()

    def __str__(self):
        return self.title
#creates class seat with necessary variables
class Seat(models.Model):
    seat_number = models.CharField(max_length=10)
    #BooleanField is used to store true/false value
    is_booked = models.BooleanField(default=False)

    def __str__(self):
        return self.seat_number
#creates class Booking with necessary variables
class Booking(models.Model):
    #each of these ties the booking to one movie, when deleted also deletes related bookings
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    booking_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.movie.title} - {self.seat.seat_number}"
