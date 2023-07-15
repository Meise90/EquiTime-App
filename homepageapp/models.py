from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class PhoneModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number format: '+999999999'. Up to 15 digits allowed.")
    phone_number = PhoneNumberField(validators=[phone_regex], blank=True, null=True)


    def __str__(self):
        return f"{self.phone_number}"
