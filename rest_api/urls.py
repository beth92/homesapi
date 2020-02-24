from django.urls import path
from . import views


urlpatterns = [
    path('homes', views.homes, name='homes'),
    path('homes/<int:home_id>', views.home_by_id, name='home-by-id'),
]
