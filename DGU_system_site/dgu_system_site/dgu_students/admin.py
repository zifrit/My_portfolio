from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('FIO', 'course', 'profile_student')
    list_filter = ('course', 'profile_student', 'type_status', 'start_and_end_period')
    pass


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    pass


@admin.register(ProfileStudent)
class ProfileStudentAdmin(admin.ModelAdmin):
    pass


@admin.register(TypeStatus)
class TypeStatusAdmin(admin.ModelAdmin):
    pass


@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    pass
