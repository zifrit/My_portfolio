from django.db import models


# Create your models here.


class Student(models.Model):
    FIO = models.CharField(max_length=100, verbose_name='ФИО студента')
    course = models.ForeignKey(to='Course', null=True, default=None, on_delete=models.CASCADE,
                               verbose_name='курс студента')
    profile_student = models.ForeignKey(to='ProfileStudent', null=True, default=None, on_delete=models.CASCADE,
                               verbose_name='профиль студента')
    type_status = models.ForeignKey(to='TypeStatus', null=True, default=None, on_delete=models.CASCADE,
                               verbose_name='вид стипендии/статус студента')
    start_and_end_period = models.CharField(max_length=100, verbose_name='дата назначения', null=True , default=None)
    faculty = models.ForeignKey(to='Faculty', null=True, default=None, on_delete=models.CASCADE,
                               verbose_name='факультет')

class Course(models.Model):
    name = models.CharField(max_length=10)

    class Meta:
        db_table = 'Course'

    def __str__(self):
        return self.name
class ProfileStudent(models.Model):
    name = models.CharField(max_length=10)

    class Meta:
        db_table = 'ProfileStudent'

    def __str__(self):
        return self.name
class TypeStatus(models.Model):
    name = models.CharField(max_length=10)

    class Meta:
        db_table = 'TypeStatus'

    def __str__(self):
        return self.name
class Faculty(models.Model):
    name = models.CharField(max_length=10)

    class Meta:
        db_table = 'Faculty'

    def __str__(self):
        return self.name

