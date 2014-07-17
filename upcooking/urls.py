""" Default urlconf for upcooking """

from django.conf.urls import include, patterns, url
from django.contrib import admin
from base.models import Recipe, HostedMeal, HostedMealReview, HostsReviewOfDiners, UserProfile
admin.autodiscover()

models = [Recipe, HostedMeal, HostedMealReview, HostsReviewOfDiners, UserProfile]
map(admin.site.register, models)

def bad(request):
    """ Simulates a server error """
    1 / 0

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'upcooking.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'', include('social_auth.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^bad/$', bad),
    url(r'', include('base.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)

