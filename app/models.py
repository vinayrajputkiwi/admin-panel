from django.db import models
from django.core.exceptions import ValidationError
# Create your models here.
def validate_email(value):
    if "@kiwitech.com" in value:
        return value
    else:
        raise ValidationError("This field accepts kiwitech mail only")


class Register(models.Model,):
    full_name=models.CharField(max_length=50)
    email=models.EmailField(unique=True,max_length=100,validators=[validate_email])
    password=models.CharField(max_length=50)
    password1=models.CharField(max_length=50)

class Otp(models.Model):
      email=models.EmailField(max_length=50)
      otp=models.CharField(max_length=50)
