from django.urls import path
from .views import *

urlpatterns = [

    path('wq', home, name='home'),

]