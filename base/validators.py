from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User, Group
from django.core.exceptions import ValidationError
from rest_framework import serializers, viewsets
from django.core import validators
from datetime import datetime
from django.utils import timezone
from pygeocoder import Geocoder
from decimal import *
from datetime import datetime

def is_valid_phone_number(value):
    pass
#     if int(value) % 2 != 0:
#         raise ValidationError('%s is not an even number' % value)

        #todo
def validate_location(self):
    g = Geocoder()
    isvalid = False
    try:
        isvalid = g.geocode(self).valid_address
    except:
        raise ValidationError("No address was found.")
    if not isvalid:
        raise ValidationError("Please enter a valid address.")
def validate_starttime(self):
    from django.utils import timezone
    tzawaredate = self.replace(tzinfo=timezone.get_default_timezone())
    now = timezone.now()
    if tzawaredate<now:
        raise ValidationError("Please enter a valid start time in the future.")
