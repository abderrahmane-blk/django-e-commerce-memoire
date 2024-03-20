from django.urls import path ,include
from django.contrib.auth import urls as auth_urls
from .views import *


urlpatterns = [
path('test-login/', test_if_logged_in , name='login-test'),
path('register-vendor/', register_vendor , name='new-vendor'),

path('' , include(auth_urls)),

]