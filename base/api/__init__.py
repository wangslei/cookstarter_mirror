from django.conf.urls import url, patterns, include
from rest_framework import viewsets, routers, serializers
from django.contrib.auth.models import User, Group
from base.models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User 
class UserProfileSerializer(serializers.ModelSerializer):
    upcoming_events = serializers.Field(source='upcoming_events')
    recent_activities = serializers.Field(source='recent_activities')
    hosted_meals = serializers.Field(source='hosted_meals')
    meals_attended = serializers.Field(source='meals_attended')
    user_field = UserSerializer(source='user', read_only=True)
    docfile = serializers.ImageField(source='docfile', blank=True)
    class Meta:
        model = UserProfile
class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
class HostedMealReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = HostedMealReview
class HostsReviewOfDinersSerializer(serializers.ModelSerializer):
    class Meta:
        model = HostsReviewOfDiners
class MealPurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = MealPurchase
class RecipeSerializer(serializers.ModelSerializer):
    creator_read_only = UserSerializer(source='creator_read_only')
    creator_upcooking_score = serializers.Field(source='upcooking_score')
    creator_profile_id = serializers.Field(source='creator_profile_id')
    class Meta:
        model = Recipe
class HostedMealSerializer(serializers.ModelSerializer):
    local_start_time = serializers.Field(source='local_start_time')
    recipe_detail = RecipeSerializer(source='recipe', read_only=True)
    host_detail = UserSerializer(source='host', read_only=True)
    host_profile_detail = UserProfileSerializer(source='host.profile', read_only=True)
    meal_purchases_detail = MealPurchaseSerializer(source='meal_purchases_details', read_only=True)
    meal_purchases_total = serializers.Field(source='meal_purchases_total')
    creator_profile_id = serializers.Field(source='creator_profile_id')
    class Meta:
        model = HostedMeal



class UserProfileSelfModelViewSet(viewsets.ModelViewSet):
    model = UserProfile
    serializer_class = UserProfileSerializer
    def get_queryset(self):
        return UserProfile.objects.filter(user=self.request.user)
class UserSelfModelViewSet(viewsets.ModelViewSet):
    model = User
    serializer_class = UserSerializer
    def get_queryset(self):
        return User.objects.filter(pk=self.request.user.pk)
class UserProfileModelViewSet(viewsets.ModelViewSet):
    model = UserProfile
    serializer_class = UserProfileSerializer
class GroupModelViewSet(viewsets.ModelViewSet):
    model = Group
    serializer_class = GroupSerializer
class UserModelViewSet(viewsets.ModelViewSet):
    model = User
    serializer_class = UserSerializer
class HostedMealReviewModelViewSet(viewsets.ModelViewSet):
    model = HostedMealReview
    serializer_class = HostedMealReviewSerializer
class HostsReviewOfDinersModelViewSet(viewsets.ModelViewSet):
    model = HostsReviewOfDiners
    serializer_class = HostsReviewOfDinersSerializer
class MealPurchaseModelViewSet(viewsets.ModelViewSet):
    model = MealPurchase
    serializer_class = MealPurchaseSerializer
class HostedMealModelViewSet(viewsets.ModelViewSet):
    model = HostedMeal
    serializer_class = HostedMealSerializer
class RecipeModelViewSet(viewsets.ModelViewSet):
    model = Recipe
    serializer_class = RecipeSerializer


router = routers.DefaultRouter()
router.register(r'user', UserModelViewSet)
router.register(r'groups', GroupModelViewSet)
router.register(r'UserProfile', UserProfileModelViewSet)
router.register(r'HostedMealReview', HostedMealReviewModelViewSet)
router.register(r'HostsReviewOfDiners', HostsReviewOfDinersModelViewSet)
router.register(r'MealPurchase', MealPurchaseModelViewSet)
router.register(r'HostedMeal', HostedMealModelViewSet)
router.register(r'Recipe', RecipeModelViewSet)
router.register(r'user_self', UserSelfModelViewSet)
router.register(r'userprofile_self', UserProfileSelfModelViewSet)

