from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Person(models.Model):

    GENDER_CHOICES = (
        ('m', 'Мужской'),
        ('f', 'Женский'),
    )
    ROLE_CHOICES = (
        ('a', 'Администрация'),
        ('d', 'Врач'),
        ('p', 'Пациент'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    third_name = models.CharField(max_length=100,  blank=True, null=True)
    avatar = models.ImageField(upload_to='persons/avatars/%m/', blank=True, null=True)
    photo = models.ImageField(upload_to='persons/photos/%m/', blank=True, null=True)
    birth_date = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default='m')
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='p')
    bio = models.TextField(max_length=500, blank=True, null=True)
  

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    def __str__(self):
        return f'{self.user.username}'

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()