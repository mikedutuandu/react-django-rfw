# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


from django.contrib.auth.models import AbstractUser
from imagekit.processors import ResizeToFill
from imagekit.models import ImageSpecField

def upload_location(instance, filename):
    return "accounts/%s" % (filename)

class User(AbstractUser):
    email = models.EmailField(max_length=254, unique=True, blank=False)

    is_driver = models.BooleanField(default=False)
    driver_license = models.IntegerField()
    license_plate = models.CharField(max_length=255)
    vehicle_make = models.CharField(max_length=255)
    vehicle_model = models.CharField(max_length=255)
    vehicle_color = models.CharField(max_length=255)
    vehicle_year = models.IntegerField()
    working_days = models.CharField(max_length=255)
    avatar = models.ImageField(upload_to=upload_location,
                              null=False,
                              blank=False,
                                )
    avatar_thumb = ImageSpecField(source='avatar',
                                 processors=[ResizeToFill(200, 200)],
                                 format='JPEG',
                                 options={'quality': 60})
    timestamp = models.DateTimeField(auto_now_add=True)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ["username"]
