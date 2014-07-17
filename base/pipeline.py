from social_auth.backends.facebook import FacebookAuth
from urllib import urlretrieve, urlopen
from django.conf import settings
from base.models import UserProfile
import sys
import json

def custom_load_extra_data(request, *args, **kwargs):
    if kwargs["is_new"]:
        userProfile = UserProfile.objects.get(user__username=kwargs["username"])
        try:
            url = None
            if isinstance(kwargs['auth'], FacebookAuth):
                url = "https://graph.facebook.com/%s?fields=location,address&access_token=%s" \
                            % (kwargs["username"], kwargs["response"]["access_token"])
            if url:
                file = urlopen(url)
                location_dict = json.loads(file.read())
                userProfile.location = location_dict["location"]["name"]
            url = None
            if isinstance(kwargs['auth'], FacebookAuth):
                url = "https://graph.facebook.com/%s/picture?type=normal&access_token=%s" \
                            % (kwargs["username"], kwargs["response"]["access_token"])
            if url:
                #eg /home/ec2-user/personal/upcooking/media
                mediaLocation = "profiles/"+kwargs["username"]+".jpg"
                urlretrieve(url, settings.MEDIA_ROOT + "/" + mediaLocation)
                userProfile.docfile = mediaLocation
                try:
                    timezone = kwargs["response"]["timezone"]
                except:
                    timezone = "-4"
                userProfile.save()
        except:
            print(sys.exc_info())
        finally:
            pass

