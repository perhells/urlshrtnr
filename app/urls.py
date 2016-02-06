from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.make, name='make'),
    url(r'^go/(?P<shortened>.+)/$', views.go, name='go'),
    url(r'^success/(?P<shortened>.+)/$', views.success, name='success'),
]
