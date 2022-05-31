from django.urls import path
from . import views

urlpatterns = [
    path('register-student', views.AddStudent.as_view(), name='register-student'),
    path('', views.MainPage.as_view()),
]
