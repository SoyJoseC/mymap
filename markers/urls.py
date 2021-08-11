from django.urls import path

from markers.views import MarkerView

urlpatterns = [
    path('map/', MarkerView.as_view()),
]
