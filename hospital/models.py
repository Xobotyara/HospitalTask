from django.db import models
from django.urls import reverse


class Hospital(models.Model):

    name = models.CharField(max_length=60, verbose_name='Наименование', help_text="Наименование медицинского учереждения")

    def __str__(self):
        return self.name


class Department(models.Model):

    name = models.CharField(max_length=60, verbose_name='Наименование', help_text="Наименование отделения")
    hospital = models.ForeignKey('Hospital', on_delete=models.CASCADE,
                                 verbose_name='Мед. учреждение', help_text="Медицинское учреждение, в котором находится отделение")

    def get_absolute_url(self):
        return reverse('department-detail', args=[str(self.id)])

    def __str__(self):
        return self.name


class Gender(models.Model):
    GENDER = (
        ('m', 'М'),
        ('f', 'Ж')
    )
    gender = models.CharField(max_length=1, choices=GENDER)

    def __str__(self):
        if self.gender == 'm':
            return 'Мужской'
        else:
            return 'Женский'


class Post(models.Model):

    name = models.CharField(max_length=60, verbose_name='Специальность',
                            help_text="Специальность служащего")

    def __str__(self):
        return self.name


class Cabinet(models.Model):

    number = models.CharField(
        max_length=10, blank=True, null=True, unique=True, verbose_name="Номер кабинета")

    name = models.CharField(max_length=60, blank=True, null=True,
                            verbose_name='Наименование', help_text="Наименование кабинета")

    department = models.ForeignKey('Department', on_delete=models.SET_NULL, blank=True, null=True,
                                   verbose_name='Отделение', help_text="Медицинское отделение, в котором находится кабинет")

    def get_absolute_url(self):
        return reverse('cabinet-detail', args=[str(self.id)])

    def __str__(self):
        return f'Кабинет "{self.name}" (Номер: {self.number})'


class Pacient(models.Model):

    name = models.CharField(max_length=30, verbose_name='Имя', db_index=True)
    surname = models.CharField(
        max_length=30, verbose_name='Фамилия', db_index=True)
    middlename = models.CharField(
        max_length=30, verbose_name='Отчеcтво', blank=True, null=True, db_index=True)
    gender = models.ForeignKey(
        'Gender', on_delete=models.PROTECT, verbose_name='Пол')
    birthday = models.DateField()
    amb_card = models.IntegerField(
        verbose_name='Номер абулаторной карты', unique=True)

    def get_absolute_url(self):
        return reverse('pacient-detail', args=[str(self.id)])

    def __str__(self):
        return f'{self.surname}, {self.name}, {self.middlename}'


class Medicine(models.Model):

    name = models.CharField(
        max_length=30, verbose_name='Название препарата', db_index=True)
    contraindication = models.CharField(
        max_length=300, verbose_name='Противопоказания', db_index=True,  blank=True, null=True)
    indication = models.CharField(
        max_length=300, verbose_name='Показания', db_index=True, blank=True, null=True)

    def get_absolute_url(self):
        return reverse('medicine-detail', args=[str(self.id)])

    def __str__(self):
        return self.name


class Procedure(models.Model):
    name = models.CharField(
        max_length=30, verbose_name='Название процедуры', db_index=True)
    info = models.CharField(
        max_length=300, verbose_name='Описание процедуры', blank=True, null=True)

    def get_absolute_url(self):
        return reverse('procedure-detail', args=[str(self.id)])

    def __str__(self):
        return self.name


class Diagnose(models.Model):
    name = models.CharField(
        max_length=30, verbose_name='Диагноз', db_index=True)
    info = models.CharField(
        max_length=300, verbose_name='Описание диагноза', blank=True, null=True)

    def get_absolute_url(self):
        return reverse('diagnose-detail', args=[str(self.id)])

    def __str__(self):
        return self.name


class Person(models.Model):
    name = models.CharField(max_length=30, verbose_name='Имя', db_index=True)
    surname = models.CharField(
        max_length=30, verbose_name='Фамилия', db_index=True)
    middlename = models.CharField(
        max_length=30, verbose_name='Отчеcтво', blank=True, null=True, db_index=True)
    gender = models.ForeignKey(
        'Gender', on_delete=models.PROTECT, verbose_name='Пол')
    post = models.ForeignKey('Post', on_delete=models.SET_NULL, blank=True, null=True,
                             verbose_name='Специальность', help_text="Специальность, по которой работает представитель персонала")
    departments = models.ManyToManyField(Department, blank=True, null=True,
                                   verbose_name='Отделения', help_text="Медицинские отделения, в которых числится работник")
    cabinets = models.ManyToManyField(Cabinet, verbose_name='Кабинеты', help_text='Список кабинетов, в которых может принимать работник')

    def get_absolute_url(self):
        return reverse('pacient-detail', args=[str(self.id)])

    def __str__(self):
        return f'{self.surname}, {self.name}, {self.middlename}: {self.post}'


class Reciept(models.Model):
    notice = models.CharField(
        max_length=300, blank=True, null=True, verbose_name='Описание рецепта')
    doctor = models.ForeignKey('Person', on_delete=models.PROTECT,
                               verbose_name='Врач', help_text='Врач, который выписал рецепт')
    pacient = models.ForeignKey('Pacient', on_delete=models.CASCADE,
                                verbose_name='Пациент', help_text='Пациент, которому выписан рецепт')
    diagnose = models.ForeignKey('Diagnose', on_delete=models.PROTECT,
                                 verbose_name='Диагноз', help_text='Диагноз, по которому выписан рецепт')
    medicines = models.ManyToManyField(
        Medicine, verbose_name='Препараты', help_text='Список препаратов по рецепту', blank=True, null=True)
    prucedures = models.ManyToManyField(
        Procedure, verbose_name='Процедуры', help_text='Список процедур, показанных по рецепту', blank=True, null=True)
    time_recieption = models.DateTimeField(verbose_name="Дата приема")

    def get_absolute_url(self):
        return reverse('reciept-detail', args=[str(self.id)])

    def __str__(self):
        return f'{self.doctor.name}, {self.doctor.surname} принял {self.pacient.name},  {self.pacient.surname}'
