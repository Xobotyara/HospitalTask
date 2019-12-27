from django.db import models
from django.urls import reverse

# Create your models here.
class Hospital(models.Model):
    
    name = models.CharField(max_length=60, help_text="Наименование медицинского учереждения")
        
    
    def __str__(self):
        return self.name

class Department(models.Model):

    name = models.CharField(max_length=60, help_text="Наименование отделения")
    hospital = models.ForeignKey('Hospital', on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('department-detail', args=[str(self.id)])

    def __str__(self):
        return self.name