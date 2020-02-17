from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from address.models import Address
from address.address_serializer import AddressSerializer

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser,\
    IsAuthenticatedOrReadOnly, DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly

from address.permissions import MyReadOnly


# Create your views here.
class AddressOperations(ModelViewSet):
    queryset = Address.active_ent.all()
    serializer_class = AddressSerializer

    # permission_classes = [MyReadOnly, ]
    # authentication_classes = [TokenAuthentication, ]#Local Authenticatoion
    # permission_classes = [IsAuthenticated, ]



