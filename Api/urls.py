from django.urls import path
from .views import EventsView

urlpatterns = [
  path('apitest/', EventsView.as_view()),
  path('apitest/<int:pk>/', EventsView.as_view()),
]