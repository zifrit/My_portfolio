from django.shortcuts import render

# Create your views here.
from django.views import View
from .models import Student
from .addition.test import pp


class AddStudent(View):
    def get(self, request):
        # print(request.POST('FIO_input', False))
        return render(request, 'dgu_students/start.html', {})

    def post(self, request):
        FIO = request.POST.get('FIO_input')
        course = request.POST.get('FIO_input')
        profile_student = request.POST.get('FIO_input')
        type_status = request.POST.get('FIO_input')
        start_and_end_period = request.POST.get('FIO_input')
        faculty = request.POST.get('FIO_input')
        # print(text)
        pp(request)
        return render(request, 'dgu_students/start.html', {'key': 'post запрос'})


class start(View):
    def get(self, request):
        print('get')
        return render(request, 'base.html', {})

    def post(self, request):
        print('post')
        return render(request, 'base.html', {'key': 'fuck'})
