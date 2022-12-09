from django.db import models


# Create your models here.
class LatestWork(models.Model):
    image = models.ImageField(verbose_name="Фото", upload_to='Latestwork/%m/%d')  # %Y year
    title = models.CharField(verbose_name="Описание", max_length=20)

    def __str__(self):
        return self.title


class Student(models.Model):
    GENDER = [
        ('M', 'Мужской'),
        ('W', 'Женщина')
    ]
    COURSE = [
        ('first', '1'),
        ('second', '2'),
        ('third', '3'),
        ('fourth', '4'),
        ('fifth', '5')
    ]
    FEE = [
        ('contract', 'Контракт'),
        ('grand', 'Бюджет')
    ]
    # change to pep8
    fname = models.CharField(verbose_name='Имя', max_length=25)
    lname = models.CharField(verbose_name='Фамилия', max_length=25)
    age = models.IntegerField(verbose_name='Возраст')  # change to positive
    aboutme = models.TextField(verbose_name='О себе')  # write with under space
    gender = models.CharField(verbose_name='Пол', choices=GENDER,max_length=3)
    course = models.CharField(verbose_name='Курс', choices=COURSE, default='1',max_length=8)  # change to integer
    fee = models.CharField(verbose_name='Оплата',choices=FEE,max_length=8)  # change to understand name
    # profession = link
    ##################################---Связь--#####################################
    is_active = models.BooleanField(verbose_name='Подтвержденный?')  # small like shit
    university = models.CharField(verbose_name='Университет',help_text='Название',max_length=25)

    def __str__(self):
        return f'{self.fname} {self.lname}'

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural  = 'Студенты'
