from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
from .choices import PAYMENT_STATUS

from django.utils import timezone
import datetime

 
class CustomUser(AbstractUser):
    phone = models.CharField(max_length=30)
    usericon = models.ImageField(upload_to='media/',default='aa',blank=True)
    is_doctor = models.BooleanField(default=False,blank=True)
    is_nurse = models.BooleanField(default=False,blank=True)
    is_accountant = models.BooleanField(default=False,blank=True)
    is_labaratorist = models.BooleanField(default=False,blank=True)
    is_pharmacist = models.BooleanField(default=False,blank=True)
    is_patient = models.BooleanField(default=False,blank=True)
    is_admin = models.BooleanField(default=False,blank=True)
    is_receptionist = models.BooleanField(default=False,blank=True)

    def name(self):
        return self.first_name + " " + self.last_name
 