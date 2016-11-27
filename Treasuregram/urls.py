from django.conf.urls import include, url
from django.contrib import admin
from main_app import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'Treasuregram.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    #admin local host
    url(r'^index/', views.index),
]
