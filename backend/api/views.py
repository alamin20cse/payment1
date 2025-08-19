from django.shortcuts import render


from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import UserRegisterSerializer, UserSerializer,ProductSerializer
from rest_framework.permissions import IsAuthenticated,AllowAny
from .models import Product

from rest_framework import mixins,viewsets,status


from django.contrib.auth import get_user_model


from rest_framework import views,viewsets,generics,mixins
User = get_user_model()

# -------------------------
# User Registration
# -------------------------
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes = [AllowAny]  # Anyone can register


# -------------------------
# User ViewSet (Profile)
# -------------------------
class UserViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]
#GET /api/user/profile/
# api/router register name/functon name/
    @action(detail=False, methods=['get'])
    def profile(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)
    



class ProductViewSet(    
    mixins.CreateModelMixin,     # POST
    mixins.ListModelMixin,       # GET (list)
    mixins.RetrieveModelMixin,   # GET (detail)
    mixins.DestroyModelMixin,    # DELETE
    mixins.UpdateModelMixin,     # PUT / PATCH (update)
    viewsets.GenericViewSet
):
    permission_classes=[AllowAny]
    queryset=Product.objects.all()
    serializer_class=ProductSerializer

    # def create(self, request, *args, **kwargs):
    #     serializer = ProductSerializer(data=request.data)
    #     if serializer.is_valid():
    #         instance = serializer.save()
    #         return Response(
    #         {"insertedId": instance.id},
    #         status=status.HTTP_201_CREATED
    #     )
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
