from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'demo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include('demo.api.urls')),
    url(r'^view/', include('demo.views.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
