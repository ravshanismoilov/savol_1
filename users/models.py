from django.db import models
from django.contrib.auth.models import AbstractUser



class CustomUser(AbstractUser):
    image = models.ImageField(upload_to='users_images/', blank=True, null=True, default='media/default_img/user_img.png')


    class Meta:
        db_table = 'customuser'

    def __str__(self):
        return self.username