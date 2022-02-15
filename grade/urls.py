from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^grade/$', views.Grade.as_view()),
]
