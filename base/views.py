""" Views for the base application """

from django.shortcuts import render, render_to_response
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm, ImageField
from base.api import Recipe, RecipeSerializer, UserProfile, UserProfileSerializer
from django.contrib.auth.models import User, Group
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.decorators import api_view
import json

def home(request):
    """ Default view for the root """
    return render(request, 'base/home.html', {'user': request.user})

class RecipeForm(ModelForm):
    class Meta:
        model = Recipe

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)
         
@api_view(['POST'])                
def create_recipe(request):
    if request.method == 'POST' and request.user.is_authenticated:
        print(request.FILES)
        form = RecipeForm(request.POST, request.FILES)
        is_valid = form.is_valid()
        if is_valid:
            recipe = form.save()
            serializer = RecipeSerializer(recipe)
            return JSONResponse(serializer.data, status=201)
        else:
            return Response(form.errors, status=400)

@api_view(['POST'])                
def edit_recipe(request, id):
    recipe=Recipe.objects.get(pk=id)
    if request.method == 'POST' and request.user.is_authenticated:
        print(request.FILES)
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        is_valid = form.is_valid()
        if is_valid:
            recipe = form.save()
            serializer = RecipeSerializer(recipe)
            return JSONResponse(serializer.data, status=201)
        else:
            return Response(form.errors, status=400)

@api_view(['POST'])                
def clone_recipe(request, id):
    recipe=Recipe.objects.get(pk=id)
    recipe.pk=None
    recipe.creator = request.user
    recipe.save()
    serializer = RecipeSerializer(recipe)
    return JSONResponse(serializer.data, status=201)
        
class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ('docfile',)

@api_view(['POST'])                
def update_profile(request, profile_id):
    int_profile_id = int(profile_id)
    if request.user.get_profile().pk != int_profile_id:
        int_profile_id = User.objects.get(pk=int_profile_id).get_profile().pk
    if request.user.is_authenticated and request.user.get_profile().pk == int_profile_id:
        if len(request.FILES) == 0:
            doc_error = {'docfile': {'errors': 'You must specify a file'}}
            return Response(doc_error, status=400)
        else:
            profile = UserProfile.objects.get(pk=int_profile_id)
            form = UserProfileForm(request.POST, request.FILES, instance=profile)        
            is_valid = form.is_valid()
            if is_valid:
                recipe = form.save()
                serializer = UserProfileSerializer(recipe)
                return JSONResponse(serializer.data, status=201)
            else:
                return Response(form.errors, status=400)
            
def login_view(request):
    """ login """
    if request.method == "POST":
	    POST = json.loads(request.body)
	    username = POST.get('username', '')
	    password = POST.get('password', '')
	    user = authenticate(username=username, password=password)
	    if user is not None: 
	        if user.is_active:
				login(request, user)
				return HttpResponse('{"success": true}')
		return HttpResponse('{"success": false}')
    elif request.user.is_authenticated(): #get is either logged in
		return HttpResponse('{"success": true}')
    else: #get is not logged in.
		return HttpResponse('{"success": false}')
    return HttpResponse('{"success": false}')

def logout_view(request):
    """ logout """
    logout(request)
    return HttpResponse('{"success": true}')

def register_view(request):
    """ register """
    if request.method == "POST":
        POST = json.loads(request.body)
        POST["username"] = POST.get("username", "")
        POST["password1"] = POST.get("password1", "")
        POST["password2"] = POST.get("password2", "")
        form = UserCreationForm(POST)
        if form.is_valid():
            new_user = form.save()
            user = authenticate(username=POST["username"], password=POST["password1"])
            login(request, user)
            return HttpResponse('{"success": true}')
        else: 
            return HttpResponse(json.dumps(form._errors))
    return HttpResponse('{"success": false}')
