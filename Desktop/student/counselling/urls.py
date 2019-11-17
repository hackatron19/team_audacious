from django.conf.urls import include, url

from .views import SampleView

from django.urls import path, include
from django.conf import settings
from . import views
from django.conf.urls.static import static

urlpatterns = [
   path('', views.index, name='index'),
   path('home/', views.home, name='home'),


]
