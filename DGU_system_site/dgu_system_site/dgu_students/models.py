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
    start_and_end_period = models.ForeignKey(to='SaEPeriod', null=True, default=None, on_delete=models.CASCADE,
                               verbose_name='начало/конец назначения')


class Course(models.Model):
    name = models.IntegerField(max_length=10)

    class Meta:
        db_table = 'Course'

    def __str__(self):
        return self.name


class ProfileStudent(models.Model):
    name = models.IntegerField(max_length=10)

    class Meta:
        db_table = 'ProfileStudent'

    def __str__(self):
        return self.name



class TypeStatus(models.Model):
    name = models.IntegerField(max_length=10)

    class Meta:
        db_table = 'TypeStatus'

    def __str__(self):
        return self.name



class SaEPeriod(models.Model):
    name = models.IntegerField(max_length=10)

    class Meta:
        db_table = 'SaEPeriod'

    def __str__(self):
        return self.name

