from django.urls import path
from . import views

urlpatterns = [
    path('fetch-sat/', views.satellite_info_view, name='satellite_info'),
    path('fetch-schedule/', views.get_passage_info_view, name='passage_info'),
    path('fetch-available/', views.get_available_passes_view, name='booking_info'),
    path('book-pass/', views.book_passage_view, name="book_pass"),
]