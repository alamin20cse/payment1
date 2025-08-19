from django.urls import path,include
from rest_framework import routers
from .views import UserViewSet,RegisterView,ProductViewSet


route=routers.DefaultRouter()
route.register('user', UserViewSet, basename='user')  # for profile endpoint
route.register('products', ProductViewSet, basename='products')  # for profile endpoint

urlpatterns = [
     path("register/", RegisterView.as_view(), name="register"),
     # path('products/',ProductViewSet,name='products')
      path('', include(route.urls)),
  
]
