from django.urls import path
from rest_framework import routers
from .views import UserViewSet,RegisterView


route=routers.DefaultRouter()
route.register('user', UserViewSet, basename='user')  # for profile endpoint
urlpatterns = [
     path("register/", RegisterView.as_view(), name="register"),
  
]
