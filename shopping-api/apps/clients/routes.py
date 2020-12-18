from django.urls import path
from rest_framework.authtoken import views

urlpatterns = [path("api-auth/", views.obtain_auth_token)]
