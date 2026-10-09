from rest_framework import serializers
from .models import Movie, Seat, Booking

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

class SeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seat
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'

    # Validate the seat field before allowing the booking to be created.
    def validate_seat(self, seat):

        # If the selected seat is already booked,
        # reject the request with a clear API error.
        if seat.is_booked:
            raise serializers.ValidationError(
                "This seat is already booked."
            )

        # If the seat is available, return it so validation can continue.
        return seat
        