"""urlconf for the base application"""

from django.conf.urls import url, patterns, include
from django.conf import settings
from base.api import router

urlpatterns = patterns('base.views',
    url(r'^login/$', 'login_view', name='login'),
    url(r'^logout/$', 'logout_view', name='logout'),
    url(r'^register/$', 'register_view', name='register'),
    url(r'^$', 'home', name='home'),
    url(r'^recipe/create/$', 'create_recipe', name='create_recipe'),
    url(r'^recipe/edit/(\d+)/$', 'edit_recipe', name='edit_recipe'),
    url(r'^recipe/clone/(\d+)/$', 'clone_recipe', name='clone_recipe'),
    url(r'^profile/(\d+)/$', 'update_profile', name='update_profile'),
    url(r'^api/v1/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)

if settings.DEBUG :
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    )