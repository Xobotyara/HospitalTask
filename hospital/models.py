from django.db import models
from django.urls import reverse


class Hospital(models.Model):

    name = models.CharField(verbose_name='Наименование',
                            max_length=60,
                            help_text="Наименование медицинского учереждения")

    def __str__(self):
        return self.name

class Department(models.Model):

    name = models.CharField(verbose_name='Наименование',
                            max_length=60,
                            help_text="Наименование отделения")
    hospital = models.ForeignKey('Hospital',
                                 on_delete=models.CASCADE,
                                 verbose_name='Мед. учреждение',
                                 help_text="Медицинское учреждение, в котором находится отделение")

    def get_absolute_url(self):
        return reverse('department-detail', args=[str(self.id)])

    def __str__(self):
        return self.name

class Sex(models.Model):
    SEX = (
        ('m', 'М'),
        ('f', 'Ж')
    )
    sex = models.CharField(max_length=1, choices=SEX)

    def __str__(self):
        return self.name
