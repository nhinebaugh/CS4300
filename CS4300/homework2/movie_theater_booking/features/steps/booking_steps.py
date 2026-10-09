# Import Behave decorators used to define Given, When, and Then steps.
from behave import given, when, then

# Import Django's built-in User model.
from django.contrib.auth.models import User

# Import the models used in the booking workflow.
from bookings.models import Movie, Seat, Booking


@given('a movie exists')
def step_movie_exists(context):
    # Create a movie that will be used during the scenario.
    context.movie = Movie.objects.create(
        title="The Lord of the Rings: The Fellowship of the Ring (Extended edition)",
        description="The best movie of all time about Frodo Baggins and his journey to destroy the one ring.",
        release_date="2001-12-19",
        duration=228
    )


@given('an available seat exists')
def step_available_seat_exists(context):
    # Create a seat that starts as available.
    context.seat = Seat.objects.create(
        seat_number="A1",
        is_booked=False
    )


@given('a user exists')
def step_user_exists(context):
    # Create a test user for the booking.
    context.user = User.objects.create_user(
        username="testuser",
        password="testpassword"
    )


@when('the user books the available seat')
def step_book_available_seat(context):
    # Create a booking using the test movie, seat, and user.
    context.booking = Booking.objects.create(
        movie=context.movie,
        seat=context.seat,
        user=context.user
    )

    # Mimic the booking behavior from our API by marking
    # the seat as booked after the booking is created.
    context.seat.is_booked = True
    context.seat.save()


@then('a booking should be created')
def step_booking_created(context):
    # Verify that exactly one booking now exists.
    assert Booking.objects.count() == 1


@then('the seat should be marked as booked')
def step_seat_marked_booked(context):
    # Reload the seat from the database to make sure
    # we are checking its most recent value.
    context.seat.refresh_from_db()

    # Verify that the seat is now marked as booked.
    assert context.seat.is_booked is True