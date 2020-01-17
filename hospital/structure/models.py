from django.db import models

class Hospital(models.Model):
    title = models.CharField(max_length=150)
    short_title = models.CharField(max_length=20)
    tel1 = models.CharField(max_length=15)
    tel2 = models.CharField(max_length=15, blank=True, null=True)
    address = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='structure/logo/', blank=True)
    about = models.TextField(blank=True, null=True)
    history = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = 'Больница'
        verbose_name_plural = 'Больницы'

    def __str__(self):
        return self.title

class Office(models.Model):
    title = models.CharField(max_length=150)
    tel = models.CharField(max_length=15, blank=True, null=True)
    photo = models.ImageField(upload_to='structure/offices/', blank=True)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE, related_name='offices')
    about = models.TextField(blank=True, null=True)
    history = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ('-title',)
        verbose_name = 'Отделение'
        verbose_name_plural = 'Отделения'

    def __str__(self):
        return self.title

class Department(models.Model):
    title = models.CharField(max_length=150)
    tel = models.CharField(max_length=15, blank=True, null=True)
    photo = models.ImageField(upload_to='structure/departments/', blank=True)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE, related_name='departments')
    office = models.ForeignKey(Office, on_delete=models.SET_NULL, related_name='departments', blank=True, null=True)
    about = models.TextField(blank=True, null=True)
    history = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ('-title',)
        verbose_name = 'Блок'
        verbose_name_plural = 'Блоки'

    def __str__(self):
        return self.title

class Cabinet(models.Model):
    title = models.CharField(max_length=150)
    number = models.CharField(max_length=10)
    tel = models.CharField(max_length=15, blank=True, null=True)
    photo = models.ImageField(upload_to='structure/cabinets/', blank=True)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE, related_name='cabinets')
    office = models.ForeignKey(Office, on_delete=models.SET_NULL, related_name='cabinets', blank=True, null=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, related_name='cabinets', blank=True, null=True)
    about = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.title} ({self.number})'