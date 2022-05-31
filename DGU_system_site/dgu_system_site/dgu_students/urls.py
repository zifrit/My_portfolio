from django.urls import path
from . import views


urlpatterns = [
    path('', views.AddStudent.as_view()),
    path('main/', views.start.as_view()),
]