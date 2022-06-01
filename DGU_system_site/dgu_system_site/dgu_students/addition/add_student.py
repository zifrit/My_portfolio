from dgu_students.models import Student, Course


def add_student(request):
    FIO = request.POST.get('FIO_input')
    course = request.POST.get('course_input')
    profile_student = request.POST.get('profile_student_input')
    type_status = request.POST.get('type_status_input')
    start_and_end_period = request.POST.get('start_and_end_period_input')
    faculty = request.POST.get('faculty_input')
    print(request.POST.get('FIO_input'))

    try:
        if Course.objects.get(name=str(course)[:-1]):
            print('success')
            return True
        else:
            print('fail')
    except:
        print('fail_1')
        return False
    # print(Course.objects.get(name='1'))

# if __name__ == "__main__":
#     pass
