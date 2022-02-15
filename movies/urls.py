from django.urls import path
from .views       import *

urlpatterns = [
	path('/movies', MovieView.as_view()),
        path('/actors', ActorView.as_view()),
]
