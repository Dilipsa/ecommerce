from django.db import models

# Create your models here.
class Home(models.Model):
    first_name = models.CharField(max_length  = 50)
    last_name  = models.CharField(max_length  = 50)
    user_name  = models.CharField(max_length  = 50)
    phone  = models.CharField(max_length  = 50)
    email      = models.EmailField(max_length = 50)
    password   = models.CharField(max_length  =20)
    password2   = models.CharField(max_length  =20)

    def __str__(self):
        return self.first_name
