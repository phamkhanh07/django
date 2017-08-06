from django.conf.urls import include, url
from django.contrib import admin



#urlpatterns = [
    # Examples:
    # url(r'^$', 'sample1.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

#    url(r'^admin/', include(admin.site.urls)),
#]


from helloworld.views import greeting
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',greeting)
]