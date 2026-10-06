from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(
    r'movies',
    views.MovieViewSet,
    basename='movie'
)

router.register(
    r'seats',
    views.SeatViewSet,
    basename='seat'
)

router.register(
    r'bookings',
    views.BookingViewSet,
    basename='booking'
)

urlpatterns = [
    path('', views.movie_list, name='movie_list'),
    path('seats/', views.seat_booking, name='seat_booking'),
    path('history/', views.booking_history, name='booking_history'),
    path('api/', include(router.urls))
]