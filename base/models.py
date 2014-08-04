from django.db import models
from django.db.models.signals import post_save
from django.core.exceptions import ValidationError
from rest_framework import serializers, viewsets
from django.core import validators
from datetime import datetime
from django.utils import timezone
from pygeocoder import Geocoder
from decimal import *
from datetime import datetime
from django.contrib.auth.models import User, Group
from base.validators import *

class Recipe(models.Model):
    def creator_profile_id(self):
        return self.creator.profile().pk 
    def creator_read_only(self):
        return self.creator
    def upcooking_score(self):
        try:
            return self.creator.get_profile().upcooking_score
        except:
            return 0
    docfile = models.FileField(upload_to='recipes', default='recipes/no-img.jpg', blank=False)
    docfile2 = models.FileField(upload_to='recipes', default='recipes/no-img.jpg', blank=False)
    docfile3 = models.FileField(upload_to='recipes', default='recipes/no-img.jpg', blank=False)
    docfile4 = models.FileField(upload_to='recipes', default='recipes/no-img.jpg', blank=False)
    docfile5 = models.FileField(upload_to='recipes', default='recipes/no-img.jpg', blank=False)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=5000)
    creator = models.ForeignKey(User, blank=True, null=True)
    is_vegan = models.BooleanField(default=False)
    is_vegetarian = models.BooleanField(default=False)
    is_gluten_free = models.BooleanField(default=False)
    is_dairy_free = models.BooleanField(default=False)
    is_nut_free = models.BooleanField(default=False)
    __str__ = lambda self: self.name

class UserProfile(models.Model):
    def get_public_location(self):
        g = Geocoder.geocode(self.location)
        return g.neighborhood if g.neighborhood else g.postal_code # alternatively g.locality or g.sublocality g.colloquial_area, etc.
    def upcoming_events(self):
        from base.models import HostedMeal
        from base.api import RecipeSerializer
        class MealPurchaseSerializer(serializers.ModelSerializer):
            recipe = RecipeSerializer(source="recipe")
            class Meta:
                model = HostedMeal 
        import pytz        
        start_date = datetime.now(pytz.utc) 
        serializer = MealPurchaseSerializer(HostedMeal.objects.filter(meal_purchases__purchaser=self.user, start_time__gt=start_date).distinct(), many=True)
        return serializer.data
    def recent_activities(self):
        from base.models import HostedMeal
        from base.api import RecipeSerializer
        class MealPurchaseSerializer(serializers.ModelSerializer):
            recipe = RecipeSerializer(source="recipe")
            class Meta:
                model = HostedMeal 
        import pytz        
        start_date = datetime.now(pytz.utc) 
        serializer = MealPurchaseSerializer(HostedMeal.objects.filter(host=self.user, start_time__lte=start_date).distinct(), many=True)
        return serializer.data
    def hosted_meals(self):
        from base.models import HostedMeal
        from base.api import RecipeSerializer
        class MealPurchaseSerializer(serializers.ModelSerializer):
            recipe = RecipeSerializer(source="recipe")
            class Meta:
                model = HostedMeal
        serializer = MealPurchaseSerializer(HostedMeal.objects.filter(host=self.user).distinct(), many=True)
        return serializer.data
    def meals_attended(self):
        from base.models import HostedMeal
        from base.api import RecipeSerializer
        class MealPurchaseSerializer(serializers.ModelSerializer):
            recipe = RecipeSerializer(source="recipe")
            class Meta:
                model = HostedMeal 
        import pytz        
        start_date = datetime.now(pytz.utc) 
        serializer = MealPurchaseSerializer(HostedMeal.objects.filter(meal_purchases__purchaser=self.user, start_time__lte=start_date).distinct(), many=True)
        return serializer.data
    def __str__(self):
        return self.user.username
    user = models.OneToOneField(User)
    location = models.CharField(max_length=500, blank=False)
    estimated_latitude = models.DecimalField(max_digits=11,decimal_places=8, default=Decimal('0.00') )
    estimated_longitude = models.DecimalField(max_digits=11,decimal_places=8, default=Decimal('0.00'))
    contact_phone = models.CharField(max_length=15, blank=False)
    level = models.IntegerField(default=1, editable=False)
    upcooking_score = models.IntegerField(default=10, editable=False)
    paypal_payout_email = models.CharField(max_length=200, blank=False)
    is_first_time = models.BooleanField(default=True, editable=False)
    remind_me_later = models.BooleanField(default=True)
    about_me = models.CharField(max_length=2000, default='Something about me...')
    docfile = models.FileField(upload_to='profiles', default='profiles/no-img.jpg', blank=True)
    about_me = models.CharField(max_length=1000, blank=False)

