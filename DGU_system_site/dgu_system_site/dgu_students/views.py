from django.shortcuts import render

# Create your views here.
from django.views import View
from .models import Student
from .addition.add_student import add_student


class AddStudent(View):
    def get(self, request):
        return render(request, 'dgu_students/start.html', {})

    def post(self, request):
        if add_student(request):
            return render(request, 'dgu_students/start.html', {})
        return render(request, 'dgu_students/start.html', {'key': 'Проверьте на пробелы в конце!!'})


class MainPage(View):
    def get(self, request):
        print('get')
        return render(request, 'base.html', {})

    def post(self, request):
        print('post')
        return render(request, 'base.html', {'key': 'fuck'})
