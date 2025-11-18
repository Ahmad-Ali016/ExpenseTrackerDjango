from django.urls import include, path
from accounts.views import *

urlpatterns = [
path('login/',login_view , name='login'),
path('logout/',logout_view ,name='logout'),
]