class MealPurchase(models.Model):
    purchaser = models.ForeignKey(User, blank=True, null=True)
    quantity = models.IntegerField(default=1)
    __str__ = lambda self: str(self.purchaser)+" bought "+str(self.quantity)
            
class HostedMeal(models.Model):
    def creator_profile_id(self):
        return self.host.profile().pk 
    def meal_purchases_details(self):
        return self.meal_purchases
    def meal_purchases_total(self):
        return reduce(lambda x,y: x+y.quantity,list(self.meal_purchases.all()),0)
    def local_start_time(self):
        profile = self.host.get_profile()
        defaultTZ = timezone.get_default_timezone()
        return self.start_time.astimezone(defaultTZ)
    recipe = models.ForeignKey(Recipe)
    host = models.ForeignKey(User, related_name="host")
    location = models.CharField(max_length=500,validators=[validate_location])
    start_time = models.DateTimeField(validators=[validate_starttime])
    is_sitdown = models.BooleanField(default=True) #fix me
    is_pickup = models.BooleanField(default=False) #fix me    
    price_per_serving = models.DecimalField(max_digits=5,decimal_places=2,validators=[validators.MinValueValidator(Decimal('0.01'))]) #fix me
    minimum_diners_required = models.IntegerField(validators=[validators.MinValueValidator(1)])
    maximum_diners_allowed = models.IntegerField(validators=[validators.MinValueValidator(1)])
    contact_phone = models.CharField(max_length=15, validators=[validators.RegexValidator(
                                                                                          r'^\d\d\d-?\d\d\d-?\d\d\d\d$',
                                                                                          'Please enter in xxx-xxx-xxxx format')]) #fix me
    meal_purchases = models.ManyToManyField(MealPurchase, blank=True)
    #todo diners must be unique
    #todo diners.length cannot be larger than maximum_diners_allowed
    did_you_host_the_meal = models.BooleanField(default=False) 
    __str__ = lambda self: str(self.start_time)+"@"+str(self.location)

    def clean(self):
        if self.is_pickup==False and self.is_sitdown==False:
            raise ValidationError({"is_sitdown":["Pick up and/or sit down need to be true."]})
        if self.minimum_diners_required > self.maximum_diners_allowed:
            raise ValidationError({"minimum_diners_required":["Minimum diners required must be less than or equal to the maximum diners allwoed."]})
        if self.did_you_host_the_meal and timezone.now()<self.start_time:
            raise ValidationError("This event hasn't occurred yet.")

        
class HostedMealReview(models.Model):
    user = models.ForeignKey(User)
    hosted_meal = models.ForeignKey(HostedMeal)
    did_you_show_up = models.BooleanField(default=True)
    did_the_hosted_meal_happen = models.BooleanField(default=True)
    rating = models.IntegerField(default=5)
    comments = models.CharField(max_length=1000, blank=True, null=True)

class HostsReviewOfDiners(models.Model):
    hosted_meal = models.ForeignKey(HostedMeal)
    user = models.ForeignKey(User)
    did_they_show_up = models.BooleanField(default=True)
    rating = models.IntegerField(default=5)
    comments = models.CharField(max_length=1000, blank=True, null=True)

def user_create(sender, instance, signal, *args, **kwargs):
    if not instance.is_superuser:
        profile, new = UserProfile.objects.get_or_create(user=instance)

User.userprofile = property(lambda x: UserProfile.objects.get_or_create(user=x)[0])
User.profile = lambda x: UserProfile.objects.get_or_create(user=x)[0]
User.get_profile = lambda x: UserProfile.objects.get_or_create(user=x)[0]
post_save.connect(user_create, sender=User)
